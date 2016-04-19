from tkinter import *
from tkinter import filedialog

__author__ = 'Rui Zheng'


class OpenFile(object):
    def __init__(self, root=None, file=None):
        self.root = Tk()
        self.root.fileName = filedialog.askopenfilename \
            (filetypes=[("Target file", "txt"),
                        ("All files", "*.*")])
        self.file = open(self.root.fileName, "r")
        self.root.mainloop()

    def ReadData(self):
        record = []
        personal = []
        for line in self.file:
            record.append(line)
            x = line.split(" ")
            personal.append(x)
        return personal
        self.file.close()


class LocalData(object):
    openfile = OpenFile()
    local_data = openfile.ReadData()
