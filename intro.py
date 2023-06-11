"""
File: Final.py
----------------
"""

from tkinter import *


def choose_mode():
    chosen_mode = []
    intro_root = Tk()
    intro_root.title("Règles")
    intro_root.geometry("+300+100")
    intro_root.resizable(0, 0)
    intro_root.bind("<Escape>", lambda event: exit())
    # TODO: Finir de traduire les règles
    rules = Label(
        text="""
1. Cliquer sur deux cartes pour les retourner.
2. Si les deux cartes sont identiques, elle resteront face visibles.
3. Sinon elles seront masquées.
4. Le jeu se termine lorsque toutes les cartes sont visibles.
5. A new game starts automatically.
6. Press ENTER to change mode.
7. Press ESCAPE to exit.
        """,
        width="60",
        bg="misty rose",
    )
    rules.pack(side=TOP)
    colored_mode = Button(
        text="MODE COLORÉ",
        width="29",
        height="5",
        bg="rosy brown",
        command=lambda mode=1, route="images/CodeInPlace/pic": clicked(
            mode, route, intro_root, chosen_mode
        ),
    )
    colored_mode.pack(side=LEFT)
    colorblind_mode = Button(
        text="MODE DALTONIEN",
        width="29",
        height="5",
        bg="rosy brown",
        command=lambda mode=2, route="images/RustyLake/pic": clicked(
            mode, route, intro_root, chosen_mode
        ),
    )
    colorblind_mode.pack(side=LEFT)
    intro_root.mainloop()
    return chosen_mode


def clicked(first_value, second_value, root, info_list):
    info_list.append(first_value)
    info_list.append(second_value)
    root.destroy()


def choose_level():
    chosen_level = []
    level_root = Tk()
    level_root.title("Niveau")
    level_root.geometry("+200+100")
    level_root.resizable(0, 0)
    level_root.bind("<Escape>", lambda event: exit())
    lvl0 = Button(
        text="TRÈS FACILE",
        width="15",
        height="5",
        bg="alice blue",
        command=lambda rows=2, cols=2: clicked(rows, cols, level_root, chosen_level),
    )
    lvl0.pack(side=LEFT)
    lvl1 = Button(
        text="FACILE",
        width="15",
        height="5",
        bg="alice blue",
        command=lambda rows=3, cols=4: clicked(rows, cols, level_root, chosen_level),
    )
    lvl1.pack(side=LEFT)
    lvl2 = Button(
        text="MOYEN",
        width="15",
        height="5",
        bg="lavender blush",
        command=lambda rows=4, cols=6: clicked(rows, cols, level_root, chosen_level),
    )
    lvl2.pack(side=LEFT)
    # TODO: Ajouter un mode très difficile
    # lvl3 = Button(
    #     text="DIFFICILE",
    #     width="15",
    #     height="5",
    #     bg="lavender",
    #     command=lambda rows=5, cols=8: clicked(rows, cols, level_root, chosen_level),
    # )
    # lvl3.pack(side=LEFT)
    level_root.mainloop()
    return chosen_level
