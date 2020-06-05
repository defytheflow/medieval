from PIL import Image, ImageTk
import simpleaudio as sa


def create_photo_image(path, size=None):
    image = Image.open(path)
    if size:
        image = image.resize(size)
    return ImageTk.PhotoImage(image)


def play_sound(sound_file):
    wave_obj = sa.WaveObject.from_wave_file(sound_file)
    wave_obj.play()
