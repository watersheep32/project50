from tkinter import *

class Reentry(Entry):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.bind('<Control-BackSpace>', self.entry_ctrl_bs)
    def entry_ctrl_bs(self, event):
        end_idx = self.index(INSERT)
        start_idx = self.get().rfind(" ", None, end_idx)
        self.selection_range(start_idx, end_idx)