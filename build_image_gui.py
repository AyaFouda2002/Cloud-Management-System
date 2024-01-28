
import tkinter as tk
from tkinter import Label, Entry, messagebox
from PIL import Image, ImageTk
import docker
import os

class DockerImageBuilder(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Docker Image Builder")
        self.geometry('1000x600')

        self.client = docker.from_env()
        self.init_ui()

    def init_ui(self):
        # Set the background image
        self.set_background('images/background1.png')

        # Define input fields and labels
        self.dockerfile_path_entry = self.create_label_entry("Dockerfile Path:", 50, 50, 250, 50)
        self.dockerfile_name_entry = self.create_label_entry("Dockerfile Name:", 50, 150, 250, 150)
        self.tag_entry = self.create_label_entry("Image Tag:", 50, 250, 250, 250)

        # Build Image button
        self.build_image_button = tk.Button(self, text="Build Image", command=self.handle_build_image, 
                                            bg="#0000FF", fg="white", width=20, height=2, 
                                            font=("Arial", 20, "bold"))
        self.build_image_button.place(x=400, y=350)

        # Exit button
        self.exit_button = tk.Button(self, text="Exit", command=self.destroy,
                                     bg="#0000FF", fg="white", width=15, height=2, 
                                     font=("Arial", 15, "bold"))
        self.exit_button.place(x=480, y=450)

    def create_label_entry(self, text, label_x, label_y, entry_x, entry_y):
        label = Label(self, text=text, font=("Arial", 16, "bold"))
        label.place(x=label_x, y=label_y)
        entry = Entry(self, font=("Arial", 16, "bold"))
        entry.place(x=entry_x, y=entry_y)
        return entry

    def set_background(self, image_path):
        image = Image.open(image_path)
        image = image.resize((1000, 600), Image.LANCZOS)
        bg_image = ImageTk.PhotoImage(image)
        background_label = tk.Label(self, image=bg_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = bg_image

    def handle_build_image(self):
        dockerfile_path = self.dockerfile_path_entry.get().strip()
        dockerfile_name = self.dockerfile_name_entry.get().strip()
        tag = self.tag_entry.get().strip().replace("/", "")

        # Validation checks
        if not dockerfile_path or not dockerfile_name or not tag:
            messagebox.showerror("Error", "All fields must be filled out.")
            return

        if '\\' in tag or '/' in tag:
            messagebox.showerror("Error", "Tag should not contain slashes.")
            return

        full_dockerfile_path = os.path.join(dockerfile_path, dockerfile_name)

        if not os.path.isfile(full_dockerfile_path):
            messagebox.showerror("Error", f"Dockerfile not found at {full_dockerfile_path}. Please check the path and name.")
            return

        try:
            image, logs = self.client.images.build(path=dockerfile_path, dockerfile=dockerfile_name, tag=tag)
            for log in logs:
                if 'stream' in log:
                    print(log['stream'].strip())
            messagebox.showinfo("Success", f"Image {tag} built successfully.")
        except docker.errors.BuildError as build_err:
            messagebox.showerror("Build Error", str(build_err))
        except docker.errors.APIError as api_err:
            messagebox.showerror("API Error", str(api_err))
        except Exception as e:
            messagebox.showerror("Unexpected Error", str(e))

# Run the application
if __name__ == "__main__":
    app = DockerImageBuilder()
    app.mainloop()
