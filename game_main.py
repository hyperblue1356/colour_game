# the player will see different names of colors with a different
# text color on the screen, the player should enter the text color
# of the word which is displayed on the screen not the word on the screen.
#If the player enters the correct color then the score will be incremented
# by one. When the wrong answer is given no increment in the score. The game
# duration will be 60 seconds or you can define any time limit as you wish.

#When the player starts the game, the count down should begin from 60 to 0
# and a color name with a different text color should be displayed on the
# screen. Every time when the player submits an answer a different word
# should be displayed simultaneously score should be increased by one
# if the player gives a correct answer.

try:
    import tkinter
except ImportError: # python 2
    import Tkinter as tkinter

mainWindow = tkinter.Tk()

import random


mainWindowPadding = 8

mainWindow.title("Colour game")
mainWindow.geometry("640x480")
mainWindow['padx'] = mainWindowPadding

colours = ["black", "blue", "red", "orange", "yellow"]

chosen_colour = random.choice(colours)




keys = [[(chosen_colour, 1)],
        [("two", 1)]]

button_1 = tkinter.Frame(mainWindow)
button_1.grid(row=1, column=0, sticky='w,e')

row = 0
for keyRow in keys:
    col = 0
    for key in keyRow:
        tkinter.Button(button_1, text=key[0]).grid(row=row, column=col, columnspan=key[1], sticky=tkinter.E + tkinter.W+tkinter.N)
        col += key[1]
    row += 1

result = tkinter.Entry(mainWindow)
result.grid(row=2, column=2, sticky='ne')

mainWindow.update()
mainWindow.minsize(button_1.winfo_width() + mainWindowPadding, button_1.winfo_height())
mainWindow.maxsize(button_1.winfo_width() + mainWindowPadding, button_1.winfo_height())


mainWindow.mainloop()

colours = ["black", "blue", "red", "orange", "yellow"]

