import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        
        if operation.get() == "Addition":
            result = num1 + num2
        elif operation.get() == "Subtraction":
            result = num1 - num2
        elif operation.get() == "Multiplication":
            result = num1 * num2
        elif operation.get() == "Division":
            result = num1 / num2
            
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Invalid input!")


root = tk.Tk()
root.title("Simple Calculator")

entry1 = tk.Entry(root)
entry1.pack(pady=10)

entry2 = tk.Entry(root)
entry2.pack(pady=10)


operations = ["Addition", "Subtraction", "Multiplication", "Division"]
operation = tk.StringVar(root)
operation.set(operations[0])  #

dropdown = tk.OptionMenu(root, operation, *operations)
dropdown.pack(pady=10)

calculate_btn = tk.Button(root, text="Calculate", command=calculate)
calculate_btn.pack(pady=10)

result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=10)

root.mainloop()
