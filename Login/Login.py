import tkinter
from tkinter import messagebox

# 全部用户
all_user = [{'account': 'admin', 'passwd': 'admin'}]


class LoginGui(object):
    def __init__(self, master):
        self.master = master
        # 全界面
        self.maxFrame = tkinter.Frame()
        self.maxFrame.pack(fill=tkinter.BOTH, expand=1, padx=10, pady=15)
        self.inputFrame = tkinter.Frame(self.maxFrame, pady=10)
        self.inputFrame.pack()
        tkinter.Label(self.inputFrame, text='用户名：', font=18).grid(row=0, column=0, sticky='W', pady=5)
        tkinter.Label(self.inputFrame, text='密码：', font=18).grid(row=1, column=0, sticky='W', pady=5)
        self.inputAccount = tkinter.Entry(self.inputFrame, justify=tkinter.CENTER)
        self.inputAccount.grid(row=0, column=1, pady=10)
        self.inputPasswd = tkinter.Entry(self.inputFrame, justify=tkinter.CENTER)
        self.inputPasswd.grid(row=1, column=1, pady=10)
        self.inputPasswd['show'] = '*'
        self.loginBtn = tkinter.Button(self.inputFrame, text='登录', font=10, padx=10)
        self.loginBtn.grid(row=2, column=0, pady=10, columnspan=2)
        self.RegBtn = tkinter.Button(self.inputFrame, text='注册', font=10, padx=10)
        self.RegBtn.grid(row=3, column=0, pady=10, columnspan=2)
        # 按钮功能绑定
        self.event_bound()

    def event_bound(self):
        self.loginBtn.bind('<ButtonRelease-1>', self.login_event)
        self.RegBtn.bind('<ButtonRelease-1>', self.reg_event)

    def login_event(self, event):
        login(account=self.inputAccount.get(), passwd=self.inputPasswd.get())

    def reg_event(self, event):
        goto_register(self.master)


class RegisterGui(object):
    def __init__(self, master):
        self.master = master
        # 全界面
        self.maxFrame = tkinter.Frame()
        self.maxFrame.pack(fill=tkinter.BOTH, expand=1, padx=10, pady=15)
        self.inputFrame = tkinter.Frame(self.maxFrame, pady=10)
        self.inputFrame.pack()
        tkinter.Label(self.inputFrame, text='用户名：', font=18).grid(row=0, column=0, sticky='W', pady=5)
        tkinter.Label(self.inputFrame, text='密码：', font=18).grid(row=1, column=0, sticky='W', pady=5)
        self.inputAccount = tkinter.Entry(self.inputFrame, justify=tkinter.CENTER)
        self.inputAccount.grid(row=0, column=1, pady=5)
        self.inputPasswd = tkinter.Entry(self.inputFrame, justify=tkinter.CENTER)
        self.inputPasswd.grid(row=1, column=1, pady=5)
        self.RegBtn = tkinter.Button(self.inputFrame, text='注册', font=10, padx=10)
        self.RegBtn.grid(row=2, column=0, pady=10, columnspan=2)
        self.LoginBtn = tkinter.Button(self.inputFrame, text='返回登录', font=10, padx=10)
        self.LoginBtn.grid(row=3, column=0, pady=10, columnspan=2)
        # 按钮功能绑定
        self.event_bound()

    def event_bound(self):
        self.RegBtn.bind('<ButtonRelease-1>', self.reg_event)
        self.LoginBtn.bind('<ButtonRelease-1>', self.login_event)

    def reg_event(self, event):
        register(account=self.inputAccount.get(), passwd=self.inputPasswd.get())

    def login_event(self, event):
        goto_login(self.master)


def register(**params):
    user = {'account': params['account'],
            'passwd': params['passwd']}
    for i in all_user:
        if params['account'] == i['account']:
            messagebox.showinfo('提示', '帐号已存在!')
            break
        else:
            all_user.append(user)
            messagebox.showinfo('提示', '注册成功!')
            print(all_user)
            break


def login(**params):
    sign = 0
    for i in all_user:
        if params['account'] == i['account']:
            if params['passwd'] == i['passwd']:
                sign = 1
                messagebox.showinfo('提示', '登陆成功!')
                break
            else:
                sign = 2
                messagebox.showinfo('提示', '用户名/密码错误!')
                break
    if sign == 0:
        messagebox.showinfo('提示', '用户名不存在!')


def goto_register(master):
    master.destroy()
    reg_gui = tkinter.Tk()
    reg_gui.title('注册')
    center_window(reg_gui, 300, 200)
    reg_gui.resizable(width=False, height=False)
    app = RegisterGui(reg_gui)
    reg_gui.mainloop()


def goto_login(master):
    master.destroy()
    login_gui = tkinter.Tk()
    login_gui.title('登录')
    center_window(login_gui, 300, 220)
    login_gui.resizable(width=False, height=False)
    app = LoginGui(login_gui)
    login_gui.mainloop()


def center_window(root, w, h):
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))


if __name__ == '__main__':
    gui = tkinter.Tk()
    # 窗口标题
    gui.title('登录')
    # 主窗口大小
    center_window(gui, 300, 220)
    # 禁止改变窗口大小
    gui.resizable(width=False, height=False)

    # 窗口添加组件
    app = LoginGui(gui)
    # 进入消息循环
    gui.mainloop()
