from tkinter import *
import tkinter as tk

class Todo:
    def __init__(self,r):
        self.r=r
        self.r.title("TO-DO LIST APPLICAITON")
        self.r.geometry("750x650")

        self.label=Label(self.r,text="To-Do List",font=('Aerial, 15 bold'),width=10,bd=5,bg='red',fg='black')
        self.label.pack(side="top",fill=BOTH)

        self.label2 = Label(self.r, text="Add Tasks", font=('Aerial, 13 bold '), width=10, bd=5, bg='red', fg='black')
        self.label2.place(x=100,y=120)

        self.label3 = Label(self.r, text="Tasks", font=('Aerial, 13 bold '), width=10, bd=5, bg='red', fg='black')
        self.label3.place(x=450, y=110)

        self.text=Listbox(self.r,height=8,bd=5,width=25,font="ariel, 20 italic bold")
        self.text.place(x=320,y=170)

        self.tex = Text(self.r, height=3, bd=6, width=18, font="ariel, 20 bold")
        self.tex.place(x=20, y=160)

        def addTasks():
            con=self.tex.get(1.0,END)
            self.text.insert(END,con)
            with open('data.txt','a') as fi:
                fi.write(con)
                fi.seek(0)
                fi.close()
            self.tex.delete(1.0, END)
        def deleted():
            delete_= self.text.curselection()
            look= self.text.get(delete_)
            with open('data.txt','r+') as f:
                new_f=f.readlines()
                f.seek(0)
                for line in new_f:
                    ite=str(look)
                    if ite not in line:
                        f.write(line)
                f.truncate()
            self.text.delete(delete_)

        with open('data.txt','r') as fi:
            ree=fi.readlines()
            for i in ree:
                df=i.split()
                self.text.insert(END,df)
            fi.close()

        self.button= Button(self.r,text="Add",font="aerial,20",width=10,bd=5,bg='red',fg='black',command=addTasks)
        self.button.place(x=30,y=300)

        self.button2 = Button(self.r, text="Delete", font="aerial,20", width=10, bd=5, bg='red', fg='black',command=deleted)
        self.button2.place(x=30, y=350)

def main():
    r=tk.Tk()
    ans=Todo(r)
    r.mainloop()

if __name__=="__main__":
    main()
