from customtkinter import *

from frontend.page import Page

from frontend.eq_pages.select_eq import Select_Eq_Page


class Select_Calc_Page(Page):
    def __init__(self, root, *args, **kwargs):
        Page.__init__(self, root,*args, **kwargs)
        self.root=root

        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)

        def page1():
            button_1.destroy()
            button_2.destroy()
            button_3.destroy()
            Select_Eq_Page(self.root)

        button_1 = CTkButton(master=root, text="Equation", fg_color="#4e1d58", hover_color="#370d40",
                             text_color="#DDC3C3", font=("Helvetica", 40), corner_radius=50, command = page1)
        button_1.grid(row=0, column=0, sticky="ew", padx=100, pady=400, ipady=20, ipadx=20)

        button_2 = CTkButton(master=root, text="Calculator", fg_color="#4e1d58", hover_color="#370d40",
                             text_color="#DDC3C3", font=("Helvetica", 40), corner_radius=50)
        button_2.grid(row=0, column=1, sticky="ew", padx=100, pady=400, ipady=20, ipadx=20)

        button_3 = CTkButton(master=root, text="Function graph", fg_color="#4e1d58", hover_color="#370d40",
                             text_color="#DDC3C3", font=("Helvetica", 40), corner_radius=50)
        button_3.grid(row=0, column=2, sticky="ew", padx=100, pady=400, ipady=20, ipadx=20)

