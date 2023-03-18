import tkinter as tk
THEME_COLOR = "#375362"

class TriviaGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Trivia Game")
        self.config(pady=20, padx=20, bg=THEME_COLOR)

        self.img_false_btn = tk.PhotoImage(file="./images/false.png")
        self.img_true_btn = tk.PhotoImage(file="./images/true.png")

        self._make_button()
        self._make_canvas()
        self._make_label()
        self.mainloop()

    def _make_button(self):
        self.btn_false = tk.Button(image=self.img_false_btn, highlightthickness=0)
        self.btn_false.grid(row=2, column=1, padx=20, pady=20)

        self.btn_true = tk.Button(image=self.img_true_btn, highlightthickness=0)
        self.btn_true.grid(row=2, column=0, padx=20, pady=20)

    def _make_canvas(self):
        self.canvas = tk.Canvas(width=300, height=250)
        self.canvas.config(bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="fasdfasf", font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

    def _make_label(self):
        self.score_label = tk.Label(text="Score: 0", bg=THEME_COLOR, highlightthickness=0, font=("Arial", 12), fg="white")
        self.score_label.grid(row=0, column=1, padx=20, pady=20)

