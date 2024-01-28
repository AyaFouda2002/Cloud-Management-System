import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import docker

class DockerGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.client = docker.from_env()
        self.geometry('800x600')  # Window size

        # Define colors
        self.color_button = '#264cf5'
        self.color_button_active = '#1e26c7'
        self.color_text = 'White'
        self.textbox_background = "#f0f0f0"

        # Set the background image
        self.set_background('images/background1.png')

        # Create the layout
        self.create_layout()

    def set_background(self, image_path):
        # Load the image using PIL
        try:
            image = Image.open(image_path)
            image = image.resize((800, 600), Image.LANCZOS)  # Resize to fit the window using LANCZOS

            # Convert to PhotoImage
            bg_image = ImageTk.PhotoImage(image)

            # Create a label to hold the background image
            background_label = tk.Label(self, image=bg_image)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)
            background_label.image = bg_image  # Keep a reference to avoid garbage collection
        except Exception as e:
            print(f"Error loading background image: {e}")

    def create_layout(self):
        center_frame = tk.Frame(self, bg='white')
        center_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Entry for container name
        container_entry = tk.Entry(center_frame, bg=self.textbox_background, font=('Arial', 12), width=30)
        container_entry.pack(pady=10)

        # Stop container button
        stop_button = tk.Button(center_frame, text="Stop Container",
                                background=self.color_button,
                                foreground=self.color_text,
                                activebackground=self.color_button_active,
                                width=20,
                                height=2,
                                highlightthickness=0,
                                highlightbackground=self.color_button,
                                highlightcolor='WHITE',
                                activeforeground=self.color_text,
                                cursor='hand2',
                                border=0,
                                font=('Arial', 12, 'bold'),
                                command=lambda: self.stop_container(container_entry.get()))
        stop_button.pack(pady=10)

        # Exit button
        exit_button = tk.Button(center_frame, text="Exit",
                                background=self.color_button,
                                foreground=self.color_text,
                                activebackground=self.color_button_active,
                                width=20,
                                height=2,
                                highlightthickness=0,
                                highlightbackground=self.color_button,
                                highlightcolor='WHITE',
                                activeforeground=self.color_text,
                                cursor='hand2',
                                border=0,
                                font=('Arial', 12, 'bold'),
                                command=self.close_application)
        exit_button.pack(pady=10)

    def stop_container(self, container_name):
        # Stop the container
        try:
            container = self.client.containers.get(container_name)
            container.stop()
            messagebox.showinfo("Success", f"Container {container_name} stopped successfully.")  # Show success message
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")  # Show error message

    def close_application(self):
        self.destroy()

# Run the application
if __name__ == "__main__":
    app = DockerGUI()
    app.mainloop()
