import tkinter.ttk as ttk

'''
Wrapper for ttk.Button which repeatinterval and repeatdelay options.
Taken from https://stackoverflow.com/a/29824277
'''


class RepeatButton(ttk.Button):
    def __init__(self, *args, **kwargs):

        self.callback = kwargs.pop('command', None)
        self.repeatinterval = kwargs.pop('repeatinterval', 100)
        self.repeatdelay = kwargs.pop('repeatdelay', 300)

        ttk.Button.__init__(self, *args, **kwargs)

        if self.callback:
            self.bind('<ButtonPress-1>', self.click)
            self.bind('<ButtonRelease-1>', self.release)

    def click(self, event=None):
        self.callback()
        self.after_id = self.after(self.repeatdelay, self.repeat)

    def repeat(self):
        self.callback()
        self.after_id = self.after(self.repeatinterval, self.repeat)

    def release(self, event=None):
        self.after_cancel(self.after_id)
