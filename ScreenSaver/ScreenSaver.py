from tkinter import *
from PIL import Image, ImageTk


class ScreenSaver(object):
    def __init__(self, master):
        self.master = master
        # 隐藏窗口管理
        self.master.overrideredirect(1)
        # 透明度
        self.master.attributes('-alpha', 1)
        # 屏保图片
        self.image1 = Image.open("resource/1.jpg")
        self.image2 = Image.open("resource/2.jpg")
        self.im = ImageTk.PhotoImage(self.image2)
        self.imglabel = Label(self.master, image=self.im, borderwidth=0)
        self.imglabel.pack()
        # 事件绑定
        self.bind()
        # 启动屏保
        self.run_screen_saver(1, 1)

    def bind(self):
        self.master.bind('<Key>', self.quit)
        self.master.bind('<Motion>', self.quit)

    def run_screen_saver(self, sign, times):
        # 4次换图片 2000毫秒
        if sign % 5 == 0:
            if times == 1:
                self.im = ImageTk.PhotoImage(self.image1)
                self.imglabel.config(image=self.im)
                times = 0
            else:
                self.im = ImageTk.PhotoImage(self.image2)
                self.imglabel.config(image=self.im)
                times = 1
            sign = 1
        else:

            sign += 1
        self.master.after(500, self.run_screen_saver, sign, times)

    def quit(self, event):
        self.master.destroy()


if __name__ == "__main__":
    screen_saver = Tk()
    ScreenSaver(screen_saver)
    screen_saver.mainloop()
from tkinter import *
from PIL import Image, ImageTk


class ScreenSaver(object):
    def __init__(self, master):
        self.master = master
        # 隐藏窗口管理
        self.master.overrideredirect(1)
        # 透明度
        self.master.attributes('-alpha', 1)
        # 屏保图片
        self.image1 = Image.open("resource/1.jpg")
        self.image2 = Image.open("resource/2.jpg")
        self.im = ImageTk.PhotoImage(self.image2)
        self.imglabel = Label(self.master, image=self.im, borderwidth=0)
        self.imglabel.pack()
        # 事件绑定
        self.bind()
        # 启动屏保
        self.run_screen_saver(1, 1)

    def bind(self):
        self.master.bind('<Key>', self.quit)
        self.master.bind('<Motion>', self.quit)

    def run_screen_saver(self, sign, times):
        # 4次换图片 2000毫秒
        if sign % 5 == 0:
            if times == 1:
                self.im = ImageTk.PhotoImage(self.image1)
                self.imglabel.config(image=self.im)
                times = 0
            else:
                self.im = ImageTk.PhotoImage(self.image2)
                self.imglabel.config(image=self.im)
                times = 1
            sign = 1
        else:

            sign += 1
        self.master.after(500, self.run_screen_saver, sign, times)

    def quit(self, event):
        self.master.destroy()


if __name__ == "__main__":
    screen_saver = Tk()
    ScreenSaver(screen_saver)
    screen_saver.mainloop()
