import tkinter as tk
from tkinter import *
from tkinter import messagebox
import json





#let's  create the function to import the questions in json format

def load_question_file(path):
    with open(path,'r') as b:
        question = json.load(b)
    return question


class Quiz():
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.current_question = 0
        self.root = tk.Tk()
        self.root.title("Udemy Python test")

        self.question_label = Label(self.root,text='',font=("Arial",16))
        self.question_label.pack()

        self.variable = StringVar()
        self.option1 = Radiobutton(self.root, text="", variable=self.variable, value="a")
        self.option2 = Radiobutton(self.root, text="", variable=self.variable, value="b")
        self.option3 = Radiobutton(self.root, text="", variable=self.variable, value="c")
        self.option4 = Radiobutton(self.root, text="", variable=self.variable, value="d")


        self.next_button = Button(self.root,text="Next",command=self.next_question)
        self.quit_button = Button(self.root,text="Quit",command=self.quit_quiz)

        self.option1.pack()
        self.option2.pack()
        self.option3.pack()
        self.option4.pack()
        self.next_button.pack()
        self.quit_button.pack()

        self.display_question()

    def display_question(self):
         question = self.questions[self.current_question]
         self.question_label.config(text=question["question"])
         self.option1.config(text=question["options"][0])
         self.option2.config(text=question["options"][1])
         self.option3.config(text=question["options"][2])
         self.option4.config(text=question["options"][3])


    def next_question(self):
        selected_answer = self.variable.get()
        correct_answer = self.questions[self.current_question]["answer"]
        if selected_answer==correct_answer:
            self.score+=1
        self.current_question+=1
        if self.current_question<len(self.questions):
            self.display_question()
        else:
            self.display_result()

    def display_result(self):
        messagebox.showinfo("Quiz is Over!!",f"Your final Score is: {self.score}/{len(self.questions)}")
        self.root.destroy()

    def quit_quiz(self):
        self.root.destroy()


file ="/Users/pushpakreddy/Downloads/new_proj/questions.json"
questions = load_question_file(file)
udemy_quiz=Quiz(questions)
udemy_quiz.root.mainloop()
