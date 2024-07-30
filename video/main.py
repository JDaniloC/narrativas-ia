from interface import image_to_text_tab, text_to_audio_tab, scenes_to_movie_tab
from audios import concatenate_audios, get_duration
from images import animate_static_image
from videos import add_audio_to_video
from PIL import Image
import gradio as gr

def animate_image(image: Image, audio_path: str) -> tuple[str, str]:
    """
    Animate the image and put an audio if it is given.
    If the audio is not given, the video will be silent.
    If the image is not given, the function will return None.
    """
    if image is None: return None, None

    duration = 5
    if audio_path is not None:
        duration = get_duration(audio_path) + 1
    video_path = animate_static_image(image, duration)
    return video_path, video_path

with gr.Blocks(
    title="Criatividade Computacional"
) as app:
    gr.Markdown("""
# Narrativas inovadoras

> Transforme sua Graphic Novel em um vídeo animado
""")
    # Variables
    text_state = gr.State(list())
    order_state = gr.State(dict())
    r_text_state = gr.State(list())
    audio_state = gr.State(list())

    video_state = gr.State(list())

    with gr.Tabs() as tabs:
        with gr.Tab("image-to-text", id="image-to-text"):
            gr.Markdown("""
            ## O que fazer nesta etapa?
            1. Insira a imagem da página da Graphic Novel
            2. Corrija a ordenação dos textos e adicione novos se precisar
            2. Verifique e corrija cada um dos textos extraídos
            3. Submeta o texto corrigido para a próxima etapa

            > A ordem importa! Aguarde com paciência a geração dos textos...
            """)
            image_input = image_to_text_tab(text_state, order_state,
                                            r_text_state, audio_state)

        with gr.Tab("text-to-audio", id="text-to-audio"):
            gr.Markdown("""## Geração dos áudios
            1. Ordene e corrija os textos de cada parágrafo
            2. Gere os áudios que serão unidos
            3. Submeta os áudios para a próxima etapa
            """)
            text_to_audio_tab(r_text_state, audio_state)
            audio_button = gr.Button("Submeter áudios")

        with gr.Tab("image-to-video", id="image-to-video"):
            gr.Markdown("""## Transforme a página em uma animação
            1. A imagem é selecionada na primeira etapa.
            2. Recorte e edite a imagem assim como quiser.
            3. Submeta a imagem para gerar uma animação até ficar satisfeito.
            """)
            with gr.Row():
                video_image_ref = gr.ImageEditor(interactive=True)
                video_output = gr.Video(interactive=False)
            video_button = gr.Button("Regerar vídeo")
            image_input.change(fn=lambda x: x,
                               inputs=image_input,
                               outputs=[video_image_ref])

        with gr.Tab("video-to-scene", id="video-to-scene"):
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
                                            type="filepath")
                scene_output = gr.Video(label="Cena dublada",
                                            interactive=False)
            scene_button = gr.Button("Gerar cena")
            scene_button.click(fn=add_audio_to_video,
                               inputs=[video_output, audio_input, video_state],
                               outputs=[scene_output, video_state])

            audio_button.click(fn=concatenate_audios,
                               inputs=[audio_state],
                               outputs=audio_input)
            video_button.click(fn=animate_image,
                               inputs=[image_input, audio_input],
                               outputs=[video_output, video_input])

        with gr.Tab("scene-to-movie", id="scene-to-movie"):
            gr.Markdown("""## Gerar o filme
            Todas as cenas aqui apresentadas são geradas pelas etapas anteriores na ordem.
            1. Remova as cenas não desejadas.
            2. Selecione músicas de fundo que serão unidos.
            3. Submeta para unir os vídeos e as músicas de fundo.
            """)
            scenes_to_movie_tab(video_state)

if __name__ == "__main__":
    app.queue().launch()