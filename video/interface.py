from audios import (concatenate_audios, gen_unreal_audio, get_duration,
                    gen_azure_audio, unreal_voices, voice_mapping)
from images import animate_static_image, resize_image
from videos import add_audio_to_video, join_videos
from functools import partial
from PIL import Image
import gradio as gr
import numpy as np
import pytesseract

def delete_text(index: int, *text_list: list[str]) -> list[str]:
    return [x for i, x in enumerate(text_list) if i != index]

def set_order(index: int, order: str,
              order_info: dict[int, int]) -> dict[int, int]:
    order_info = dict(order_info)
    order_info[index] = int(order)
    return order_info

def save_image_texts(order_info: dict[int, int], *text_list: list[str], 
                     ) -> tuple[list[str], list[None]]:
    ordered_texts: list[tuple[int, str]] = list()
    for index, text in enumerate(text_list):
        order = order_info.get(index, index + 1) - 1
        ordered_texts.append((order, text))
    ordered_texts = sorted(ordered_texts, key=lambda x: x[0])
    ordered_texts = [x[1] for x in ordered_texts]
    return ordered_texts, [None for _ in range(len(text_list))]

def extract_text(image: Image) -> list[str]:
    full_text: str = pytesseract.image_to_string(image)
    return [text for text in full_text.split("\n\n")
            if text.strip() != ""]

def generate_audio_from_text(index: int, text: str, voice: str,
                             audio_list: list[bytes]
                             ) -> tuple[bytes|None, list[bytes]]:
    """
    Call the function to generate an audio file from the given text.
    Returns the generated audio bytes and the updated audio list.
    """
    if voice in unreal_voices:
        audio_bytes = gen_unreal_audio(text, voice)
    else:
        audio_bytes = gen_azure_audio(text, voice)

    if audio_bytes is not None:
        audio_list[index] = audio_bytes
    return audio_bytes, audio_list

def animate_image(image: Image, audio_path: str) -> tuple[str, str]:
    duration = get_duration(audio_path)
    video_path = animate_static_image(image, duration)
    return video_path, video_path

def generate_scene(video_path: str, audio_path: str) -> str:
    return add_audio_to_video(video_path, audio_path)

with gr.Blocks(
    title="Criatividade Computacional"
) as app:
    gr.Markdown("""
# Narrativas inovadoras

> Transforme sua Graphic Novel em um vídeo animado
""")
    text_state = gr.State(list())
    order_state = gr.State(dict())
    r_text_state = gr.State(list())
    audio_state = gr.State(list())

    with gr.Tabs() as tabs:
        with gr.Tab("image-to-text", id="image-to-text"):
            gr.Markdown("""
            ## O que fazer nesta etapa?
            1. Insira a imagem da página da Graphic Novel
            2. Verifique e corrija o texto extraído
            3. Submeta o texto corrigido para a próxima etapa

            > A ordem importa! Aguarde com paciência a geração dos textos...
            """)
            with gr.Row():
                with gr.Column():
                    image_input = gr.Image(label="Imagem da página",
                                           type="pil")
                    image_input.upload(fn=resize_image,
                                       inputs=image_input, 
                                       outputs=image_input)
                    upload_img_btn = gr.Button("Carregar imagem")
                    upload_img_btn.click(fn=extract_text,
                                         inputs=[image_input],
                                         outputs=[text_state])

                @gr.render(inputs=[text_state, order_state],
                           triggers=[text_state.change])
                def show_text_rows(text_list: list[str],
                                   order_info: dict[int, str]):
                    order_list = [str(i+1) for i in range(len(text_list))]
                    with gr.Column():
                        text_inputs = list()
                        for index, text_value in enumerate(list(text_list)):
                            with gr.Row():
                                curr_order = order_info.get(index, index+1)
                                order = gr.Dropdown(label="Ordem do balão",
                                                    choices=order_list,
                                                    value=str(curr_order))
                                bti = gr.Button(value="✖️", variant="stop",
                                                size="sm")
                            ti = gr.Textbox(value=text_value,
                                            label=f"Balão {index+1}")
                            order.change(fn=partial(set_order, index),
                                            inputs=[order, order_state],
                                            outputs=[order_state])
                            bti.click(fn=partial(delete_text, index),
                                        inputs=text_inputs,
                                        outputs=[text_state])
                            text_inputs.append(ti)
                        with gr.Row():
                            add_text_btn = gr.Button("Adicionar texto")
                            image_button = gr.Button("Submeter transcrições")
                        add_text_btn.click(fn=lambda *x: x + ("",),
                                           inputs=text_inputs,
                                           outputs=[text_state])
                        image_button.click(fn=save_image_texts,
                                           inputs=[order_state] + text_inputs,
                                           outputs=[r_text_state, audio_state])

        with gr.Tab("text-to-audio", id="text-to-audio"):
            gr.Markdown("""## Geração dos áudios
            1. Ordene e corrija os textos de cada parágrafo
            2. Gere os áudios que serão unidos
            3. Submeta os áudios para a próxima etapa
            """)
            @gr.render(inputs=[r_text_state, audio_state],
                       triggers=[r_text_state.change])
            def show_audio_rows(img_texts: list[str], audios: list[np.ndarray]):
                for index, text_value in enumerate(list(img_texts)):
                    with gr.Row():
                        with gr.Column():
                            voice_select = gr.Dropdown(choices=voice_mapping,
                                                       label="Voz do áudio",
                                                       value=voice_mapping[0])
                            text_input = gr.Textbox(value=text_value,
                                                    label=f"Balão {index+1}")
                            generate_btn = gr.Button("Regerar áudio")
                        audio_output = gr.Audio(label=f"Áudio {index+1}",
                                                value=audios[index],
                                                interactive=False)
                    gr.Markdown("---")
                    generate_btn.click(partial(generate_audio_from_text, index),
                                        inputs=[text_input, voice_select, audio_state],
                                        outputs=[audio_output, audio_state])
            audio_button = gr.Button("Submeter áudios")

        with gr.Tab("image-to-video", id="image-to-video"):
            gr.Markdown("""## Transforme a página em uma animação
            1. A imagem é selecionada na primeira etapa.
            2. Recorte e edite a imagem assim como quiser.
            3. Submeta a imagem para gerar uma animação até ficar satisfeito.
            """)
            with gr.Row():
                video_reference_image = gr.ImageEditor(interactive=True)
                video_output = gr.Video(interactive=False)
            video_button = gr.Button("Regerar vídeo")
        image_input.change(fn=lambda x: x, inputs=image_input,
                           outputs=[video_reference_image])

        with gr.Tab("product", id="product"):
            gr.Markdown("""## Gerar a cena
            1. Verifique se o áudio agrupado na etapa 2 está correto.
            2. Verifique se a imagem animada na etapa 3 está correta.
            3. Submeta para unir o áudio e a imagem animada.
            """)
            with gr.Row():
                with gr.Column():
                    video_input = gr.Video(label="Imagem animada",
                                           interactive=False)
                    audio_input = gr.Audio(label="Áudio unido",
                                           interactive=False,
                                           type="filepath")
                animation_output = gr.Video(label="Cena dublada",
                                            interactive=False)

            animation_button = gr.Button("Gerar cena")
            animation_button.click(generate_scene,
                                   [video_output, audio_input],
                                   [animation_output])

        audio_button.click(fn=concatenate_audios,
                            inputs=[audio_state],
                            outputs=audio_input)
        video_button.click(fn=animate_image,
                            inputs=[image_input, audio_input],
                            outputs=[video_output, video_input])
if __name__ == "__main__":
    app.queue().launch()
