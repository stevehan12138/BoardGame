from tkinter import *
import tkinter.font as tkFont

game = Tk()

game.title("Steve's Board Game")
fontStyle = tkFont.Font(family="Times New Roman", size=28)
fontStyle1 = tkFont.Font(size=90)
fontStyle2 = tkFont.Font(family="Times New Roman", size=14)
game.geometry("1920x1080")
game.configure(bg = "white")

# actually I think comments are kinda useful u kno

# Declaring a widget

canvas = Canvas(game, width = 800, height = 100)
input_user = StringVar()
input_field = Entry(game, text =input_user, borderwidth = 2, font = fontStyle2, bg = 'light gray', width = 80)
input_field.bind("<Return>", Enter_pressed)
name_Label = Label(game, text = "                                                                                Who's the spy?", font = fontStyle, borderwidth = 2, bg = 'white') #(put name of the game)
filling_label_1 = Label(game, text = " ", font = fontStyle1, bg = 'white')
filling_label_2 = Label(game, text = " ", font = fontStyle1, bg = 'white')
filling_label_3 = Label(game, text = " ", font = fontStyle1, bg = 'white')

# Putting the widget up on the screen

name_Label.grid(row = 0, column = 0)
filling_label_1.grid(row = 1, column = 0)
filling_label_2.grid(row = 2, column = 0)
filling_label_3.grid(row = 3, column = 0)
canvas.grid(row = 4, column = 1)
input_field.grid(row = 5, column = 1)





# Draw Loop
game.mainloop()









