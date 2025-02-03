
import tkinter as tk
from tkinter import messagebox, simpledialog
import random

class BankAccount:
    def __init__(self, name, account_number):
        self.name = name
        self.account_number = account_number
        self.balance = 0.00

class BankTellerApp:
    def __init__(self, master):
        self.master = master
        master.title("Bank Teller Application")
        master.geometry("500x600")
        master.configure(bg='#f0f0f0')

        # Dictionary to store multiple bank accounts
        self.accounts = {}
        self.current_account = None

        # Create UI Components
        self.create_ui()

    def create_ui(self):
        # Title Label
        title_label = tk.Label(
            self.master, 
            text="Bank Teller System", 
            font=('Arial', 20, 'bold'), 
            bg='#3498db', 
            fg='white', 
            width=30, 
            pady=10
        )
        title_label.pack(pady=20)

        # Account Name Entry
        name_frame = tk.Frame(self.master, bg='#f0f0f0')
        name_frame.pack(pady=10)
        
        tk.Label(name_frame, text="Account Name:", bg='#f0f0f0', font=('Arial', 12)).pack(side=tk.LEFT, padx=10)
        self.name_entry = tk.Entry(name_frame, font=('Arial', 12), width=25)
        self.name_entry.pack(side=tk.LEFT)

        # Account Number Display
        number_frame = tk.Frame(self.master, bg='#f0f0f0')
        number_frame.pack(pady=10)
        
        tk.Label(number_frame, text="Account Number:", bg='#f0f0f0', font=('Arial', 12)).pack(side=tk.LEFT, padx=10)
        self.number_label = tk.Label(number_frame, text="Not Generated", font=('Arial', 12, 'bold'), fg='#e74c3c')
        self.number_label.pack(side=tk.LEFT)

        # Balance Display
        balance_frame = tk.Frame(self.master, bg='#f0f0f0')
        balance_frame.pack(pady=10)
        
        tk.Label(balance_frame, text="Current Balance:", bg='#f0f0f0', font=('Arial', 12)).pack(side=tk.LEFT, padx=10)
        self.balance_label = tk.Label(balance_frame, text="$0.00", font=('Arial', 12, 'bold'), fg='#2ecc71')
        self.balance_label.pack(side=tk.LEFT)

        # Action Buttons
        button_frame = tk.Frame(self.master, bg='#f0f0f0')
        button_frame.pack(pady=20)

        buttons = [
            ("Generate Account", self.generate_account, '#3498db'),
            ("Deposit", self.deposit, '#2ecc71'),
            ("Withdraw", self.withdraw, '#e74c3c'),
            ("Account Details", self.show_account_details, '#f39c12')
        ]

        for text, command, color in buttons:
            btn = tk.Button(
                button_frame, 
                text=text, 
                command=command, 
                bg=color, 
                fg='white', 
                font=('Arial', 12), 
                width=15
            )
            btn.pack(pady=10)

    def generate_account(self):
        # Validate name entry
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showerror("Error", "Please enter an account name")
            return

        # Generate random 10-digit account number
        account_number = str(random.randint(1000000000, 9999999999))
        
        # Create a new bank account
        new_account = BankAccount(name, account_number)
        
        # Store the account in the accounts dictionary
        self.accounts[account_number] = new_account
        
        # Set as current account
        self.current_account = new_account
        
        # Update UI
        self.number_label.config(text=account_number, fg='#2ecc71')
        self.balance_label.config(text="$0.00", fg='#2ecc71')
        
        messagebox.showinfo("Account Created", f"Account created for {name}\nAccount Number: {account_number}")

    def deposit(self):
        if not self.current_account:
            messagebox.showerror("Error", "Please generate an account first")
            return

        # Prompt for deposit amount
        amount = simpledialog.askfloat("Deposit", "Enter deposit amount:", minvalue=0.01)
        
        if amount:
            self.current_account.balance += amount
            self.balance_label.config(text=f"${self.current_account.balance:.2f}", fg='#2ecc71')
            messagebox.showinfo("Deposit", f"Deposited ${amount:.2f}")

    def withdraw(self):
        if not self.current_account:
            messagebox.showerror("Error", "Please generate an account first")
            return

        # Prompt for withdrawal amount
        amount = simpledialog.askfloat("Withdraw", "Enter withdrawal amount:", minvalue=0.01)
        
        if amount:
            if amount > self.current_account.balance:
                messagebox.showerror("Error", "Insufficient funds")
            else:
                self.current_account.balance -= amount
                self.balance_label.config(text=f"${self.current_account.balance:.2f}", fg='#e74c3c')
                messagebox.showinfo("Withdrawal", f"Withdrawn ${amount:.2f}")

    def show_account_details(self):
        if not self.current_account:
            messagebox.showerror("Error", "Please generate an account first")
            return

        details = (
            f"Account Name: {self.current_account.name}\n"
            f"Account Number: {self.current_account.account_number}\n"
            f"Current Balance: ${self.current_account.balance:.2f}"
        )
        messagebox.showinfo("Account Details", details)

def main():
    root = tk.Tk()
    app = BankTellerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()