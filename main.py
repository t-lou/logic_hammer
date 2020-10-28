import tkinter
from logic_hammer import LogicHammer

root = tkinter.Tk()
root.title('Logic Hammer')

scroll_bar_src = tkinter.Scrollbar(root)
text_field_src = tkinter.Text(root, height=50, width=120)

scroll_bar_src.pack(side=tkinter.LEFT, fill=tkinter.Y)
text_field_src.pack(side=tkinter.LEFT, fill=tkinter.Y)

scroll_bar_src.config(command=text_field_src.yview)
text_field_src.config(yscrollcommand=scroll_bar_src.set)

scroll_bar_dst = tkinter.Scrollbar(root)
text_field_dst = tkinter.Text(root, height=50, width=120)

scroll_bar_dst.pack(side=tkinter.RIGHT, fill=tkinter.Y)
text_field_dst.pack(side=tkinter.LEFT, fill=tkinter.Y)

scroll_bar_dst.config(command=text_field_dst.yview)
text_field_dst.config(yscrollcommand=scroll_bar_dst.set)


def exec(event):
    content = text_field_src.get('1.0', tkinter.END).strip()
    content = content.replace('\n', '')
    text_field_src.delete('1.0', tkinter.END)
    text_field_src.insert(tkinter.END, content)
    result = str(LogicHammer(content))
    text_field_dst.delete('1.0', tkinter.END)
    text_field_dst.insert(tkinter.END, result)


root.bind('<Return>', exec)

text_field_src.focus()
tkinter.mainloop()
