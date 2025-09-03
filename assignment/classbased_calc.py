import tkinter as tk

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, value):
        self.result += value
        return self.result

    def subtract(self, value):
        self.result -= value
        return self.result

    def multiply(self, value):
        self.result *= value
        return self.result

    def divide(self, value):
        if value != 0:
            self.result /= value
            return self.result
        else:
            return "Error: Division by zero"

    def reset(self):
        self.result = 0
        return self.result

# GUI Setup
def run_calculator():
    calc = Calculator()

    def perform_operation(op):
        try:
            value = float(entry.get())
            if op == "add":
                result = calc.add(value)
            elif op == "subtract":
                result = calc.subtract(value)
            elif op == "multiply":
                result = calc.multiply(value)
            elif op == "divide":
                result = calc.divide(value)
            result_label.config(text=f"Result: {result}")
        except ValueError:
            result_label.config(text="Please enter a valid number.")

    def reset_calc():
        result = calc.reset()
        result_label.config(text=f"Result: {result}")
        entry.delete(0, tk.END)

    # Create window
    window = tk.Tk()
    window.title("Interactive Calculator")

    # Input field
    entry = tk.Entry(window, width=20)
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    # Buttons
    tk.Button(window, text="Add", command=lambda: perform_operation("add")).grid(row=1, column=0)
    tk.Button(window, text="Subtract", command=lambda: perform_operation("subtract")).grid(row=1, column=1)
    tk.Button(window, text="Multiply", command=lambda: perform_operation("multiply")).grid(row=1, column=2)
    tk.Button(window, text="Divide", command=lambda: perform_operation("divide")).grid(row=1, column=3)
    tk.Button(window, text="Reset", command=reset_calc).grid(row=2, column=0, columnspan=4, pady=10)

    # Result display
    result_label = tk.Label(window, text="Result: 0", font=("Arial", 14))
    result_label.grid(row=3, column=0, columnspan=4)

    window.mainloop()

# Run the GUI
run_calculator()

