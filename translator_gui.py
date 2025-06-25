import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

translator = Translator()

def get_lang_code(lang_name):
    for code, name in LANGUAGES.items():
        if name.lower() == lang_name.lower():
            return code
    return "en"

def translate_text():
    text = input_text.get("1.0", "end").strip()
    src_lang = src_lang_var.get()
    dest_lang = dest_lang_var.get()
    
    if not text:
        messagebox.showwarning("Empty Input", "Please enter text to translate.")
        return
    
    try:
        translated = translator.translate(
            text,
            src=get_lang_code(src_lang),
            dest=get_lang_code(dest_lang)
        )
        output_text.delete("1.0", "end")
        output_text.insert("end", translated.text)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

def clear_fields():
    input_text.delete("1.0", "end")
    output_text.delete("1.0", "end")

root = tk.Tk()
root.title("🌐 Advanced AI Translator")
root.geometry("800x500")
root.configure(bg="#e6f0ff")

style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=6)
style.configure("TLabel", font=("Arial", 12))
style.configure("TCombobox", font=("Arial", 11))

title = tk.Label(root, text="AI Translator", font=("Arial", 24, "bold"), bg="#e6f0ff", fg="#003366")
title.pack(pady=15)

lang_frame = tk.Frame(root, bg="#e6f0ff")
lang_frame.pack(pady=5)

src_lang_var = tk.StringVar(value="english")
dest_lang_var = tk.StringVar(value="hindi")

ttk.Label(lang_frame, text="From:").grid(row=0, column=0, padx=10)
src_lang_menu = ttk.Combobox(lang_frame, textvariable=src_lang_var, values=sorted(LANGUAGES.values()), width=25, state="readonly")
src_lang_menu.grid(row=0, column=1, padx=10)

ttk.Label(lang_frame, text="To:").grid(row=0, column=2, padx=10)
dest_lang_menu = ttk.Combobox(lang_frame, textvariable=dest_lang_var, values=sorted(LANGUAGES.values()), width=25, state="readonly")
dest_lang_menu.grid(row=0, column=3, padx=10)

input_frame = tk.Frame(root, bg="#e6f0ff")
input_frame.pack(pady=10, fill="x", padx=20)

tk.Label(input_frame, text="Enter Text:", font=("Arial", 13, "bold"), bg="#e6f0ff").pack(anchor="w")
input_text = tk.Text(input_frame, height=6, font=("Arial", 12), wrap="word")
input_text.pack(fill="x", pady=5)

btn_frame = tk.Frame(root, bg="#e6f0ff")
btn_frame.pack(pady=10)

translate_button = ttk.Button(btn_frame, text="🔁 Translate", command=translate_text)
translate_button.grid(row=0, column=0, padx=10)

clear_button = ttk.Button(btn_frame, text="🗑 Clear", command=clear_fields)
clear_button.grid(row=0, column=1, padx=10)

output_frame = tk.Frame(root, bg="#e6f0ff")
output_frame.pack(pady=10, fill="x", padx=20)

tk.Label(output_frame, text="Translated Text:", font=("Arial", 13, "bold"), bg="#e6f0ff").pack(anchor="w")
output_text = tk.Text(output_frame, height=6, font=("Arial", 12), bg="#f7f7f7", wrap="word")
output_text.pack(fill="x", pady=5)

root.mainloop()
