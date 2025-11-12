from customtkinter import *

from backend.math_calc.operation.operation import iscorrectoperation, Operation
from frontend.page import Page

class Operation_Page(Page):
    def __init__(self, root, *args, **kwargs):
        Page.__init__(self, root, *args, **kwargs)
        self.root = root

        def calc():
            label_result.configure(text="Calculating . . .")
            op = entry.get()
            if iscorrectoperation(op):
                current_op = Operation(op)
                label_result.configure(text=current_op.solve())
            else:
                label_result.configure(text="Wrong input!")

        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)


        entry = CTkEntry(root, placeholder_text="Enter the operation line here...",  state="normal",
                           height=50, width=100, font=("Helvetica", 80),
                           text_color="#DDC3C3", fg_color="#4e1d58")
        entry.grid(row=0, column=0, columnspan=2, sticky="ew", padx=100, pady=200, ipadx=50, ipady=50)


        label_result = CTkLabel(root, text=" . . . ", height=200, width=100, font=("Helvetica", 100),
                                corner_radius=50, text_color="#370d40", fg_color="orange")
        label_result.grid(row=1, column=0, sticky="ew", padx=(110,10),  ipadx=50, ipady=5)

        button_calc = CTkButton(master=root, text="Calculate", height=200, width=100, fg_color="orange",
                                text_color="#370d40", font=("Helvetica", 40), corner_radius=50, command=calc)
        button_calc.grid(row=1, column=1, sticky="ew", padx=(10,110),  ipadx=50, ipady=5)


        """Button hover effect, for it to change the font color as well"""
        button_calc.bind("<Enter>", lambda event: button_calc.configure(fg_color="#4e1d58", text_color="orange"))
        button_calc.bind("<Leave>", lambda event: button_calc.configure(fg_color="orange", text_color="#370d40"))