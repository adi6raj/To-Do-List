import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

# Function to add a new task
def add_task():
    task = task_entry.get()
    if task.strip():
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty!")

# Function to delete the selected task
def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Selection Error", "No task selected to delete!")

# Function to clear all tasks
def clear_all_tasks():
    if messagebox.askyesno("Clear All", "Are you sure you want to clear all tasks?"):
        task_listbox.delete(0, tk.END)

# Function to mark or unmark a task with strikethrough
def mark_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        current_task = task_listbox.get(selected_task_index)
        if current_task.startswith("✔ "):  # If already marked, unmark it
            task_listbox.delete(selected_task_index)
            task_listbox.insert(selected_task_index, current_task[2:])
            task_listbox.itemconfig(selected_task_index, fg="black")  # Reset color
        else:  # Mark the task
            task_listbox.delete(selected_task_index)
            task_listbox.insert(selected_task_index, "✔ " + current_task)
            task_listbox.itemconfig(selected_task_index, fg="green")  # Change color to green
    else:
        messagebox.showwarning("Selection Error", "No task selected to mark!")

# Function to add a due date/reminder to a task
def add_due_date():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        current_task = task_listbox.get(selected_task_index)
        due_date = simpledialog.askstring("Due Date", "Enter a due date (e.g., YYYY-MM-DD):")
        if due_date:
            task_listbox.delete(selected_task_index)
            task_listbox.insert(selected_task_index, f"{current_task} (Due: {due_date})")
    else:
        messagebox.showwarning("Selection Error", "No task selected to add a due date!")

# Initialize the main application window
root = tk.Tk()
root.title("Enhanced To-Do List with Mark and Due Dates")
root.geometry("450x600")
root.configure(bg="#f7f7f7")

# Title label
title_label = tk.Label(root, text="Enhanced To-Do List", font=("Arial", 18, "bold"), bg="#f7f7f7", fg="#333")
title_label.pack(pady=10)

# Entry widget to add tasks
task_entry = tk.Entry(root, font=("Arial", 14), width=30)
task_entry.pack(pady=10)

# Add Task button
add_task_button = tk.Button(root, text="Add Task", font=("Arial", 12), bg="#4caf50", fg="white", command=add_task)
add_task_button.pack(pady=5)

# Listbox to display tasks
task_listbox = tk.Listbox(root, font=("Arial", 14), width=40, height=15, selectmode=tk.SINGLE)
task_listbox.pack(pady=10)

# Buttons for task management
button_frame = tk.Frame(root, bg="#f7f7f7")
button_frame.pack(pady=10)

delete_task_button = tk.Button(button_frame, text="Delete Task", font=("Arial", 12), bg="#e63946", fg="white", command=delete_task)
delete_task_button.grid(row=0, column=0, padx=10)

clear_all_button = tk.Button(button_frame, text="Clear All", font=("Arial", 12), bg="#ffb400", fg="white", command=clear_all_tasks)
clear_all_button.grid(row=0, column=1, padx=10)

mark_task_button = tk.Button(button_frame, text="Mark/Unmark", font=("Arial", 12), bg="#2196f3", fg="white", command=mark_task)
mark_task_button.grid(row=0, column=2, padx=10)

add_due_date_button = tk.Button(button_frame, text="Add Due Date", font=("Arial", 12), bg="#9c27b0", fg="white", command=add_due_date)
add_due_date_button.grid(row=0, column=3, padx=10)

# Run the Tkinter event loop
root.mainloop()
