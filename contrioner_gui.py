import tkinter as tk
from tkinter import Toplevel, Canvas, Frame, Scrollbar
import docker

class DockerApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Initialize Docker client
        self.client = docker.from_env()

        # Configure the main window size
        self.geometry('1166x718')  # Width x Height

        # Create a canvas and a scrollbar
        self.canvas = Canvas(self)
        self.scrollbar = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = Frame(self.canvas)

        # Configure the canvas
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Pack everything
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Define colors
        self.color2 = '#264cf5'
        self.color3 = '#1e26c7'
        self.color4 = 'Black'

        # List Docker containers as buttons
        self.list_containers_as_buttons()

        # Add Exit button
        self.exit_button = self.create_button("Exit", self.close_app)
        self.exit_button.pack(fill=tk.X, pady=(10, 5))

    def create_button(self, text, command):
        return tk.Button(self.scrollable_frame,
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
                         font=('Arial', 15, 'bold'),
                         command=command)

    def list_containers_as_buttons(self):
        for container in self.client.containers.list(all=True):
            name = container.name
            button = self.create_button(name, lambda c=container: self.open_container_details(c))
            button.pack(fill=tk.X, pady=(10, 5))

    def open_container_details(self, container):
        details_window = Toplevel(self)
        details_window.title("Container Details")

        details = f"Name: {container.name}\nID: {container.id}\nStatus: {container.status}"
        details_label = tk.Label(details_window, text=details, font=("Arial", 12))
        details_label.pack(pady=20)

    def close_app(self):
        self.destroy()

if __name__ == "__main__":
    app = DockerApp()
    app.mainloop()

