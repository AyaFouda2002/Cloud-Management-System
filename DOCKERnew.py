import tkinter as tk
from tkinter import Label, Text, messagebox
import os
from PIL import Image, ImageTk

# Function to create Dockerfile
def create_dockerfile(path, content):
    try:
        directory = os.path.dirname(path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(path, "w+") as writer:
            writer.write(content)
        messagebox.showinfo("Success", f"Dockerfile created at {path}")
    except OSError as e:
        messagebox.showerror("File Error", f"An error occurred while creating the Dockerfile: {e.strerror}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

# Function to handle button click for creating Dockerfile
def on_create_button_click(path_entry, content_text):
    path = path_entry.get()
    content = content_text.get("1.0", "end-1c")
    if path and content:
        create_dockerfile(path, content)
    else:
        messagebox.showwarning("Warning", "Please fill in all fields")

# Main application class
class DockerfileCreatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Dockerfile Creator')
        self.setup_ui()

    # Function to create styled buttons
    def create_button(self, text, command):
        button = tk.Button(self, text=text, font=('Arial', 25, 'bold'),
                           command=command, relief='flat',
                           bg="#0000FF", fg="white", cursor='hand2')
        button.bind("<Enter>", lambda e: button.config(bg="#FC766A"))
        button.bind("<Leave>", lambda e: button.config(bg="#5B84B1"))
        return button

    # Setup the UI
    def setup_ui(self):
        # The background image path needs to be updated to the correct path where the image is stored.
        # For example, if the image is stored at "C:/path/to/background.png", replace 'background1.png' with the new path.
        background_image_path = "images\\background1.png"  # Update this line with the correct path

        # Load and set background image
        background_image = Image.open(background_image_path)
        background_photo = ImageTk.PhotoImage(background_image)
        self.geometry(f"{background_photo.width()}x{background_photo.height()}")

        background_label = Label(self, image=background_photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = background_photo  # keep a reference!

        # Path input
        path_label = Label(self, text="Enter Path", font=("Arial", 12, "bold"), width=10)
        path_label.pack(pady=(25, 10))

        self.path_entry = tk.Entry(self, font=('Arial', 12), width=60)
        self.path_entry.pack(pady=(0, 30))

        # Dockerfile content
        content_label = Label(self, text="Dockerfile Content", font=("Arial", 17, "bold"), width=20)
        content_label.pack(pady=(20, 10))

        self.content_text = Text(self, height=10, font=('Arial', 12))
        self.content_text.pack(pady=(0, 50))

        # Create Dockerfile button
        create_button = self.create_button("Create Dockerfile",
                                           lambda: on_create_button_click(self.path_entry, self.content_text))
        create_button.pack(pady=(55, 5))

        # Exit button
        exit_button = self.create_button("Exit", self.quit)
        exit_button.pack(pady=(4, 0))

# Run the application
if __name__ == "__main__":
    app = DockerfileCreatorApp()
    app.mainloop()
