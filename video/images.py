from moviepy.editor import ImageClip, CompositeVideoClip
from PIL import Image
import numpy as np
import tempfile

def resize_image(image: Image) -> Image:
    """
    If the image has the width greater than 1024px, resizes the
    image to a max width of 1024px keeping the aspect ratio
    """
    if image.mode == "RGBA":
        image = image.convert("RGB")
    MAX_WIDTH = 1024
    width, height = image.size
    if width <= MAX_WIDTH:
        return image

    aspect_ratio = width / height
    new_width = MAX_WIDTH
    new_height = int(MAX_WIDTH / aspect_ratio)
    return image.resize((new_width, new_height), Image.LANCZOS)

def animate_static_image(image: Image, duration: int):
    """
    Creates a video with the static image where will
    scrolls to bottom til the duration ends
    """
    clip = ImageClip(np.array(image), transparent=False)
    HEIGHT_RATIO = 1080 / 1920

    width, height = clip.size
    new_height = int(width * HEIGHT_RATIO)
    screensize = (width, new_height)

    y_speed = (height - new_height) / duration
    clip: ImageClip = clip.resize(
        height=screensize[1] * 4
    ).set_duration(duration)

    clip = (CompositeVideoClip([clip])
        .resize(width=screensize[0])
        .set_position(lambda t: ("center", 1 - t * y_speed)))

    clip = CompositeVideoClip([clip], size=screensize)
    with tempfile.NamedTemporaryFile(delete=False) as temp_audio:
        file_path = temp_audio.name + ".mp4"
        clip.write_videofile(file_path, fps=24)
    return file_path
