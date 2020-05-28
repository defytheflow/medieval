class Level:

    def __init__(self, canvas, character, background):
        self.canvas = canvas
        self.character = character
        self.background = background

    def play(self):
        self.canvas.character = self.character
        self.background.draw(self.canvas)
        self.character.draw(self.canvas, 0, 0)
