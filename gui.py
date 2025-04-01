import tkinter as tk
from tkinter import messagebox
from parser import check_grammar

# --- FUNCTION TO HANDLE BUTTON CLICK ---
def on_check_button_click():
    sentence = entry.get()
    if sentence.lower() == "exit":
        window.quit()
    else:
        result = check_grammar(sentence)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, result)

# --- SET UP TKINTER WINDOW ---
window = tk.Tk()
window.title("Grammar Checker")

# Entry Label
label = tk.Label(window, text="Enter a sentence:")
label.pack(padx=10, pady=5)

# Sentence Input Field
entry = tk.Entry(window, width=50)
entry.pack(padx=10, pady=5)

# Check Button
check_button = tk.Button(window, text="Check Grammar", command=on_check_button_click)
check_button.pack(padx=10, pady=10)

# Result Text Box
result_text = tk.Text(window, height=15, width=60)
result_text.pack(padx=10, pady=10)

# Start the Tkinter event loop
window.mainloop()
