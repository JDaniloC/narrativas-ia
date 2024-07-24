from audios import concatenate_audios, gen_unreal_audio, unreal_voices
from functools import partial
import gradio as gr
import numpy as np
import pytesseract

def extract_text(image: np.ndarray) -> list[str]:
    full_text = pytesseract.image_to_string(image)
    return [text for text in full_text.split("\n\n") if text.strip() != ""]

def delete_text(index: int, *text_list: list[str]) -> list[str]:
    return [x for i, x in enumerate(text_list) if i != index]

def save_image_texts(*text_list: list[str]) -> tuple[list[str], list[None]]:
    gr.Tabs(selected="text-to-audio")
    return text_list, [None for _ in range(len(text_list))]

def generate_audio_from_text(index: int, text: str, voice: str,
                             audio_list: list[bytes]
                             ) -> tuple[bytes|None, list[bytes]]:
    """
    Call the function to generate an audio file from the given text.
    Returns the generated audio bytes and the updated audio list.
    """
    audio_bytes = gen_unreal_audio(text, voice)
    if audio_bytes is not None:
        audio_list[index] = audio_bytes
    return audio_bytes, audio_list

def animate_image(image: np.ndarray) -> tuple[str, str]:
    return "./videos/1_0.mp4", "./videos/1_0.mp4"

def generate_scene(video: np.ndarray, audios: list[np.ndarray]) -> str:
    return "./videos/1_0.mp4"

with gr.Blocks(
    title="Criatividade Computacional"
) as app:
    gr.Markdown("""
# Narrativas inovadoras

> Transforme sua Graphic Novel em um vídeo animado
""")
    text_state = gr.State([])
    r_text_state = gr.State([])
    audio_state = gr.State([])

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
                    image_input = gr.Image()
                    upload_img_btn = gr.Button("Carregar imagem")
                    upload_img_btn.click(fn=extract_text,
                                         inputs=[image_input],
                                         outputs=[text_state])

                @gr.render(inputs=[text_state], triggers=[text_state.change])
                def show_text_rows(text_list: list[str]):
                    with gr.Column():
                        text_inputs = list()
                        for index, text_value in enumerate(list(text_list)):
                            with gr.Row():
                                ti = gr.Textbox(value=text_value,
                                                label=f"Balão {index+1}")
                                bti = gr.Button(value="✖️", variant="stop",
                                                size="sm")
                                bti.click(fn=partial(delete_text, index),
                                          inputs=text_inputs,
                                          outputs=[text_state])
                            text_inputs.append(ti)
                        image_button = gr.Button("Submeter transcrições")
                        image_button.click(fn=save_image_texts,
                                           inputs=text_inputs,
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
                            text_input = gr.Textbox(value=text_value,
                                                    label=f"Balão {index+1}")
                            voice_select = gr.Dropdown(choices=unreal_voices,
                                                        label="Voz do áudio",
                                                        value="Scarlett")
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
                                           interactive=False)
                animation_output = gr.Video(label="Cena dublada",
                                            interactive=False)

            animation_button = gr.Button("Gerar cena")
            animation_button.click(generate_scene,
                                   [video_output, audio_state],
                                   [animation_output])

        audio_button.click(fn=concatenate_audios,
                            inputs=[audio_state],
                            outputs=[audio_input])
        video_button.click(fn=animate_image,
                            inputs=image_input,
                            outputs=[video_output, video_input])
if __name__ == "__main__":
    app.queue().launch()
