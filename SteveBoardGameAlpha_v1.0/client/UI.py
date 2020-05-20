from tkinter import *
import tkinter.font as tkFont

game = Tk()

game.title("Steve's Board Game")
fontStyle = tkFont.Font(family="Times New Roman", size=28)
game.geometry("1920x1080")
game.configure(bg = "white")

# actually I think comments are kinda useful u kno

# Declaring a widget

chat = Entry(game, width = 18, borderwidth = 3, font = fontStyle)
canvas = Canvas(game, width = 350, height = 600, bg = 'white')
canvas.create_rectangle(0, 0, 350, 600, fill = 'light gray')
fill_Label_1 = Label(game, text = "                                                                               ", font = fontStyle, bg = 'white')
name_Label = Label(game, text = "Hello World", font = fontStyle, bg = 'white') #(put name of the game)
fill_Label_2 = Label(game, text = "                                                                                                ", font = fontStyle, bg = 'white')
fill_Label_3 = Label(game, text = "", font = fontStyle, bg = 'white')
fill_Label_4 = Label(game, text = "", font = fontStyle, bg = 'white')
fill_Label_5 = Label(game, text = "", font = fontStyle, bg = 'white')
fill_Label_6 = Label(game, text = "", font = fontStyle, bg = 'white')
fill_Label_7 = Label(game, text = "", font = fontStyle, bg = 'white')
fill_Label_14 = Label(game, text = "                                                                                                ", font = fontStyle, bg = 'white')
fill_Label_15 = Label(game, text = "                                             ", font = fontStyle, bg = 'white')
fill_Label_16 = Label(game, text = "                                                                                                ", font = fontStyle, bg = 'white')
fill_Label_17 = Label(game, text = "                                             ", font = fontStyle, bg = 'white')




# Putting the widget up on the screen


fill_Label_1.grid(row = 0, column = 0)
name_Label.grid(row = 0, column = 1)
fill_Label_2.grid(row = 0, column = 2)
fill_Label_3.grid(row = 1, column = 0)
fill_Label_4.grid(row = 2, column = 0)
fill_Label_5.grid(row = 3, column = 0)
fill_Label_6.grid(row = 4, column = 0)
fill_Label_7.grid(row = 5, column = 0)
fill_Label_14.grid(row = 6, column = 0)
fill_Label_15.grid(row = 6, column = 1)
canvas.grid(row = 6, column = 2)
fill_Label_16.grid(row = 7, column = 0)
fill_Label_17.grid(row = 7, column = 1)
chat.grid(row = 7, column = 2)




# Draw Loop

game.mainloop()