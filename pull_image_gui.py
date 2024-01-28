import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import docker
import docker.errors

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
            image = image.resize((800, 600), Image.LANCZOS)  # Use Image.LANCZOS for resampling

            # Convert to PhotoImage
            bg_image = ImageTk.PhotoImage(image)

            # Create a label to hold the background image
            background_label = tk.Label(self, image=bg_image)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)
            background_label.image = bg_image  # Keep a reference to avoid garbage collection
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load background image: {e}")

    def create_layout(self):
        center_frame = tk.Frame(self, bg='white')
        center_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Entry for image name
        self.image_entry = tk.Entry(center_frame, bg=self.textbox_background, font=('Arial', 12), width=30)
        self.image_entry.pack(pady=10)

        # Pull image button
        pull_button = tk.Button(center_frame, text="Pull Image",
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
                                command=self.pull_image)
        pull_button.pack(pady=10)

        # Exit button
        exit_button = tk.Button(center_frame, text="Exit",
                                background=self.color_button,
                                foreground=self.color_text,
                                activebackground=self.color_button_active,
                                width=15,
                                height=2,
                                highlightthickness=0,
                                highlightbackground=self.color_button,
                                highlightcolor='WHITE',
                                activeforeground=self.color_text,
                                cursor='hand2',
                                border=0,
                                font=('Arial', 12, 'bold'),
                                command=self.quit)  # Exit the application
        exit_button.pack(pady=10)
    def validate_image_name(self, image_name):
        # Basic validation to check for Docker image name format 'repository:tag'
        # It must have a colon. The part before the colon may or may not contain a slash.
        if ':' in image_name:
            repository, tag = image_name.split(':', 1)
            if '/' in repository or not repository.strip():
                # If there's a slash or the repository is empty, it's not valid
                return False
            if not tag.strip():
                # If the tag is empty, it's not valid
                return False
            # The image name is valid if there's a repository and a tag
            return True
        else:
            # If there's no colon, it's not in 'repository:tag' format
            return False


    def pull_image(self):
        image_name = self.image_entry.get().strip()  # Ensure whitespace is removed
        if not image_name:
            messagebox.showwarning("Warning", "Please enter an image name.")
            return
        
        # Validate the image name format
        if not self.validate_image_name(image_name):
            messagebox.showerror("Error", "Invalid image name format. Please ensure it's in the format 'repository:tag'.")
            return
        
        # Attempt to pull the image
        try:
            pulled_image = self.client.images.pull(image_name)
            tag = pulled_image.tags[0] if pulled_image.tags else 'latest'
            messagebox.showinfo("Success", f"Successfully pulled image {tag}")
        except docker.errors.ImageNotFound:
            messagebox.showerror("Not Found", f"The Docker image '{image_name}' could not be found. Please check the image name and try again.")
        except docker.errors.APIError as e:
            messagebox.showerror("Docker Error", f"Error pulling image: {e.explanation}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

    def quit(self):
        self.destroy()  # Ensure a clean exit

# Run the application
if __name__ == "__main__":
    app = DockerGUI()
    app.mainloop()
