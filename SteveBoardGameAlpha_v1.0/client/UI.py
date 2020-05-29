from tkinter import *
import tkinter.font as tkFont

class Game():

    def __init__(self):
        self.game = Tk()
        self.game.title("Steve's Board Game")
        self.fontStyle = tkFont.Font(family="Times New Roman", size=28)
        self.fontStyle1 = tkFont.Font(size=90)
        self.fontStyle2 = tkFont.Font(family="Times New Roman", size=14)
        self.game.geometry("400x400")
        self.game.configure(bg = "white")
        self.user_name = 'p1'
        self.widgets()

""" def send_message(self):
        self.canvas_chat.create_text(10, 40, text = self.user_name + ': ' + self.chat_input.get(), font = self.fontStyle2, anchor = NW)
        self.chat_input.delete(0, END) """

    def widgets(self):
    #    self.canvas_chat = Canvas(self.game, width = 300, height = 500, bg = 'gray92')
        self.canvas_chat.pack()
    #    self.input_user = StringVar()
    #    self.chat_input = Entry(self.game, text = self.input_user, borderwidth = 2, font = self.fontStyle2, bg = 'gray92', width = 27)
        self.chat_input.pack()
    #    self.enter_chat = Button(self.game, width = 8, text = '    Enter', command = self.send_message)
        self.enter_chat.pack()

    def start(self):
        self.game.mainloop()

Game().start()