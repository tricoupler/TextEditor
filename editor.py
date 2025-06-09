import tkinter as tk
from tkinter import filedialog, messagebox


class Editor:

    keybind_text = (
        "Ctrl+S = Save   |   Ctrl+O = Open   |   Ctrl+N = New File   |   "
    )
    keybind_text2 = "Ctrl+Q = Quit without Saving   |   Esc = Quit and Save"

    def __init__(self, tk_root):
        self.root = tk_root
        self.create_window()
        self.create_bottom_frame()
        self.add_text_box()
        self.add_keybinds()

    def create_window(self):
        self.root.title("YouTube Script Editor")
        self.root.attributes("-fullscreen", True)
        self.root.configure(bg="black")

    def create_bottom_frame(self):
        self.bottom_frame = tk.Frame(self.root, bg="#0C0C0C")
        self.bottom_frame.pack(fill="x", side="bottom")
        self.scroll_label = tk.Label(
            self.bottom_frame,
            text=self.keybind_text + self.keybind_text2,
            fg="#806868",
            bg="#0C0C0C",
            font=("Consolas", 12),
        )
        self.scroll_label.pack(anchor="center")

    def add_text_box(self):
        self.text_box = tk.Text(
            self.root,
            wrap="word",
            bg="black",
            fg="#806868",
            insertbackground="white",
            bd=0,
            highlightthickness=0,
            font=("Helvetica", 20),
            undo=True,
        )
        self.text_box.pack(fill="both", expand=True, padx=40, pady=(10, 0))

    def add_keybinds(self):
        self.root.bind("<Control-s>", self.save_file)
        self.root.bind("<Control-o>", self.open_file)
        self.root.bind("<Control-q>", self.quit_without_saving)
        self.root.bind("<Escape>", self.quit_and_save)
        self.root.bind("<Control-n>", self.new_file)

    def save_file(self, event=None):
        try:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt", filetypes=[("Text files", "*.txt")]
            )
            if file_path:
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(self.text_box.get("1.0", "end-1c"))

            self.show_toast("Saved file")
        except Exception:
            self.show_toast("Failed to save file")

    def open_file(self, event=None):
        try:
            file_path = filedialog.askopenfilename(
                filetypes=[("Text files", "*.txt")]
            )
            if file_path:
                with open(file_path, "r", encoding="utf-8") as file:
                    self.text_box.delete("1.0", "end")
                    self.text_box.insert("1.0", file.read())

            self.show_toast("Opened file")
        except Exception:
            self.show_toast("Failed to open file")

    def quit_without_saving(self, event=None):
        self.root.destroy()

    def quit_and_save(self, event=None):
        self.save_file()
        self.root.destroy()

    def new_file(self, event=None):
        try:
            if self.text_box.get("1.0", "end-1c").strip():
                confirm = messagebox.askyesno(
                    "New File", "Discard current text and create a new file?"
                )
                if not confirm:
                    return
            self.text_box.delete("1.0", "end")
            self.show_toast("Created new file")
        except Exception:
            self.show_toast("Failed to create new file")

    def show_toast(self, message, duration=2000):
        toast = tk.Label(
            self.root,
            text=message,
            bg="#1e1e1e",
            fg="#806868",
            font=("Consolas", 36),
            bd=10,
            relief="solid",
            padx=10,
            pady=5,
        )
        toast.place(relx=1.0, rely=1.0, anchor="se", x=-20, y=-60)
        self.root.after(duration, toast.destroy)

    def call_main_loop(self):
        self.root.mainloop()
