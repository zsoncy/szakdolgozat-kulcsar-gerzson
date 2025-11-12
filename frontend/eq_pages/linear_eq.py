from customtkinter import *

from backend.math_calc.equation.linear_equation import Linear_equation
from frontend.page import Page

class Linear_Eq_Page(Page):
    def __init__(self, root, *args, **kwargs):
        Page.__init__(self, root, *args, **kwargs)
        self.root = root

        def calc():
            label_result.configure(text="Calculating . . .")
            a = entry_a.get()
            b = entry_b.get()
            if (a.isdigit() and int(a) != 0) and (b.isdigit() and int(b) != 0):
                current_eq = Linear_equation((int(a), int(b)))
                result= current_eq.solve()
                label_result.configure(text="X = " + str(result))
            else:
                label_result.configure(text="Wrong parameters!")

        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)
        root.columnconfigure(2, weight=1)
        root.columnconfigure(3, weight=1)

        entry_a = CTkEntry(root, placeholder_text="a",  state="normal",
                           height=50, width=100, font=("Helvetica", 80),
                           text_color="#DDC3C3", fg_color="#4e1d58")
        entry_a.grid(row=0, column=0, sticky="ew", padx=(100,0), pady=200)

        label_1 = CTkLabel(root, text="x  +", height=50, width=100, font=("Helvetica", 80),
                           corner_radius=7, text_color="#DDC3C3", fg_color="#4e1d58")
        label_1.grid(row=0, column=1, sticky="ew", pady=200, ipadx=50, ipady=5)

        entry_b = CTkEntry(root,  placeholder_text="b",  state="normal",
                           height=50, width=100, font=("Helvetica", 80),
                           text_color="#DDC3C3", fg_color="#4e1d58")
        entry_b.grid(row=0, column=2, sticky="ew", pady=200)

        label_2 = CTkLabel(root, text="= 0", height=50, width=50, font=("Helvetica", 80),
                           corner_radius=7, text_color="#DDC3C3", fg_color="#4e1d58")
        label_2.grid(row=0, column=3, sticky="ew", padx=(0,100), pady=200, ipadx=50, ipady=5)

        label_result = CTkLabel(root, text=" X = ", height=200, width=100, font=("Helvetica", 100),
                                corner_radius=50, text_color="#370d40", fg_color="orange")
        label_result.grid(row=1, column=0, columnspan=3, sticky="ew", padx=(110,10),  ipadx=50, ipady=5)

        button_calc = CTkButton(master=root, text="Calculate", height=200, width=100, fg_color="orange",
                                text_color="#370d40", font=("Helvetica", 40), corner_radius=50, command=calc)
        button_calc.grid(row=1, column=3, sticky="ew", padx=(10,110),  ipadx=50, ipady=5)


        """Button hover effect, for it to change the font color as well"""
        button_calc.bind("<Enter>", lambda event: button_calc.configure(fg_color="#4e1d58", text_color="orange"))
        button_calc.bind("<Leave>", lambda event: button_calc.configure(fg_color="orange", text_color="#370d40"))