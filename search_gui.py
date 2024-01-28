import tkinter as tk
from tkinter import messagebox, scrolledtext, font
from PIL import Image, ImageTk
import docker
from datetime import datetime

class DockerApp_dockerhub(tk.Tk):
    def __init__(self):
        super().__init__()

        self.client = docker.from_env()
        self.geometry('800x600')  # Adjust the size of the window as needed

        # Load and set background image
        self.set_background('images/background1.png')  # Update the path to your background image

        # Define colors
        self.color_button = '#264cf5'
        self.color_button_active = '#1e26c7'
        self.color_text = 'White'
        self.textbox_background = "#f0f0f0"  # Modern light grey background

        # Create the layout
        self.create_layout()

    def set_background(self, image_path):
        try:
            background_image = Image.open(image_path)
            background_photo = ImageTk.PhotoImage(background_image)
            self.geometry(f"{background_photo.width()}x{background_photo.height()}")

            background_label = tk.Label(self, image=background_photo)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)
            background_label.image = background_photo
        except Exception as e:
            print(f"Error loading background image: {e}")

    def create_layout(self):
        # Frame to hold the widgets, placed in the center
        center_frame = tk.Frame(self, bg="#ffffff")
        center_frame.place(relx=0.5, rely=0.5, anchor='center', width=400, height=200)  # Adjust size and position

        # Label
        label_font = font.Font(size=12, weight='bold')  # Adjust font size and weight
        search_label = tk.Label(center_frame, text="Enter Image Name to Search on DockerHub:", bg="#ffffff", font=label_font)
        search_label.pack(pady=10)

        # Text Entry
        search_entry = tk.Entry(center_frame, width=50, bg=self.textbox_background, font=('Arial', 12))
        search_entry.pack(pady=10)

        # Search Button
        search_button = tk.Button(center_frame, text="Search Image",
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
                                  command=lambda: self.search_image_dockerhub(search_entry))
        search_button.pack(pady=10)

        # Exit Button
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
                                command=self.close_app)
        exit_button.pack(pady=10)

    def search_image_dockerhub(self, entry_widget):
        image_name = entry_widget.get()
        try:
            results = self.client.images.search(term=image_name)
            self.show_results_in_new_window(results)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_results_in_new_window(self, results):
        results_window = tk.Toplevel(self)
        results_window.title("Search Results")
        results_text = scrolledtext.ScrolledText(results_window, height=15, width=60)
        results_text.pack(pady=10)

        for result in results:
            name = result.get('name', 'N/A')
            description = result.get('description', 'No description')
            creation_date = datetime.fromtimestamp(result.get('created', 0)).strftime('%Y-%m-%d %H:%M:%S')
            user = result.get('user', 'Unknown')
            results_text.insert(tk.END, f"Name: {name}\nUser: {user}\nDate: {creation_date}\nDescription: {description}\n\n")

    def close_app(self):
        self.destroy()  # This will close the application

if __name__ == "__main__":
    app = DockerApp()
    app.mainloop()
