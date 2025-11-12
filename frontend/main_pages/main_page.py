from customtkinter import *
from PIL import Image

from frontend.page import Page

from frontend.main_pages.select_calc import Select_Calc_Page


class Main_Page(Page):
    def __init__(self, root, *args, **kwargs):
        Page.__init__(self, root,*args, **kwargs)
        self.root=root

        def page1():
            logo_label.destroy()
            title_label.destroy()
            button_1.destroy()
            button_2.destroy()
            Select_Calc_Page(self.root)

        logo = CTkImage(Image.open("../../LOGO.png"), size=(850, 850))
        logo_label = CTkLabel(root, text="", image=logo)
        logo_label.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=20, pady=(50, 20))

        title_label = CTkLabel(master=root, text="Photo Calculator",
                               font=("Helvetica", 80, 'bold', 'underline'), text_color="#370d40")
        title_label.grid(row=0, column=1, sticky="ew", padx=(10, 30), pady=(100, 0))

        button_1 = CTkButton(master=root, text="Open an image", fg_color="#4e1d58", hover_color="#370d40",
                             text_color="#DDC3C3", font=("Helvetica", 40), corner_radius=50)
        button_1.grid(row=1, column=1, sticky="ew", padx=100, pady=(0, 200), ipady=20, ipadx=20)

        button_2 = CTkButton(master=root, text="Continue with manual input", fg_color="#4e1d58", hover_color="#370d40",
                             text_color="#DDC3C3", font=("Helvetica", 40), corner_radius=50, command = page1)
        button_2.grid(row=1, column=1, sticky="ew", padx=100, pady=(100, 50), ipady=20, ipadx=20)