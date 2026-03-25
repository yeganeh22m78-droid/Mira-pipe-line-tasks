import tkinter as tk
from tkinter import ttk, messagebox
from auth import login_user, register_user

def open_login_window():
    root = tk.Tk()
    root.title("Task List")
    root.geometry("350x250")
    root.resizable(False, False)

    ttk.Label(root, text="Welcome to Task List",
              font=("Arial", 14)).pack(pady=20)

    frame = ttk.Frame(root)
    frame.pack(pady=10)

    ttk.Label(frame, text="Username:").grid(row=0, column=0, padx=10, pady=8)
    username_var = tk.StringVar()
    ttk.Entry(frame, textvariable=username_var, width=20).grid(row=0, column=1)

    ttk.Label(frame, text="Password:").grid(row=1, column=0, padx=10, pady=8)
    password_var = tk.StringVar()
    ttk.Entry(frame, textvariable=password_var, show="*", width=20).grid(row=1, column=1)

    def do_login():
        username = username_var.get()
        password = password_var.get()
        if not username or not password:
            messagebox.showerror("Error", "Please fill all fields")
            return
        user_id = login_user(username, password)
        if user_id:
            root.destroy()
            open_tasks_window(user_id, username)
        else:
            messagebox.showerror("Error", "Wrong username or password")

    def do_register():
        username = username_var.get()
        password = password_var.get()
        if not username or not password:
            messagebox.showerror("Error", "Please fill all fields")
            return
        success = register_user(username, password)
        if success:
            messagebox.showinfo("Success", "Registered! Now login.")
        else:
            messagebox.showerror("Error", "Username already exists")

    btn_frame = ttk.Frame(root)
    btn_frame.pack(pady=15)
    ttk.Button(btn_frame, text="Login", command=do_login).grid(row=0, column=0, padx=10)
    ttk.Button(btn_frame, text="Register", command=do_register).grid(row=0, column=1, padx=10)

    root.mainloop()

def open_tasks_window(user_id, username):
    from gui_tasks import open_tasks
    open_tasks(user_id, username)