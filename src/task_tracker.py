import tkinter as tk

def add_task():
    task = entry.get() # здесь мы получаем слова из поля для ввода
    if task:
        todo_list.insert(tk.END, task) # здесь с помощью константы END вставляем полученное слово в конец списка
        entry.delete(0, tk.END) # здесь очищаем поле для ввода, от нулевого индекса и до конца

def move_task(source, target):
    try:
        selected = source.curselection()[0]  # Берем первый выделенный элемент
        task = source.get(selected)
        source.delete(selected)
        target.insert(tk.END, task)
    except IndexError:
        pass  # Ничего не выбрано

def move_right():
    if todo_list.curselection():
        move_task(todo_list, progress_list)
    elif progress_list.curselection():
        move_task(progress_list, done_list)

def move_left():
    if done_list.curselection():
        move_task(done_list, progress_list)
    elif progress_list.curselection():
        move_task(progress_list, todo_list)

def delete_task():
    # Проверяем, в каком списке есть выделение
    for lst in [todo_list, progress_list, done_list]:
        selected = lst.curselection()
        if selected:
            lst.delete(selected)
            break  # Прерываем после первого найденного


root = tk.Tk()
root.title("Канбан-трекер")
root.configure(
    bg="#403d39",
    padx=15,
    pady=30
)


# === Поле ввода ===
entry = tk.Entry(
    root,
    bg="#252422",
    font=("Segoe UI", 10),
    insertbackground="#fffcf2",
    fg="#fffcf2",
    relief="flat",
    highlightthickness=0,
    bd=1
)
entry.grid(
    row=0,
    column=0,
    columnspan=2,
    sticky="nsew",
    padx=(15, 0),
    ipadx=10
)

# === Кнопка добавления ===
button_add = tk.Button(
    root,
    text="ADD TASK",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    bg="#ccc5b9",
    activebackground="#C94B20",
    activeforeground="#fffcf2",
    fg="#252422",
    command=add_task,
    padx=10,
    pady=5
)
button_add.grid(
    row=0,
    column=2,
    sticky="nsew",
    pady=1,
    padx=15
)

# === Колонка "To Do" ===
todo_frame = tk.Frame(
    root,
    padx=15,
    pady=15,
    bg="#403d39"
)
tk.Label(
    todo_frame,
    text="To Do",
    font=("Segoe UI", 12, "bold"),
    fg="#eb5e28",
    bg="#403d39"
).pack()
todo_list = tk.Listbox(
    todo_frame,
    width=40,
    height=20,
    fg="#FCE3DA",
    bg="#252422",
    font=("Segoe UI", 10),
    highlightthickness=0,
    bd=0,
    relief='flat')
todo_list.pack(
    fill="both",
    expand=True
)
todo_frame.grid(
    row=1,
    column=0,
    sticky="ns"
)

# === Колонка "In Progress" ===
progress_frame = tk.Frame(
    root,
    pady=15,
    bg="#403d39"
)
tk.Label(
    progress_frame,
    text="In Progress",
    font=("Segoe UI", 12, "bold"),
    fg="#fffcf2",
    bg="#403d39"
).pack()
progress_list = tk.Listbox(
    progress_frame,
    width=40,
    height=20,
    bg="#252422",
    fg="#fffcf2",
    font=("Segoe UI", 10),
    highlightthickness=0,
    bd=0,
    relief='flat'
)
progress_list.pack(
    fill="both",
    expand=True
)
progress_frame.grid(
    row=1,
    column=1,
    sticky="ns"
)

# === Колонка "Done" ===
done_frame = tk.Frame(
    root,
    padx=15,
    pady=15,
    bg="#403d39"
)
tk.Label(
    done_frame,
    text="Done",
    font=("Segoe UI", 12, "bold"),
    fg="#41E63E",
    bg="#403d39"
).pack()
done_list = tk.Listbox(
    done_frame,
    width=40,
    height=20,
    bg="#252422",
    fg="#DFEBC1",
    font=("Segoe UI", 10),
    highlightthickness=0,
    bd=0,
    relief='flat'
)
done_list.pack(
    fill="both",
    expand=True
)
done_frame.grid(
    row=1,
    column=2,
    sticky="ns"
)

# === Кнопка "ВЛЕВО" ===
button_left = tk.Button(
    root,
    text="◀ MOVE TO LEFT",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    bg="#ccc5b9",
    activebackground="#C94B20",
    activeforeground="#fffcf2",
    fg="#252422",
    command=move_left,
    padx=10,
    pady=5
)
button_left.grid(
    row=3,
    column=0,
    sticky="nsew",
    padx=15
)

# === Кнопка "ВПРАВО" ===
button_right = tk.Button(
    root,
    text="MOVE TO RIGHT ▶",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    bg="#ccc5b9",
    activebackground="#C94B20",
    activeforeground="#fffcf2",
    fg="#252422",
    command=move_right,
    padx=10,
    pady=5
)
button_right.grid(
    row=3,
    column=1,
    sticky="nsew"
)

# === Кнопка "УДАЛИТЬ" ===
button_delete = tk.Button(
    root,
    text="DELETE TASK",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    bg="#ccc5b9",
    activebackground="#C94B20",
    activeforeground="#fffcf2",
    fg="#252422",
    command=delete_task,
    padx=10,
    pady=5
)
button_delete.grid(
    row=3,
    column=2,
    sticky="nsew",
    pady=1,
    padx=15
)

root.mainloop()
