from tkinter.filedialog import *
from tkinter.messagebox import *
import os


class Gui(object):
    def __init__(self, master):
        self.filename = ""
        self.master = master
        # 任务栏
        self.menubar = Menu(master)
        self.master['menu'] = self.menubar
        # 文件功能
        self.filemenu = Menu(master)
        self.filemenu.add_command(label="新建", accelerator="Ctrl+N", command=self.newfile)
        self.filemenu.add_command(label="打开", accelerator="Ctrl+O", command=self.openfile)
        self.filemenu.add_command(label="保存", accelerator="Ctrl+S", command=self.savefile)
        self.filemenu.add_command(label="另存为", accelerator="Ctrl+shift+s", command=self.saveasfile)
        self.menubar.add_cascade(label="文件", menu=self.filemenu)
        # 文本区域
        self.textPad = Text(self.master, undo=True)
        self.textPad.pack(expand=YES, fill=BOTH)
        self.scroll = Scrollbar(self.textPad)
        self.textPad.config(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.textPad.yview)
        self.scroll.pack(side=RIGHT, fill=Y)
        # 热键绑定
        self.hotkey_bind()

    def hotkey_bind(self):
        # 热键绑定
        self.textPad.bind("<Control-N>", self.newfile)
        self.textPad.bind("<Control-n>", self.newfile)
        self.textPad.bind("<Control-O>", self.openfile)
        self.textPad.bind("<Control-o>", self.openfile)
        self.textPad.bind("<Control-S>", self.savefile)
        self.textPad.bind("<Control-s>", self.savefile)

    def newfile(self):
        self.master.title("未命名文件")
        self.filename = None
        self.textPad.delete(1.0, END)

    def openfile(self):
        self.filename = askopenfilename(defaultextension=".txt")
        if self.filename == "":
            self.filename = None
        else:
            self.master.title("记事本" + os.path.basename(self.filename))
            self.textPad.delete(1.0, END)
            f = open(self.filename, 'r')
            self.textPad.insert(1.0, f.read())
            f.close()

    def savefile(self):
        try:
            f = open(self.filename, 'w')
            msg = self.textPad.get(1.0, 'end')
            f.write(msg)
            f.close()
        except:
            self.saveasfile()

    def saveasfile(self):
        f = asksaveasfilename(initialfile="未命名.txt", defaultextension=".txt")
        try:
            self.filename = f
            fh = open(self.filename, 'w')
            msg = self.textPad.get(1.0, END)
            fh.write(msg)
            fh.close()
            self.master.title(os.path.basename(f))
        except:
            pass


if __name__ == '__main__':
    gui = Tk()
    # 窗口标题
    gui.title('记事本')
    # 主窗口大小
    gui.geometry("1000x600+100+50")
    # 禁止改变窗口大小
    gui.resizable(width=False, height=False)

    # 窗口添加组件
    app = Gui(gui)
    # 进入消息循环
    gui.mainloop()
