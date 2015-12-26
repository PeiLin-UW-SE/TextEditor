from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
import os


class Menus:
    def __init__(self, master):
        self.master = master
        self.file_operator_obj = FileOperators()
        self.text_appear_obj = TextAppearance()

        main_menu = Menu(master)
        master.config(menu=main_menu)

        file_menu = Menu(main_menu, tearoff=FALSE)
        main_menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.file_operator_obj.new_file)
        file_menu.add_command(label="Open", command=self.file_operator_obj.open_file)
        file_menu.add_command(label="Save", command=self.file_operator_obj.save_file)
        file_menu.add_command(label="Save As...", command=self.file_operator_obj.save_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=master.destroy)

        appear_menu = Menu(main_menu, tearoff=FALSE)
        main_menu.add_cascade(label="Appearance", menu=appear_menu)
        appear_menu.add_command(label="Bold", command=self.text_appear_obj.bold)
        appear_menu.add_command(label="Italic", command=self.text_appear_obj.italic)
        appear_menu.add_command(label="Underline", command=self.text_appear_obj.underline)
        appear_menu.add_command(label="Highlight", command=self.text_appear_obj.highlight)
        appear_menu.add_separator()
        appear_menu.add_command(label="Clear", command=self.text_appear_obj.clear)

        about_menu = Menu(main_menu, tearoff=FALSE)
        main_menu.add_cascade(label="About", menu=about_menu)
        about_menu.add_command(label="Info", command=self.file_operator_obj.about_window)


class Buttons:
    def __init__(self, master):
        self.master = master
        self.file_operator_obj = FileOperators()
        self.text_appear_obj = TextAppearance()

        btn_frame = Frame(master)
        btn_frame.pack()
        new_btn = Button(btn_frame, text="New", command=self.file_operator_obj.new_file)
        new_btn.pack(side=LEFT, padx=2)
        save_btn = Button(btn_frame, text="Save", command=self.file_operator_obj.save_file)
        save_btn.pack(side=LEFT, padx=2)
        bold_btn = Button(btn_frame, text="Bold", command=self.text_appear_obj.bold)
        bold_btn.pack(side=LEFT, padx=2)
        italic_btn = Button(btn_frame, text="Italic", command=self.text_appear_obj.italic)
        italic_btn.pack(side=LEFT, padx=2)
        quit_btn = Button(btn_frame, text="Quit", command=master.destroy)
        quit_btn.pack(side=LEFT, padx=2)


class FileOperators:
    def __init__(self):
        self.filename = None

    def new_file(self):
        self.filename = "Untitled"
        text.delete(0.0, END)

    def open_file(self):
        f = tkinter.filedialog.askopenfile(mode="r")
        try:
            t = f.read()
            text.delete(0.0, END)
            text.insert(0.0, t)
        except AttributeError:
            pass
        global x
        x = os.path.split(f.name)[1]

    def save_file(self):
        global x
        try:
            t = text.get(0.0, END)
            f = open(x, "w")
            f.write(t)
            f.close()
        except NameError:
            pass

    def save_as(self):
        try:
            f = tkinter.filedialog.asksaveasfile(mode="w", defaultextension=".txt")
            t = text.get(0.0, END)
            f.write(t.rstrip())
        except AttributeError:
            pass

    def about_window(self):
        tkinter.messagebox.showinfo("About", "Created by Pei Lin Li \n 2015")


class TextAppearance:
    def bold(self):
        text.tag_config("bt", font=("Georgia", "12", "bold"))
        try:
            text.tag_add("bt", "sel.first", "sel.last")
        except TclError:
            pass

    def italic(self):
        text.tag_config("it", font=("Georgia", "12", "italic"))
        try:
            text.tag_add("it", "sel.first", "sel.last")
        except TclError:
            pass

    def underline(self):
        text.tag_config("ut", font=("Georgia", "12", "underline"))
        try:
            text.tag_add("ut", "sel.first", "sel.last")
        except TclError:
            pass

    def highlight(self):
        text.tag_config("ht", font=("Georgia,", "12"), background="yellow")
        try:
            text.tag_add("ht", "sel.first", "sel.last")
        except TclError:
            pass

    def clear(self):
        try:
            text.tag_remove("bt", "sel.first", "sel.last")
            text.tag_remove("it", "sel.first", "sel.last")
            text.tag_remove("ut", "sel.first", "sel.last")
            text.tag_remove("ht", "sel.first", "sel.last")
        except TclError:
            pass

root = Tk()

root.title("Python Tkinter Text Editor")
root.minsize(width=450, height=580)
root.maxsize(width=450, height=580)
name = Label(root, text="Python Tkinter Text Editor v3.0", bd=2, anchor=N, font=24, relief=GROOVE)
name.pack(side=TOP, fill=X)

run_1 = Menus(root)
run_2 = Buttons(root)

text = Text(root, font=("Georgia,", "12"), width=55, height=32, relief=SUNKEN)
text.pack()

root.mainloop()
