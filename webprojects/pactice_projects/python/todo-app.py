#importing packages
from tkinter import *
import tkinter.messagebox

#Creating the initial window
window=Tk()
#giving a title
window.title("Python To-Do List App")

#Frame widget to holkd the listbox and the scrollbar
frame_task=Frame(window)
frame_task.pack()

#To hold items in a listbox
listbox_task=Listbox(frame_task, bg="black", fg="white", height=15, width=50, font="Helvetica")
listbox_task.pack(side=tkinter.LEFT)

#Scroll down in case the total list exceeds tje sixe of the given window
scrollbar_task=Scrollbar(frame_task)
scrollbar_task.pack(side=tkinter.RIGHT, fill=tkinter.Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

#Button WWidget
entry_button=Button (window,text="Add Task", width=50, command=entertask)
entry_button.pack(pady=3)

delete_button=Button(window,text="Delete Task", width=50,command=deletetask)
delete_button.pack(pady=3)

mark_button=Button(window,text="Mark as Done",width=50,command=markdone)
mark_button.pack(pady=3)

window.mainloop()

##Defining the To-do list functions##

def entertask():
    #A new window to pop up to take input
    input_text=""
    def add():
        input_text=entry_task.get(1.0, "end-1c")
        if input_text=="":
            tkinter.messagebox.showwarning(title="Warning!",message="Please Enter Some Text!")
        else:
            listbox_task.insert(END,input_text)
            #close the root1 window
            root1.destroy()
        root1=Tk()
        root1.title("Add Task")
        entry_task=Text(root1,width=40,height=4)
        entry_task.pack()
        button_temp=Button(root1,text="Add Task",command=add)
        button_temp.pack()
        root1.mainloop()

#Function to facilitate the delete task from the listbox
def deletetask():
    #deletes the selected item
    selected=listbox_task.curselection()
    listbox_task.delete(selected[0])

#Executes this to mark as completed
def markcompleted():
    marked=listbox_task.curselection()
    temp=marked[0]
    #Store the text of the selected item as a string
    temp_marked=listbox_task.get(marked)
    #Update it
    temp_marked=temp_marked+" X"
    #Delete it then instert it
    listbox_task.delete(temp)
    listbox_task.insert(temp,temp_marked)