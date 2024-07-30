from audios import (gen_unreal_audio, gen_azure_audio,
                    unreal_voices, voice_mapping)
from texts import extract_text, extract_advanced_text
from images import resize_image
from videos import join_videos
from functools import partial
from PIL import Image
import gradio as gr
import numpy as np

def delete_item(index: int, *item_list: list[str]) -> list[str]:
    """
    Receives an index and a list of items and returns a new list
    without the item at the given index.
    """
    return [x for i, x in enumerate(item_list) if i != index]

def delete_item_list(index: int, item_list: list[str]) -> list[str]:
    """
    Delete the item at the given index and return the updated list.
    """
    return delete_item(index, *item_list)

def delete_and_decrement(index: int, item_list: list[str]
                         ) -> tuple[list[str], int]:
    """
    Delete the item at the given index and decrement count
    """
    return delete_item(index, *item_list), len(item_list) - 1

def set_order(index: int, order: str,
              order_info: dict[int, int]) -> dict[int, int]:
    order_info = dict(order_info)
    order_info[index] = int(order)
    return order_info

def save_image_texts(order_info: dict[int, int], *text_list: list[str], 
                     ) -> tuple[list[str], list[None]]:
    """
    Reorder the texts and save it in the state to be used in the
    next step and return a list of None to clear the audios.
    """
    ordered_texts: list[tuple[int, str]] = list()
    for index, text in enumerate(text_list):
        order = order_info.get(index, index + 1) - 1
        ordered_texts.append((order, text))
    ordered_texts = sorted(ordered_texts, key=lambda x: x[0])
    ordered_texts = [x[1] for x in ordered_texts]
    return ordered_texts, [None for _ in range(len(text_list))]

def resize_and_extract_text(image: Image) -> tuple[np.ndarray, list[str]]:
    """
    Resize the image and extract the text from it, returning
    the resized image and the list of extracted texts.
    """
    resized_image = resize_image(image)
    text_list = extract_text(resized_image)
    return resized_image, text_list

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

def add_new_audio(count: int, audio_list: list[str]) -> tuple[int, list[str]]:
    """
    Add a new audio to the list and increment the count.
    """
    return count + 1, audio_list + [None]

def save_bg_audio(index: int, new_audio: str,
                  audio_list: list[str]) -> list[str]:
    """
    Save the audio path in the list and return the updated list.
    """
    audio_list[index] = new_audio
    return audio_list

def image_to_text_tab(text_state: gr.State, order_state: gr.State,
                      r_text_state: gr.State, audio_state: gr.State):
    with gr.Row():
        with gr.Column():
            with gr.Row():
                normal_btn = gr.Button("Extrair texto")
                advanced_btn = gr.Button("Extrair texto avançado")

            image_input = gr.Image(label="Imagem da página", type="pil")
            image_input.upload(fn=resize_and_extract_text,
                               inputs=image_input, 
                               outputs=[image_input, text_state])
            normal_btn.click(fn=extract_text,
                             inputs=image_input,
                             outputs=[text_state])
            advanced_btn.click(fn=extract_advanced_text,
                               inputs=image_input,
                               outputs=[text_state])

            gr.Examples(
                inputs=[image_input],
                examples=[
                    ["./examples/greatest_00.jpg"],
                    ["./examples/greatest_01.jpg"],
                    ["./examples/greatest_02.jpg"],
                    ["./examples/greatest_03.jpg"],
                    ["./examples/greatest_04.jpg"],
                ]
            )

        @gr.render(inputs=[text_state, order_state],
                   triggers=[text_state.change])
        def show_text_rows(text_list: list[str], order_info: dict[int, str]):
            order_list = [str(i+1) for i in range(len(text_list))]
            with gr.Column():
                text_inputs = list()
                for index, text_value in enumerate(list(text_list)):
                    with gr.Row():
                        curr_order = order_info.get(index, index+1)
                        order = gr.Dropdown(label="Ordem do balão",
                                            choices=order_list,
                                            value=str(curr_order))
                        bti = gr.Button(value="✖️", variant="stop", size="sm")
                    ti = gr.Textbox(value=text_value, label=f"Balão {index+1}")
                    order.change(fn=partial(set_order, index),
                                 inputs=[order, order_state],
                                 outputs=[order_state])
                    bti.click(fn=partial(delete_item, index),
                              inputs=text_inputs,
                              outputs=[text_state])
                    text_inputs.append(ti)
                with gr.Row():
                    add_text_btn = gr.Button("Adicionar texto")
                    image_button = gr.Button("Submeter transcrições",
                                                visible=len(text_list) > 0)
                add_text_btn.click(fn=lambda *x: x + ("",),
                                   inputs=text_inputs,
                                   outputs=[text_state])
                image_button.click(fn=save_image_texts,
                                   inputs=[order_state] + text_inputs,
                                   outputs=[r_text_state, audio_state])
    return image_input

def text_to_audio_tab(text_state: gr.State, audio_state: gr.State):
    @gr.render(inputs=[text_state, audio_state], triggers=[text_state.change])
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

def scenes_to_movie_tab(video_state: gr.State):
    bg_audio_state = gr.State(list())
    bg_count_state = gr.State(0)

    with gr.Row():
        @gr.render(inputs=[video_state], triggers=[video_state.change])
        def list_scenes(video_list: list[str]):
            with gr.Column():
                for index, text_value in enumerate(list(video_list)):
                    gr.Video(label=f"Cena {index+1}", value=text_value,
                             interactive=False)
                    bvi = gr.Button(value="✖️", variant="stop",
                                    size="sm")
                    bvi.click(fn=partial(delete_item_list, index),
                              inputs=[video_state],
                              outputs=[video_state])

        @gr.render(inputs=[bg_audio_state, bg_count_state],
                   triggers=[bg_count_state.change])
        def list_bg_audios(audio_list: list[str], audio_count: int):
            with gr.Column():
                for index in range(audio_count):
                    with gr.Row():
                        audio_output = gr.Audio(label=f"Áudio {index+1}",
                                                value=audio_list[index],
                                                type="filepath")
                        bai = gr.Button(value="✖️", variant="stop",
                                        size="sm")
                        bai.click(fn=partial(delete_and_decrement, index),
                                  inputs=[bg_audio_state],
                                  outputs=[bg_audio_state, bg_count_state])

                    audio_output.upload(partial(save_bg_audio, index),
                                        inputs=[audio_output, bg_audio_state],
                                        outputs=[bg_audio_state])
    with gr.Row():
        add_bg_btn = gr.Button("Adicionar áudio")
        add_bg_btn.click(fn=add_new_audio,
                        inputs=[bg_count_state, bg_audio_state],
                        outputs=[bg_count_state, bg_audio_state])
        final_button = gr.Button("Gerar filme")
    final_output = gr.Video(label="Filme final", interactive=False)
    final_button.click(fn=join_videos,
                       inputs=[video_state, bg_audio_state],
                       outputs=[final_output])
