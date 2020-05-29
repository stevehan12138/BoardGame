from tkinter import * 
import tkinter.font as tkFont

class Game():
    def __init__(self):
        self.user_name = 'p1'
        self.game = Tk()
        self.game.title("Steve's Board Game")
        self.fontStyle = tkFont.Font(family="Times New Roman", size=28)
        self.fontStyle1 = tkFont.Font(size=90)
        self.fontStyle2 = tkFont.Font(family="Times New Roman", size=14)
        self.game.geometry("1920x1080")
        self.game.configure(bg = "white")
        self.widgets()
        self.putWidgetsOnScreen()
        self.user_name = 'p1'
        self.message_pos = 40

    def put_user_name(self):
        self.canvas_icons.create_text(53, 45, text = str(self.input_name.get()), font = self.fontStyle2)
        self.user_name = str(self.input_name.get())
        self.input_name.delete(0, END)

    def send_message(self):
        self.canvas_chat.create_text(15, self.message_pos, text = str(self.user_name) + ': ' + str(self.chat_input.get()), font = self.fontStyle2, anchor = NW, tag = "delete")
        self.chat_input.delete(0, END)
        self.message_pos += 25
        self.clear_chat()
    
    def clear_chat(self):
        if self.message_pos > 715:
            self.canvas_chat.delete("delete")
            self.message_pos = 40
        else:
            return

    def widgets(self):
        self.canvas_icons = Canvas(self.game, width = 675, height = 100, bg = 'white', highlightbackground = 'white')
        self.icon_p1 = self.canvas_icons.create_oval(5, 5, 95, 95, width = 3, fill = 'green')
        self.icon_p2 = self.canvas_icons.create_oval(120, 5, 210, 95, width = 3, fill = 'red')
        self.icon_p3 = self.canvas_icons.create_oval(235, 5, 325, 95, width = 3, fill = 'gray92')
        self.icon_p4 = self.canvas_icons.create_oval(350, 5, 440, 95, width = 3, fill = 'gray92')
        self.icon_p5 = self.canvas_icons.create_oval(465, 5, 555, 95, width = 3, fill = 'gray92')
        self.icon_p6 = self.canvas_icons.create_oval(580, 5, 670, 95, width = 3, fill = 'gray92')
        self.enter_chat = Button(self.game, width = 8, text = '    Enter', command = self.send_message)
        self.enter_name = Button(self.game, width = 8, text = '    Enter', command = self.put_user_name)
        self.input_name = Entry(self.game, borderwidth = 2, font = self.fontStyle2, bg = 'white', width = 33)
        self.canvas_icons.create_text(53+115, 45, font = self.fontStyle)
        self.canvas_icons.create_text(53+230, 45, font = self.fontStyle)
        self.canvas_icons.create_text(53+345, 45, font = self.fontStyle)
        self.canvas_icons.create_text(53+460, 45, font = self.fontStyle)
        self.canvas_icons.create_text(53+575, 45, font = self.fontStyle)
        self.canvas_chat = Canvas(self.game, width = 300, height = 750, bg = 'gray92')
        self.canvas_chat.create_text(150, 20, text = "Game Chat", font = self.fontStyle)
        self.input_user = StringVar()
        self.user_name_label = Label(self.game, text = "Enter your user name:", font = self.fontStyle2, bg = 'white')
        self.chat_input = Entry(self.game, text = self.input_user, borderwidth = 2, font = self.fontStyle2, bg = 'gray92', width = 27)
        self.name_Label = Label(self.game, text = "Who's the spy?", font = self.fontStyle, borderwidth = 2, bg = 'white')
        self.filling_Label_1 = Label(self.game, text = "                ", font = self.fontStyle1, borderwidth = 2, bg = 'white')
        self.filling_Label_2 = Label(self.game, text = "                ", font = self.fontStyle1, borderwidth = 2, bg = 'white')
    
    def putWidgetsOnScreen(self):
        self.name_Label.grid(row = 0, column = 2, sticky = E)
        self.canvas_icons.grid(row = 1, column = 2, sticky = W)
        self.user_name_label.grid(row = 2, column = 1, sticky = W)
        self.input_name.grid(row = 3, column = 1, sticky = W, columnspan = 1)
        self.enter_name.grid(row = 3, column = 2, sticky = W, columnspan = 1)
        self.canvas_chat.grid(row = 4, column = 6, sticky = E)
        self.filling_Label_1.grid(row = 4, column = 5)
        self.chat_input.grid(row = 5, column = 6, sticky = W)
        self.enter_chat.grid(row = 5, column = 6, sticky = E)
    
    def start(self):
        self.game.mainloop()

Game().start()