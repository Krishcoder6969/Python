from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = Tk()
window.title("Codingals Text Editor")
window.geometry("600x500")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

def oppen_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)
        input_file.close()
    window.title(f"Codingals Text Editor - {filepath}")
def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files",)]
    )        