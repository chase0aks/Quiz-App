from tkinter import *
from tkinter import messagebox as mb
from gtts import gTTS
import playsound
import time
import json


class Quiz:

    def __init__(self):
        self.q_no = 0
        self.display_title()
        self.display_question()
        self.opt_selected = IntVar()
        self.opts = self.radio_buttons()
        self.display_options()
        self.buttons()
        self.data_size = len(question)
        self.correct = 0

    def check_ans(self, q_no):
        if self.opt_selected.get() == answer[q_no]:
            return True

    def next_btn(self):
        if self.check_ans(self.q_no):
            self.correct += 1
            self.q_no += 1

        else:
            if self.q_no == 3:
                self.q_no -= 3
            elif self.q_no == 2:
                self.q_no -= 2
            elif self.q_no == 1:
                self.q_no -= 1
            elif self.q_no == 0:
                self.q_no += 0
            else:
                self.q_no -= 1

        if self.q_no == self.data_size:
            gui.destroy()
        else:
            self.clear_options()
            self.display_question()
            self.display_options()

    def clear_options(self):
        for btn in self.opts:
            btn['text'] = ""
        gui.update()

    def buttons(self):
        next_button = Button(gui,
                             text="Next",
                             command=self.next_btn,
                             width=10,
                             bg="blue",
                             fg="white",
                             font=("ariel", 16, "bold"))

        next_button.place(x=350, y=380)
        quit_button = Button(gui,
                             text="Quit",
                             command=gui.destroy,
                             width=5,
                             bg="black",
                             fg="white",
                             font=("ariel", 16, " bold"))

        quit_button.place(x=700, y=50)


    def display_options(self):
        val = 0
        self.opt_selected.set(0)
        for option in options[self.q_no]:
            self.opts[val]['text'] = option
            val += 1
            gui.update()
            qtts = gTTS(option)
            qtts.save('choices.mp3')
            playsound.playsound("choices.mp3", False)
            time.sleep(1)

    def display_question(self):
        q_no = Label(gui,
                     text=question[self.q_no],
                     width=60,
                     font=('ariel', 16, 'bold'),
                     anchor='w')

        q_no.place(x=70, y=100)
        gui.update()
        tts = gTTS(question[self.q_no])
        tts.save('question.mp3')
        playsound.playsound("question.mp3", True)

    def display_title(self):
        title = Label(gui,
                      text="GeeksforGeeks QUIZ",
                      width=50,
                      bg="green",
                      fg="white",
                      font=("ariel", 20, "bold"))
        title.place(x=0, y=2)

    def radio_buttons(self):
        q_list = []
        y_pos = 150
        while len(q_list) < 4:
            radio_btn = Radiobutton(gui,
                                    text=" ",
                                    variable=self.opt_selected,
                                    value=len(q_list) + 1,
                                    font=("ariel", 14))
            q_list.append(radio_btn)
            radio_btn.place(x=100, y=y_pos)
            y_pos += 40
        return q_list


gui = Tk()
gui.geometry("800x450")
gui.title("GeeksforGeeks Quiz")
with open('data.json') as f:
    data = json.load(f)

question = (data['question'])
options = (data['options'])
answer = (data['answer'])
quiz = Quiz()
gui.mainloop()
