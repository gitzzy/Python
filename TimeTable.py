import tkinter as tk
from tkinter import ttk
import pickle
import os
from datetime import datetime

# Define the timetable
timetable = [
    ("6:00 AM - 6:30 AM", "Wake up, freshen up"),
    ("6:30 AM - 7:00 AM", "Morning exercise / yoga"),
    ("7:00 AM - 7:30 AM", "Breakfast"),
    ("7:30 AM - 9:30 AM", "NIMCET Preparation"),
    ("9:30 AM - 9:45 AM", "Short break"),
    ("9:45 AM - 11:45 AM", "NIMCET Preparation"),
    ("11:45 AM - 12:00 PM", "Break / Relaxation"),
    ("12:00 PM - 1:00 PM", "Data Science"),
    ("1:00 PM - 2:00 PM", "Lunch Break"),
    ("2:00 PM - 4:00 PM", "NIMCET Preparation"),
    ("4:00 PM - 4:15 PM", "Short break"),
    ("4:15 PM - 6:15 PM", "NIMCET Preparation"),
    ("6:15 PM - 6:30 PM", "Break / Snack"),
    ("6:30 PM - 8:00 PM", "NIMCET Preparation"),
    ("8:00 PM - 9:00 PM", "Python"),
    ("9:00 PM - 9:30 PM", "Light review / Revision"),
    ("9:30 PM - 10:00 PM", "Dinner and Relaxation"),
    ("10:00 PM", "Prepare for bed, Sleep")
]

# File to save the progress
progress_file = "progress.pkl"

# Load progress if it exists
if os.path.exists(progress_file):
    with open(progress_file, 'rb') as f:
        done_tasks = pickle.load(f)
else:
    done_tasks = [False] * len(timetable)

# Function to mark task as done
def mark_done(index):
    tasks[index]['label'].config(foreground='green')
    tasks[index]['var'].set(f"{timetable[index][1]} - DONE")
    check_buttons[index]['state'] = 'disabled'
    done_tasks[index] = True
    save_progress()
    update_progress_bar()

# Function to save progress
def save_progress():
    with open(progress_file, 'wb') as f:
        pickle.dump(done_tasks, f)

# Function to update progress bar
def update_progress_bar():
    completed_tasks = sum(done_tasks)
    total_tasks = len(done_tasks)
    progress = (completed_tasks / total_tasks) * 100
    progress_var.set(progress)

# Function to reset all tasks
def reset_tasks():
    for i in range(len(timetable)):
        done_tasks[i] = False
        tasks[i]['label'].config(foreground='red')
        tasks[i]['var'].set(timetable[i][1])
        check_buttons[i]['state'] = 'normal'
    save_progress()
    update_progress_bar()

# Function to check if it's time for a task and notify
def check_task_time():
    current_time = datetime.now().strftime("%I:%M %p")
    for index, (time, task) in enumerate(timetable):
        if time == current_time and not done_tasks[index]:
            tk.messagebox.showinfo("Task Reminder", f"It's time for {task}!")

# Create the main window
root = tk.Tk()
root.title("Timetable Tracker")

# Create a list to hold the StringVar objects
tasks = []
check_buttons = []

# Create and place the timetable entries
for index, (time, task) in enumerate(timetable):
    task_var = tk.StringVar()
    if done_tasks[index]:
        task_var.set(f"{task} - DONE")
        color = 'green'
    else:
        task_var.set(task)
        color = 'red'
    tasks.append({'var': task_var})
    
    frame = ttk.Frame(root)
    frame.pack(fill='x', padx=5, pady=5)
    
    time_label = ttk.Label(frame, text=time, width=20)
    time_label.pack(side='left')
    
    task_label = ttk.Label(frame, textvariable=task_var, width=50, foreground=color)
    task_label.pack(side='left')
    
    tasks[index]['label'] = task_label
    
    check_button = ttk.Button(frame, text="Mark as Done", command=lambda i=index: mark_done(i))
    check_button.pack(side='right')
    
    if done_tasks[index]:
        check_button['state'] = 'disabled'
    
    # Store the button to disable it later
    check_buttons.append(check_button)

# Create a progress bar
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, orient='horizontal', length=200, mode='determinate', variable=progress_var)
progress_bar.pack(pady=10)

# Update the progress bar initially
update_progress_bar()

# Button to reset all tasks
reset_button = ttk.Button(root, text="Reset All Tasks", command=reset_tasks)
reset_button.pack(pady=5)

# Check task time periodically
root.after(1000, check_task_time)

# Start the main event loop
root.mainloop()
