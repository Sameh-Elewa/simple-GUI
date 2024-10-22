import tkinter as tk
from tkinter import ttk

# Example Classes
class ReverseString:
    def execute(self, s):
        return self.reverse_string(s)

    def reverse_string(self, s):
        if len(s) == 0:
            return s
        return s[-1] + self.reverse_string(s[:-1])

class Power:
    def execute(self, x, n):
        return self.power(int(x), int(n))

    def power(self, x, n):
        if n == 0:
            return 1
        return x * self.power(x, n - 1)

class GCD:
    def execute(self, a, b):
        return self.gcd(int(a), int(b))

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

# Function to Add Two Numbers
def add_two_numbers(a, b):
    return int(a) + int(b)

# GUI Setup
class ExampleSelectorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Example Selector")

        # Label and Dropdown for Example Selection
        self.label = ttk.Label(root, text="Select an Example:")
        self.label.pack(pady=10)

        self.example_var = tk.StringVar()
        self.example_combobox = ttk.Combobox(root, textvariable=self.example_var)
        self.example_combobox['values'] = ("Add Two Numbers", "Reverse String", "Power", "GCD")
        self.example_combobox.pack(pady=10)
        self.example_combobox.bind("<<ComboboxSelected>>", self.on_example_selected)

        # Input fields
        self.input_label1 = ttk.Label(root, text="Input 1:")
        self.input_label1.pack(pady=5)

        self.input_entry1 = ttk.Entry(root)
        self.input_entry1.pack(pady=5)

        self.input_label2 = ttk.Label(root, text="Input 2:")
        self.input_label2.pack(pady=5)

        self.input_entry2 = ttk.Entry(root)
        self.input_entry2.pack(pady=5)

        # Button to Execute Selected Example
        self.execute_button = ttk.Button(root, text="Execute", command=self.execute_example)
        self.execute_button.pack(pady=10)

        # Output Display
        self.output_label = ttk.Label(root, text="Output:")
        self.output_label.pack(pady=10)

        self.output_text = tk.Text(root, height=10, width=50)
        self.output_text.pack(pady=10)

    def on_example_selected(self, event):
        selected_example = self.example_var.get()

        if selected_example == "Reverse String":
            self.input_label1.config(text="Enter a string:")
            self.input_label2.config(text="(Not Used)")
            self.input_entry2.delete(0, tk.END)
            self.input_entry2.insert(0, "Not used")
            self.input_entry2.config(state='disabled')
        elif selected_example == "Power":
            self.input_label1.config(text="Base Number:")
            self.input_label2.config(text="Power Number:")
            self.input_entry2.config(state='normal')
        else:
            self.input_label1.config(text="Enter first number:")
            self.input_label2.config(text="Enter second number:")
            self.input_entry2.config(state='normal')

    def execute_example(self):
        selected_example = self.example_var.get()

        # Map selection to class or function
        example_classes = {
            "Reverse String": ReverseString,
            "Power": Power,
            "GCD": GCD,
        }

        # Clear previous output
        self.output_text.delete(1.0, tk.END)

        # Get user input
        input1 = self.input_entry1.get()
        input2 = self.input_entry2.get()

        # Execute the selected example
        if selected_example == "Add Two Numbers":
            result = add_two_numbers(input1, input2)
        else:
            example_instance = example_classes[selected_example]()
            if selected_example == "Reverse String":
                result = example_instance.execute(input1)
            else:
                result = example_instance.execute(input1, input2)

        # Handle output
        self.output_text.insert(tk.END, str(result))

if __name__ == "__main__":
    root = tk.Tk()
    gui = ExampleSelectorGUI(root)
    root.mainloop()
