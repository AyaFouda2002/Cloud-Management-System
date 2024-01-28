import tkinter as tk
from tkinter import Toplevel, Label, Canvas, Scrollbar, Frame
from PIL import Image, ImageTk
import docker

class DockerApp_list(tk.Tk):
    def __init__(self):
        super().__init__()

        # Initialize Docker client
        self.client = docker.from_env()

        # Configure the main window size
        self.geometry('1166x718')

        # Load and set the background image
        self.set_background_image('images/background1.png')

        # Set up the canvas and scrollbar for buttons
        self.canvas = Canvas(self)
        self.scrollbar = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.buttons_frame = Frame(self.canvas)

        self.buttons_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.buttons_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Pack the canvas and scrollbar into the window
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Define colors
        self.color2 = '#264cf5'
        self.color3 = '#1e26c7'
        self.color4 = 'Black'

        # List Docker images as buttons
        self.list_images_as_buttons()

        # Add Exit button
        self.exit_button = self.create_button("Exit")
        self.exit_button.configure(command=self.close_app)
        self.exit_button.pack(pady=(10, 5))

    def set_background_image(self, image_path):
        try:
            bg_image = Image.open(image_path)
            photo = ImageTk.PhotoImage(bg_image)

            self.bg_panel = Label(self, image=photo)
            self.bg_panel.image = photo  # keep a reference!
            self.bg_panel.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            print(f"Error loading background image: {e}")

    def create_button(self, text):
        return tk.Button(self.buttons_frame,
                         text=text,
                         background=self.color2,
                         foreground=self.color4,
                         activebackground=self.color3,
                         width=100,
                         height=2,
                         highlightthickness=0,
                         highlightbackground=self.color2,
                         highlightcolor='WHITE',
                         activeforeground=self.color4,
                         cursor='hand1',
                         border=0,
                         font=('Arial', 15, 'bold'))

    def list_images_as_buttons(self):
        for image in self.client.images.list():
            tag = image.tags[0] if image.tags else "Untagged"
            button = self.create_button(tag)
            button.configure(command=lambda img=image: self.open_details_window(img))
            button.pack(fill=tk.X, pady=(10, 5))

    def open_details_window(self, image):
        details_window = Toplevel(self)
        details_window.title("Image Details")

        details = f"Tags: {image.tags}\nID: {image.id}\nSize: {image.attrs['Size']} bytes"
        details_label = tk.Label(details_window, text=details, font=("Arial", 12))
        details_label.pack(pady=20)

    def close_app(self):
        self.destroy()

if __name__ == "__main__":
    app = DockerApp()
    app.mainloop()
