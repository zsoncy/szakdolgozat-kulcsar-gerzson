from customtkinter import *

from frontend.main_page import Main_Page


if __name__ == '__main__':
    root = CTk(fg_color="#DDC3C3")
    root.title("Photo Calculator")
    root.geometry("1600x900")
    root.minsize(1500, 800)
    root.columnconfigure(0, weight=2)
    root.columnconfigure(1, weight=1)
    root.iconbitmap("../../LOGO.ico")

    main = Main_Page(root)

    root.mainloop()






