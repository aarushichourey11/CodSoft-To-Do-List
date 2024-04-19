
import tkinter as tk
def add_task():
    task=entry.get()
    if task:
        todo_list.insert(tk.END,task)
        entry.delete(0,tk.END)

def toggle_completed():
    selected_index = todo_list.curselection()
    if selected_index:  # Check if any item is selected
        completed = completed_tasks.get(selected_index[0], False)
        completed_tasks[selected_index[0]] = not completed
        task_text = todo_list.get(selected_index)
        if not completed:
            task_text = f"[X] {task_text}"
        else:
            task_text = f"[ ] {task_text}"
        todo_list.delete(selected_index)
        todo_list.insert(selected_index, task_text)

def delete_task():
    selected_index=todo_list.curselection()
    if selected_index:
        todo_list.delete(selected_index)
        
root = tk.Tk()
root.title("My To Do App")
root.geometry("800x700")


heading_label = tk.Label(root, text="To-Do List", font=("Helvetica", 20, "bold"), fg="purple")
heading_label.pack(pady=20)

entry = tk.Entry(root, width=60)
entry.pack(pady=30,ipady=8)


button_style = {"font": ("Helvetica", 12), "width": 15, "height": 2, "bg": "#E6E6FA", "fg": "black", "activebackground": "#45a049"}

add_button=tk.Button(root,text="Add Task",command=add_task,**button_style)
add_button.pack()

listbox_style = {"width": 50, "height": 20, "font": ("Helvetica", 12)}
todo_list = tk.Listbox(root, **listbox_style)
todo_list.pack(pady=20, ipady=25)


completed_tasks={}
toggle_button=tk.Button(root, text="Task Completed",command=toggle_completed,**button_style)
toggle_button.pack()

delete_button=tk.Button(root,text="Delete Task",command=delete_task,**button_style)
delete_button.pack()


# Run the Tkinter event loop
root.mainloop()
