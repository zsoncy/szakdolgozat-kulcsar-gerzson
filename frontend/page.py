from customtkinter import CTkFrame


class Page(CTkFrame):

    def __init__(self, root, *args, **kwargs):
        CTkFrame.__init__(self, master=root, *args, **kwargs)
        self.root=root
