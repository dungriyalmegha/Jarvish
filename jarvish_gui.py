import tkinter as tk
from PIL import ImageTk, Image

def start_assistant():
    query = entry.get()
    # Process the query and perform assistant tasks here
    # Add your code to handle the query and perform actions

def exit_assistant():
    window.destroy()

# Create the main window
window = tk.Tk()
window.title("Jarvisht")
window.geometry("500x500")
window.configure(bg="#f2f2f2")

# Load and display a logo image
logo_image = Image.open("robot.jpg")
logo_image = logo_image.resize((300, 200))
logo_photo = ImageTk.PhotoImage(logo_image)

logo_label = tk.Label(window, image=logo_photo, bg="#f2f2f2")
logo_label.pack(pady=20)
# Create a frame with blue border
frame = tk.Frame(window, bg="blue", borderwidth=2, relief="solid")
frame.pack(padx=20, pady=20)

# Create a label for the title
title_label = tk.Label(window, text="Welcome", font=("Arial", 16), bg="#f2f2f2")
title_label.pack()



# Create a start button
start_button = tk.Button(window, text="Start", font=("Arial", 16), width=15, bg="#4caf50", fg="white", command=start_assistant)
start_button.pack()

# Create an exit button
exit_button = tk.Button(window, text="Exit", font=("Arial", 16), width=15, bg="#f44336", fg="white", command=exit_assistant)
exit_button.pack(pady=20)

# Run the main window's event loop
window.mainloop()