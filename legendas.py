import tkinter as tk

class ModernCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry("400x600")
        self.configure(bg="#1e1e1e")
        
        self.result_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Área de display
        display_frame = tk.Frame(self, bg="#2e2e2e")
        display_frame.pack(expand=True, fill="both")

        self.display = tk.Entry(display_frame, textvariable=self.result_var, font=("Helvetica", 24), bd=0, bg="#3e3e3e", fg="#ffffff", justify="right")
        self.display.pack(expand=True, fill="both", ipadx=10)

        # Layout dos botões
        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+')
        ]

        button_frame = tk.Frame(self)
        button_frame.pack(expand=True, fill="both")

        for row_index, row in enumerate(buttons):
            for col_index, button_text in enumerate(row):
                button = tk.Button(button_frame, text=button_text, font=("Helvetica", 18), bg="#4e4e4e", fg="#ffffff", relief="flat", padx=20, pady=20, command=lambda text=button_text: self.on_button_click(text))
                button.grid(row=row_index, column=col_index, sticky="nsew")

        for i in range(4):
            button_frame.columnconfigure(i, weight=1)
            button_frame.rowconfigure(i, weight=1)

    def on_button_click(self, text):
        if text == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif text == 'C':
            self.result_var.set("")
        else:
            current_text = self.result_var.get()
            new_text = current_text + text
            self.result_var.set(new_text)

if __name__ == "__main__":
    app = ModernCalculator()
    app.mainloop()
