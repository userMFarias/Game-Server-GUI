import tkinter as tk
import socket
from tkinter import messagebox

# GUI class
class Toplevel1:
    def __init__(self, top=None):
        self.top = top
        top.geometry("281x450+608+121")
        top.title("UDP Game Client")
        top.configure(background="#d9d9d9")

        self.entry_number = tk.StringVar()

        # Entry field
        self.Entry1 = tk.Entry(top, textvariable=self.entry_number, font="TkFixedFont")
        self.Entry1.place(relx=0.05, rely=0.089, height=20, relwidth=0.299)

        # Label for entry
        self.Label1 = tk.Label(top, text="Enter number (0-9)", anchor='w', background="#d9d9d9")
        self.Label1.place(relx=0.032, rely=0.022, height=21, width=134)

        # Label for result
        self.Label2 = tk.Label(top, text="result_label", anchor='w', background="#d9d9d9")
        self.Label2.place(relx=0.107, rely=0.289, height=21, width=144)

        # Send button
        self.Button1 = tk.Button(top, text="Send", command=self.send_number)
        self.Button1.place(relx=0.107, rely=0.178, height=26, width=67)

    def send_number(self):
        number = self.entry_number.get()

        if not number.isdigit() or not (0 <= int(number) <= 9):
            messagebox.showerror("Invalid Input", "Enter a number between 0 and 9.")
            return

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect(("127.0.0.1", 65432))  # Replace with actual server IP/port
                s.sendall(number.encode())
                result = s.recv(1).decode()

            if result == '1':
                self.Label2.config(text="You win!", fg="green")
            elif result == '0':
                self.Label2.config(text="You lose!", fg="red")
            elif result == '2':
                self.Label2.config(text="Draw!", fg="blue")
            else:
                self.Label2.config(text="Unexpected response", fg="black")

        except Exception as e:
            messagebox.showerror("Connection Error", f"Could not connect to server:\n{e}")

# Run the GUI
def start_up():
    root = tk.Tk()
    app = Toplevel1(root)
    root.mainloop()

if __name__ == '__main__':
    start_up()
