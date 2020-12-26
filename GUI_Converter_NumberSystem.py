from tkinter import *
from Converter_NumberSystem import other_to_other

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(text.get(1.0, 'end-1c'))
    lab['text'] = "Successfully copied!"


def convert():
    lab['text'] = ""
    number = ent_number.ent.get()
    base_in = int(ent_base_in.ent.get())
    base_out = int(ent_base_out.ent.get())
    result = other_to_other(number, base_in, base_out)
    text.delete(1.0, END)
    text.insert(1.0, str(result))


def reset():
    lab['text'] = ""
    ent_number.ent.delete(0, END)
    ent_base_in.ent.delete(0, END)
    ent_base_out.ent.delete(0, END)
    text.delete(1.0, END)


def swap():
    base_in_num, base_out_num = ent_base_in.ent.get(), ent_base_out.ent.get()
    ent_base_in.ent.delete(0, END)
    ent_base_out.ent.delete(0, END)
    ent_base_in.ent.insert(0, base_out_num)
    ent_base_out.ent.insert(0, base_in_num)


class EnterNumber:
    def __init__(self, lab_name):
        frame = LabelFrame(text=lab_name)
        frame.pack()
        self.ent = Entry(frame)
        self.ent.pack(side=LEFT)


root = Tk()
root.title("Number System Converter")

ent_number = EnterNumber("Enter number")
ent_base_in = EnterNumber("From base")
ent_base_out = EnterNumber("To base")

frame_buttons = Frame()
frame_buttons.pack(pady=15)
Button(frame_buttons, width=10, text="Convert", command=convert).pack(side=LEFT, padx=10)
Button(frame_buttons, width=10, text="Reset", command=reset).pack(side=LEFT)
Button(frame_buttons, width=10, text="Swap", command=swap).pack(side=LEFT, padx=10)

frame_result = LabelFrame(text="Result number")
frame_result.pack()
text = Text(frame_result, width=30, height=2)
text.pack(pady=10)
frame_in_result = Frame(frame_result)
frame_in_result.pack()
lab = Label(frame_in_result, width=20)
lab.pack(side=LEFT)
Button(frame_in_result, width=10, text="Copy", command=copy_to_clipboard).pack(anchor=W, pady=5, padx=5)


root.mainloop()
