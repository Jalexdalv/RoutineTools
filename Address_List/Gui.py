from tkinter import *
from pymysql import *
from tkinter import messagebox


class Gui(object):
    def __init__(self, master):
        self.master = master
        # 输入区域
        self.inputFrame = Frame(self.master, pady=10)
        self.inputFrame.pack()
        Label(self.inputFrame, text='姓名：', font=18).grid(row=0, column=0, pady=5)
        Label(self.inputFrame, text='信息：', font=18).grid(row=1, column=0, pady=5)
        self.inputName = Entry(self.inputFrame)
        self.inputName.grid(row=0, column=1, pady=5)
        self.inputInfo = Entry(self.inputFrame)
        self.inputInfo.grid(row=1, column=1, pady=5)
        self.AddBtn = Button(self.inputFrame, text='添加', font=10, padx=15)
        self.AddBtn.grid(row=3, column=0, pady=10)
        self.DelBtn = Button(self.inputFrame, text='删除', font=10, padx=15)
        self.DelBtn.grid(row=3, column=1, pady=10)
        self.FreshBtn = Button(self.inputFrame, text='刷新', font=10, padx=15)
        self.FreshBtn.grid(row=3, column=2, pady=10)
        # 显示区域
        self.showFrame = Frame(self.master)
        self.showFrame.pack()
        self.showArea = Text(self.showFrame, width=40, height=20, font=16, state=DISABLED)
        self.showArea.pack(side=BOTTOM, fill=BOTH)
        # 按钮绑定
        self.event_bound()
        # 连接数据库
        self.conn = Connect(host='localhost', port=3306, user='root', passwd='root', db='address', charset='utf8')
        # 获取游标
        self.cursor = self.conn.cursor()
        # 显示
        self.update()

    def event_bound(self):
        self.AddBtn.bind('<ButtonRelease-1>', self.add_event)
        self.DelBtn.bind('<ButtonRelease-1>', self.del_event)
        self.FreshBtn.bind('<ButtonRelease-1>', self.update_event)

    def add_event(self, event):
        self.add()

    def del_event(self, event):
        self.dels()

    def update_event(self, event):
        self.update()

    def add(self):
        address_list = dict()
        info = ''
        sql = "SELECT * from addr"
        self.cursor.execute(sql)
        for row in self.cursor.fetchall():
            address_list[row[0]] = row[1]
        if self.inputName.get() in address_list.keys():
            if self.inputInfo.get() in address_list[self.inputName.get()].split(','):
                messagebox.showinfo('提示', '添加失败!')
            else:
                info = address_list[self.inputName.get()]+','+self.inputInfo.get()
                sql = "UPDATE addr SET info='%s' WHERE name='%s'" % (info, self.inputName.get())
                self.cursor.execute(sql)
                self.conn.commit()
                messagebox.showinfo('提示', '添加成功!')
                self.update()
        else:
            info = self.inputInfo.get()
            sql = "INSERT INTO addr(name, info) VALUES ('%s','%s')" % (self.inputName.get(), info)
            self.cursor.execute(sql)
            self.conn.commit()
            messagebox.showinfo('提示', '添加成功!')
            self.update()

    def dels(self):
        address_list = dict()
        sql = "SELECT * from addr"
        self.cursor.execute(sql)
        for row in self.cursor.fetchall():
            address_list[row[0]] = row[1]
        if self.inputName.get() in address_list.keys():
            if self.inputInfo.get():
                if self.inputInfo.get() in address_list[self.inputName.get()].split(','):
                    temp = address_list[self.inputName.get()].split(',')
                    temp.remove(self.inputInfo.get())
                    if not temp:
                        sql = "DELETE FROM addr WHERE name='%s' " % (self.inputName.get())
                        self.cursor.execute(sql)
                        self.conn.commit()
                        self.update()
                        messagebox.showinfo('提示', '删除成功!')
                    else:
                        sql = "UPDATE addr SET info='%s' WHERE name='%s'" % (','.join(temp), self.inputName.get())
                        self.cursor.execute(sql)
                        self.conn.commit()
                        messagebox.showinfo('提示', '删除成功!')
                        self.update()
                else:
                    messagebox.showinfo('提示', '删除失败!')
            else:
                sql = "DELETE FROM addr WHERE name='%s' " % (self.inputName.get())
                self.cursor.execute(sql)
                self.conn.commit()
                self.update()
                messagebox.showinfo('提示', '删除成功!')
        else:
            messagebox.showinfo('提示', '删除失败!')

    def update(self):
        sql = "SELECT * from addr"
        self.cursor.execute(sql)
        self.showArea.config(state=NORMAL)
        self.showArea.delete(0.0, END)
        for row in self.cursor.fetchall():
            self.showArea.insert(END, row[0] + '  ' + row[1] + '\n')
            self.showArea.see(END)
            self.showArea.update()
        self.showArea.config(state=DISABLED)


if __name__ == '__main__':
    gui = Tk()
    # 窗口标题
    gui.title('通讯录')
    # 主窗口大小
    gui.geometry("400x500")
    # 禁止改变窗口大小
    gui.resizable(width=False, height=False)

    # 窗口添加组件
    app = Gui(gui)
    # 进入消息循环
    gui.mainloop()
