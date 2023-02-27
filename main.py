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
        self.opt_selected = StringVar()
        self.display_choices()
        self.buttons()
        self.choice_vars = []

        self.data_size = len(question)
        self.correct = 0

    def check_ans(self, q_no):
        if self.opt_selected.get() == answer[q_no]:
            return True

    def next_btn(self):
        if self.check_ans(self.q_no):
            self.correct += 1

        self.q_no += 1
        if self.q_no == self.data_size:
            gui.destroy()
        else:
            self.clear_options()
            self.clear_question()
            self.display_question()
            self.display_choices()

    def clear_options(self):
        for child in self.choice_frame.winfo_children():
            child.destroy()

    def clear_question(self):
        self.question_frame.destroy()

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

    def display_choices(self):
        spacer = gTTS("or")
        spacer.save("spacer.mp3")
        self.choice_frame = Frame(gui)
        self.choice_frame.place(x=100, y=self.question_frame.winfo_y(
        ) + self.question_frame.winfo_height() + 20)
        self.opt_selected.set("")
        val = 0

        header = Label(self.choice_frame,
                       text="Please Select One Option", font=("ariel", 18))
        header.pack()

        for option in options[self.q_no]:
            radio_btn = Radiobutton(self.choice_frame,
                                    text=option,
                                    variable=self.opt_selected,
                                    value=option,
                                    font=("ariel", 14))
            radio_btn.pack(side="top", anchor="w")
            gui.update()
            qtts = gTTS(option)
            qtts.save('choices.mp3')
            playsound.playsound("choices.mp3", True)
            if val != len(options[self.q_no]) - 1:
                playsound.playsound("spacer.mp3", True)
                val += 1

    def display_question(self):
        self.question_frame = Frame(gui)
        self.question_frame.place(x=70, y=50)
        q_no = Label(self.question_frame,
                     text=question[self.q_no],
                     width=60,
                     font=('ariel', 16, 'bold'),
                     anchor='center',
                     wraplength=700,
                     pady=20)
        q_no.pack(side='top', fill='both', expand=True)
        gui.update()
        tts = gTTS(question[self.q_no])
        tts.save('question.mp3')
        playsound.playsound("question.mp3", True)

    def display_title(self):
        title = Label(gui,
                      text="English 2600",
                      width=50,
                      bg="green",
                      fg="white",
                      font=("ariel", 20, "bold"),
                      padx=10,
                      pady=10,
                      anchor='center')
        title.pack()

    def run(self):
        self.display_question()
        self.display_choices()


gui = Tk()
gui.geometry("800x450")
gui.title("English 2600")
with open('data.json') as f:
    data = json.load(f)

question = (data['question'])
options = (data['options'])
answer = (data['answer'])
quiz = Quiz()
gui.mainloop()
