import tkinter as tk
from editor import Editor


def main():
    root = tk.Tk()
    editor = Editor(root)
    editor.call_main_loop()


if __name__ == "__main__":
    main()
