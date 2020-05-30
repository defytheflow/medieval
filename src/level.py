import tkinter as tk

from sprites import Character
from backgrounds import Background

class Level:

    def __init__(self,
                 canvas: tk.Canvas,
                 character: Character,
                 background: Background):

        self.canvas = canvas
        self.character = character
        self.background = background

    def play(self):
        self.canvas.character = self.character
        self.background.draw(self.canvas)
        self.character.draw(self.canvas, 0, 0)
