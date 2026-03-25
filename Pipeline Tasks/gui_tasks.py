import tkinter as tk
from tkinter import ttk, messagebox
from tasks import add_task, get_tasks, update_task, delete_task

def open_tasks(user_id, username):
    root = tk.Tk()
    root.title(f"Tasks - {username}")
    root.geometry("600x450")

    ttk.Label(root, text=f"Welcome {username}!",
              font=("Arial", 13)).pack(pady=10)

    frame = ttk.Frame(root)
    frame.pack(fill="both", expand=True, padx=20, pady=5)

    columns = ("Title", "Description", "Status")
    tree = ttk.Treeview(frame, columns=columns, show="headings", height=12)
    tree.heading("Title", text="Title")
    tree.heading("Description", text="Description")
    tree.heading("Status", text="Status")
    tree.column("Title", width=150)
    tree.column("Description", width=250)
    tree.column("Status", width=100)
    tree.pack(fill="both", expand=True)

    task_ids = []

    def load_tasks():
        tree.delete(*tree.get_children())
        task_ids.clear()
        tasks = get_tasks(user_id)
        for task in tasks:
            task_ids.append(task[0])
            tree.insert("", "end", values=(task[1], task[2], task[3]))

    def add_new_task():
        popup = tk.Toplevel(root)
        popup.title("New Task")
        popup.geometry("300x200")

        ttk.Label(popup, text="Title:").pack(pady=5)
        title_var = tk.StringVar()
        ttk.Entry(popup, textvariable=title_var, width=25).pack()

        ttk.Label(popup, text="Description:").pack(pady=5)
        desc_var = tk.StringVar()
        ttk.Entry(popup, textvariable=desc_var, width=25).pack()

        def save():
            if not title_var.get():
                messagebox.showerror("Error", "Enter a title")
                return
            add_task(user_id, title_var.get(), desc_var.get())
            popup.destroy()
            load_tasks()

        ttk.Button(popup, text="Save", command=save).pack(pady=15)

    def edit_task():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a task")
            return

        index = tree.index(selected[0])
        task_id = task_ids[index]
        values = tree.item(selected[0])["values"]

        popup = tk.Toplevel(root)
        popup.title("Edit Task")
        popup.geometry("300x230")

        ttk.Label(popup, text="Title:").pack(pady=5)
        title_var = tk.StringVar(value=values[0])
        ttk.Entry(popup, textvariable=title_var, width=25).pack()

        ttk.Label(popup, text="Description:").pack(pady=5)
        desc_var = tk.StringVar(value=values[1])
        ttk.Entry(popup, textvariable=desc_var, width=25).pack()

        ttk.Label(popup, text="Status:").pack(pady=5)
        status_var = tk.StringVar(value=values[2])
        ttk.Combobox(popup, textvariable=status_var,
                     values=["pending", "done"]).pack()

        def save():
            update_task(task_id, title_var.get(),
                       desc_var.get(), status_var.get())
            popup.destroy()
            load_tasks()

        ttk.Button(popup, text="Save", command=save).pack(pady=15)

    def remove_task():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a task")
            return
        confirm = messagebox.askyesno("Confirm", "Are you sure?")
        if confirm:
            index = tree.index(selected[0])
            task_id = task_ids[index]
            delete_task(task_id)
            load_tasks()

    btn_frame = ttk.Frame(root)
    btn_frame.pack(pady=10)
    ttk.Button(btn_frame, text="New Task", command=add_new_task).grid(row=0, column=0, padx=8)
    ttk.Button(btn_frame, text="Edit", command=edit_task).grid(row=0, column=1, padx=8)
    ttk.Button(btn_frame, text="Delete", command=remove_task).grid(row=0, column=2, padx=8)

    load_tasks()
    root.mainloop()