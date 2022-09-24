import tkinter as tk
window=tk.Tk()
window.geometry("400x500")
def onclick():
    print(1)

chkvar1=tk.IntVar()
chkbtn1=tk.Checkbutton(text="Спальня 1",variable=chkvar1,onvalue=1,offvalue=0)
chkbtn1.grid(row=0,column=0)
scl=tk.Scale(label="Яркость",from_=1,to=100,orient=tk.HORIZONTAL,length=300,width=20)
scl.grid(row=1,column=0)

chkvar2=tk.IntVar()
chkbtn2=tk.Checkbutton(text="Спальня 2",variable=chkvar2,onvalue=1,offvalue=0)
chkbtn2.grid(row=2,column=0)
scl=tk.Scale(label="Яркость",from_=1,to=100,orient=tk.HORIZONTAL,length=300,width=20)
scl.grid(row=3,column=0)

chkvar3=tk.IntVar()
chkbtn3=tk.Checkbutton(text="Ванная",variable=chkvar3,onvalue=1,offvalue=0)
chkbtn3.grid(row=4,column=0)
scl=tk.Scale(label="Яркость",from_=1,to=100,orient=tk.HORIZONTAL,length=300,width=20)
scl.grid(row=5,column=0)

chkvar4=tk.IntVar()
chkbtn4=tk.Checkbutton(text="Кухня",variable=chkvar4,onvalue=1,offvalue=0)
chkbtn4.grid(row=6,column=0)
scl=tk.Scale(label="Яркость",from_=1,to=100,orient=tk.HORIZONTAL,length=300,width=20)
scl.grid(row=7,column=0)

chkvar5=tk.IntVar()
chkbtn5=tk.Checkbutton(text="Прихожая",variable=chkvar5,onvalue=1,offvalue=0)
chkbtn5.grid(row=8,column=0)
scl=tk.Scale(label="Яркость",from_=1,to=100,orient=tk.HORIZONTAL,length=300,width=20)
scl.grid(row=9,column=0)
window.mainloop()
