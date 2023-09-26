from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT= "Courier"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.quiz.score = 0
        self.window= Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas= Canvas(width=300, height=250, bg="white")
        self.q_txt= self.canvas.create_text(150, 125, width= 280, text="", font=(FONT, 13, "bold"))
        self.canvas.grid(column=0, row= 1, columnspan=2, pady= 50)

        self.score= Label(text= f"score: {self.quiz.score}/10", font= (FONT, 10, "bold"), bg=THEME_COLOR, highlightthickness=0, fg="white")
        self.score.grid(column=1, row=0, sticky="ne")

        true= PhotoImage(file="images/true.png")
        self.true_button= Button(image=true, bg=THEME_COLOR, highlightthickness=0, bd=0, command=self.right)
        self.true_button.grid(column=0, row=2)

        false= PhotoImage(file="images/false.png")
        self.false_button= Button(image=false, bg=THEME_COLOR, highlightthickness=0, bd=0, command= self.wrong)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_txt= self.quiz.next_question()
            self.canvas.itemconfig(self.q_txt, text= q_txt)
        else:
            self.canvas.itemconfig(self.q_txt, text= f"You are reached end of quiz.", font=(FONT, 15, "bold"))
            self.true_button.config(state= "disabled")
            self.false_button.config(state= "disabled")
    
    def right(self):
        self.feedback(self.quiz.check_answer("True"))
        
    def wrong(self):
        self.feedback(self.quiz.check_answer("False"))
    
    def feedback(self, is_right):
        if is_right:
            self.canvas.config(background="green")
            self.score.config(text= f"Score: {self.quiz.score}/10")
        else:
            self.canvas.config(background="red")
        self.window.after(2000, func=self.get_next_question)
