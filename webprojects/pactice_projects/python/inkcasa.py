import tkinter as tk
from tkinter import messagebox

# Core Structure for Booking and Inventory Management System for "Ink Casa"

# --- Booking Functionality ---

# Classes for Artist, Client, Appointment, and Service
class Artist:
    def __init__(self, artist_id, name, specialization):
        self.artist_id = artist_id
        self.name = name
        self.specialization = specialization

class Client:
    def __init__(self, client_id, name, phone):
        self.client_id = client_id
        self.name = name
        self.phone = phone

class Service:
    def __init__(self, service_id, name, price):
        self.service_id = service_id
        self.name = name
        self.price = price

class Appointment:
    def __init__(self, appointment_id, client, artist, service, date, time):
        self.appointment_id = appointment_id
        self.client = client
        self.artist = artist
        self.service = service
        self.date = date
        self.time = time

# Storage for appointments
appointments = []

# Function to create a new appointment
def create_appointment(client, artist, service, date, time):
    for appointment in appointments:
        if appointment.artist.artist_id == artist.artist_id and appointment.date == date and appointment.time == time:
            raise ValueError("Artist is already booked for this slot.")

    appointment_id = len(appointments) + 1
    new_appointment = Appointment(appointment_id, client, artist, service, date, time)
    appointments.append(new_appointment)
    return new_appointment

# --- Inventory Management ---

# Classes for inventory items
class ClothingItem:
    def __init__(self, item_id, name, stock_level):
        self.item_id = item_id
        self.name = name
        self.stock_level = stock_level

class PiercingSupply:
    def __init__(self, item_id, name, stock_level):
        self.item_id = item_id
        self.name = name
        self.stock_level = stock_level

class AftercareProduct:
    def __init__(self, item_id, name, stock_level):
        self.item_id = item_id
        self.name = name
        self.stock_level = stock_level

# Storage for inventory
global_inventory = {
    "clothing": [],
    "piercing_supplies": [],
    "aftercare_products": []
}

# Function to update inventory levels after a sale
def update_inventory(category, item_id, quantity_sold):
    for item in global_inventory[category]:
        if item.item_id == item_id:
            if item.stock_level >= quantity_sold:
                item.stock_level -= quantity_sold
                return item
            else:
                raise ValueError("Not enough stock available.")

# --- Notifications ---

# Pseudocode: Generate booking confirmation message
def generate_confirmation_message(appointment):
    message = f"Booking Confirmation:\n"
    message += f"Client: {appointment.client.name}\n"
    message += f"Artist: {appointment.artist.name}\n"
    message += f"Service: {appointment.service.name}\n"
    message += f"Date: {appointment.date}\n"
    message += f"Time: {appointment.time}\n"
    return message

# --- User Login System ---

# Classes for Users
class User:
    def __init__(self, user_id, username, password, role):
        self.user_id = user_id
        self.username = username
        self.password = password  # In production, passwords should be hashed
        self.role = role  # Roles: "client", "in-store", "admin"

# Storage for users
users = []

# Function to register a new user
def register_user(username, password, role):
    user_id = len(users) + 1
    new_user = User(user_id, username, password, role)
    users.append(new_user)
    return new_user

# Function to login a user
def login_user(username, password):
    for user in users:
        if user.username == username and user.password == password:
            return user
    return None

# --- GUI Implementation ---

def login_gui():
    def attempt_login():
        username = username_entry.get()
        password = password_entry.get()
        user = login_user(username, password)
        if user:
            messagebox.showinfo("Login Successful", f"Welcome, {user.username}! Role: {user.role}")
            if user.role == "admin":
                admin_dashboard()
            elif user.role == "in-store":
                staff_dashboard()
            elif user.role == "client":
                client_dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    login_window = tk.Tk()
    login_window.title("Ink Casa Login")

    tk.Label(login_window, text="Username:").grid(row=0, column=0)
    username_entry = tk.Entry(login_window)
    username_entry.grid(row=0, column=1)

    tk.Label(login_window, text="Password:").grid(row=1, column=0)
    password_entry = tk.Entry(login_window, show="*")
    password_entry.grid(row=1, column=1)

    login_button = tk.Button(login_window, text="Login", command=attempt_login)
    login_button.grid(row=2, column=0, columnspan=2)

    login_window.mainloop()

def admin_dashboard():
    dashboard = tk.Toplevel()
    dashboard.title("Admin Dashboard")
    tk.Label(dashboard, text="Welcome to the Admin Dashboard").pack()

def staff_dashboard():
    dashboard = tk.Toplevel()
    dashboard.title("Staff Dashboard")
    tk.Label(dashboard, text="Welcome to the Staff Dashboard").pack()

def client_dashboard():
    dashboard = tk.Toplevel()
    dashboard.title("Client Dashboard")
    tk.Label(dashboard, text="Welcome to the Client Dashboard").pack()

# Example Usage
if __name__ == "__main__":
    # Create some initial data
    artist = Artist(1, "Jane Doe", "Portraits")
    client = Client(1, "John Smith", "123-456-7890")
    service = Service(1, "Small Tattoo", 100)

    # Register users
    admin = register_user("admin", "admin123", "admin")
    staff = register_user("staff", "staff123", "in-store")
    client_user = register_user("johnsmith", "password", "client")

    # Launch the GUI
    login_gui()
