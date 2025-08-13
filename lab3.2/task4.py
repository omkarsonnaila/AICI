import tkinter as tk

def generate_bill():
    name = entry_name.get()
    days = int(entry_days.get())
    room = room_var.get()

    rate = {"Single": 1000, "Double": 2000, "Suite": 3500}[room]
    total = days * rate

    bill = f"Customer: {name}\nRoom: {room}\nDays: {days}\nTotal: ₹{total}"
    output.delete("1.0", tk.END)
    output.insert(tk.END, bill)

root = tk.Tk()
root.title("Hotel Bill")
root.geometry("300x300")

tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Days").pack()
entry_days = tk.Entry(root)
entry_days.pack()

tk.Label(root, text="Room Type").pack()
room_var = tk.StringVar(value="Single")
tk.OptionMenu(root, room_var, "Single", "Double", "Suite").pack()

tk.Button(root, text="Generate Bill", command=generate_bill).pack(pady=10)
output = tk.Text(root, height=5)
output.pack()

root.mainloop()
