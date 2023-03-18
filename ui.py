import tkinter as tk
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class TriviaGUI(tk.Tk):
    def __init__(self, quiz_brain: QuizBrain):
        super().__init__()
        self.quiz = quiz_brain
        self.title("Trivia Game")
        self.config(pady=20, padx=20, bg=THEME_COLOR)

        self.img_false_btn = tk.PhotoImage(file="./images/false.png")
        self.img_true_btn = tk.PhotoImage(file="./images/true.png")

        self._make_button()
        self._make_canvas()
        self._make_label()
        self.get_next_question()
        self.mainloop()

    def _make_button(self):
        self.btn_false = tk.Button(image=self.img_false_btn, highlightthickness=0, command=self.click_btn_false)
        self.btn_false.grid(row=2, column=1, padx=20, pady=20)

        self.btn_true = tk.Button(image=self.img_true_btn, highlightthickness=0, command=self.click_btn_true)
        self.btn_true.grid(row=2, column=0, padx=20, pady=20)

    def _make_canvas(self):
        self.canvas = tk.Canvas(width=300, height=250)
        self.canvas.config(bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="fasdfasf", font=("Arial", 15, "italic"), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

    def _make_label(self):
        self.score_label = tk.Label(text="Score: 0", bg=THEME_COLOR, highlightthickness=0, font=("Arial", 10), fg="white")
        self.score_label.grid(row=0, column=1, padx=20, pady=20)

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="No more questions")
            self.btn_true.config(state="disabled")
            self.btn_false.config(state="disabled")

    def click_btn_true(self):
        is_correct = self.quiz.check_answer("True")
        self.display_feedback(is_correct)

    def click_btn_false(self):
        is_correct = self.quiz.check_answer("False")
        self.display_feedback(is_correct)

    def display_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.after(1000, self.get_next_question)