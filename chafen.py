# game = input("请输入游戏名称（arc/phi/chu）：")
# score = float(input("请输入游戏得分或acc(phi请输入acc且不用输入%)："))
# dingshu = float(input("请输入歌曲定数："))


import tkinter
from tkinter import ttk


def arcaea(score, dingshu):
    if score <= 9500000:
        return dingshu
        pass
    if 9500000 < score <= 9800000:
        return dingshu + (score - 9500000) / 300000
        pass
    if 9800000 < score <= 10100000:
        return dingshu + 1.0 + (score - 9800000) / 200000
        pass
    pass


def phigros(score, dingshu):
    if score <= 70:
        dingshu = 0
        return dingshu
        pass
    if 70 < score <= 100:
        return ((100 * (score / 100) - 55) / 45) ** 2 * dingshu
        pass
    pass


def chuni(score, dingshu):
    if score <= 975000:
        return 0
        pass
    if 975000 < score <= 1000000:
        return dingshu + (score - 975000) / 25000
        pass
    if 1000000 < score <= 1005000:
        return dingshu + 1.00 + (score - 1000000) / 10000
        pass
    if 1005000 < score <= 1007500:
        return dingshu + 1.50 + (score - 1005000) / 5000
        pass
    if 1007500 < score <= 1009000:
        return dingshu + 2.00 + (score - 1007500) / 10000
        pass
    if 1009000 < score <= 1010000:
        return dingshu + 2.15
        pass
    pass


window = tkinter.Tk()
window.iconbitmap('ico.ico')
window.title('适用arc,phi,chunithm的简易单曲定数查分器')
window.geometry('300x300')
button = tkinter.Button(window, text='退出', command=lambda: window.destroy(), width=8, height=2)
# button.place(x=40,y=90,anchor='nw') # 绝对位置，放置按钮
button.place(relx=1, rely=1, anchor='se')  # 相对位置，放置按钮

# 显示文本
var = tkinter.StringVar()
var.set("选择音游：\n\n歌曲分数或acc:\n\n歌曲定数:\n\n单曲定数为:")
message = tkinter.Message(window, width=200, textvariable=var)
message.place(x=20, y=50)

# 选择游戏
select = ttk.Combobox(window, width=12, textvariable=tkinter.StringVar(), state="readonly")
lis = ['Arcaea', 'Phigros', 'Chunithm']
select['values'] = lis
select.place(x=150, y=50)

# 输入分数
entry = tkinter.Entry(window, width=12)
entry.place(x=150, y=85)
entry2 = tkinter.Entry(window, width=12)
entry2.place(x=150, y=120)

# 显示定数
var2 = tkinter.StringVar()


# 调用函数
def get_score():
    game = select.get()
    score_str = entry.get()
    dingshu_str = entry2.get()
    if score_str == '' or dingshu_str == '':  # 判断字符串是否为空
        return  # 如果为空，直接返回，不进行后面的代码
    score = float(score_str)
    dingshu = float(dingshu_str)
    if game == 'Arcaea':
        var2.set('%.2f' % arcaea(score, dingshu))
    elif game == 'Phigros':
        var2.set('%.2f' % phigros(score, dingshu))
    elif game == 'Chunithm':
        var2.set('%.2f' % chuni(score, dingshu))
    # 将得到的定数显示在窗口上
    message2 = tkinter.Message(window, width=200, textvariable=var2, fg='red', font=('Arial', 15))
    message2.place(x=160, y=150)
    return var2
    pass


# 按钮
button = tkinter.Button(window, text='计算单曲定数', command=lambda: get_score(), width=10, height=2)
button.place(relx=0, rely=1, anchor='sw')  # 相对位置，放置按钮

# 连续计算单曲定数时，需要先清空上一次的结果
button['command'] = lambda: var2.set('')
button['command'] = lambda: get_score()

if __name__ == '__main__':
    window.mainloop()

