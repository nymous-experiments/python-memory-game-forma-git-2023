from tkinter import *
from tkinter.font import Font


def show_victory(old_root):
    old_root.destroy()
    victory_screen = Tk()
    victory_screen.title("Règles")
    victory_screen.geometry("+300+100")
    victory_screen.resizable(0, 0)
    victory_screen.bind("<Escape>", lambda event: exit())
    victory_screen.bind("<Button-1>", lambda event: exit())
    victory_screen.bind("<Return>", lambda event: exit())
    font = Font(victory_screen, size=25)
    text = Label(
        text="BRAVO\nVOUS AVEZ GAGNÉ",
        font=font,
        width="32",
        anchor="center",
        bg="misty rose",
    )
    text.pack(side=TOP)
    victory_screen.mainloop()
