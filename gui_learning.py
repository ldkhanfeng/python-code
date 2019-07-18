import tkinter
# 生成主窗口
window = tkinter.Tk()
window.title('My window')
window.geometry('500x300')

# 标签
label = tkinter.Label(window, text='hello word')
label.pack()

# 按钮
def hit_button():
    exit()
button = tkinter.Button(window, text='Exit', command=hit_button)
button.pack()

# Entry窗口部件
entry = tkinter.Entry(window)
entry.pack()

# Text窗口部件
text = tkinter.Text(window, height=3)
text.pack()

# Listbox
listbox = tkinter.Listbox(window,height=2)
for item in['python', 'tkinter', 'listbox']:
    listbox.insert('end',item)
listbox.pack()

# 
# 主窗口循环显示
window.mainloop()
