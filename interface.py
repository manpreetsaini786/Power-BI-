import tkinter as tk
from tkinter import messagebox, font as tkfont
import subprocess
import os
import bcrypt 

# Example user database (replace with actual user management in production)
users = {
    "manpreet": bcrypt.hashpw("saini".encode(), bcrypt.gensalt())
}

# Attempt to login
def try_login():
    username = entry_username.get()
    password = entry_password.get().encode()
    
    hashed_password = users.get(username)
    if hashed_password and bcrypt.checkpw(password, hashed_password):
        messagebox.showinfo("Login Success", "You have successfully logged in.")
        open_powerbi_report()
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password")

# Open a .pbix file using Power BI Desktop
def open_powerbi_report():
    pbix_path = r"F:\AdventureWorks Report.pbix"
    if os.path.exists(pbix_path):
        subprocess.Popen(["start", pbix_path], shell=True)
    else:
        messagebox.showerror("File Error", "The specified PBIX file does not exist.")

# Set up the main window
root = tk.Tk()
root.title("Power BI Viewer Login")
root.geometry("400x200")  # Set the window size

# Styling
large_font = tkfont.Font(family="Helvetica", size=14, weight="bold")
bg_color = "#ededed"
root.configure(bg=bg_color)

# Username entry
label_username = tk.Label(root, text="Username:", font=large_font, bg=bg_color)
label_username.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
entry_username = tk.Entry(root, font=large_font)
entry_username.grid(row=0, column=1, padx=10, pady=10)

# Password entry
label_password = tk.Label(root, text="Password:", font=large_font, bg=bg_color)
label_password.grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)
entry_password = tk.Entry(root, show="*", font=large_font)
entry_password.grid(row=1, column=1, padx=10, pady=10)

# Login button
button_login = tk.Button(root, text="Login", command=try_login, font=large_font)
button_login.grid(row=2, column=0, columnspan=2, pady=10)

# Start the GUI event loop
root.mainloop()