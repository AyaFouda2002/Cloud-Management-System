import tkinter as tk
from tkinter import messagebox, Label, Frame, Entry, Canvas, Button, Toplevel
from PIL import Image, ImageTk

# Define the properties for each button
button_properties = [
    {"text": "Create a Virtual Machine", "command": "create_VM", "width": 20, "height": 1},
    # ... add other button properties here
]

class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Login Page')

        # Background image
        self.bg_frame = Image.open('images\\background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')

        # ... [rest of the initialization code for LoginPage]


    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=tk.FLAT,
                                  activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=860, y=420)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=tk.FLAT,
                                  activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)
        self.password_entry.config(show='*')

    def sign_in(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "1234":
            self.show_admin_page()
            self.window.withdraw()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def show_admin_page(self):
        admin_window = tk.Toplevel()
        admin_window.geometry("600x400")
        admin_window.configure(background='#4a7a8c')

        # Create buttons
        self.create_buttons(admin_window, button_properties)


        # Load and set background image
        background_image = Image.open('images\\background1.png')
        background_photo = ImageTk.PhotoImage(background_image)
        admin_window.geometry(f"{background_photo.width()}x{background_photo.height()}")

        background_label = tk.Label(admin_window, image=background_photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = background_photo

        # Welcome label
        welcome_label = tk.Label(admin_window, text="Welcome to Cloud Management System", bg='#4a7a8c', fg='white',
                                 font=('Helvetica', 16))
        welcome_label.pack(pady=10)

        # Add other admin page elements here...

    def create_buttons(self, admin_window, button_properties):
        for prop in button_properties:
            button_font = ("Helvetica", 12, "underline")
            command = getattr(self, prop["command"])  # Retrieve method from the class

            btn = tk.Button(admin_window, text=prop["text"],
                            command=lambda cmd=command: cmd(),
                            width=prop["width"], height=prop["height"], font=button_font,
                            bg="#4a7a8c", fg="white")
            btn.pack(pady=10)

    # Define command methods for buttons
    def create_VM():
        print("Enter the details for creating a new Virtual Machine in QEMU:")
        vm_name = input("Enter the name of the VM: ")
        image_file = input("Enter the path to the disk image (e.g., /path/to/image.qcow2): ")
        os_type = input("Enter the type of operating system (e.g., linux, windows): ")
        cpu_cores = input("Enter the number of CPU cores: ")
        memory = input("Enter the amount of RAM in MB (e.g., 1024 for 1GB): ")
        network_model = input("Enter the network model (e.g., user, bridge): ")
        qemu_command = f"qemu-system-x86_64 -name {vm_name} -m {memory} -smp cores={cpu_cores} -drive file={image_file},format=qcow2"
        if os_type.lower() == 'windows':
            qemu_command += " -enable-kvm"
            qemu_command += f" -net {network_model}"
            print("\nQEMU Command to Run VM:")
            print(qemu_command)
            # Run the QEMU command to start the VM
        try:
            subprocess.run(qemu_command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while starting the VM: {e}")
            return
        print("\nVM has been started.")
    # Create a new window
    vm_window = tk.Toplevel()
    vm_window.title("Create Virtual Machine")
    vm_window.geometry("400x300")

    # Entry for VM name
    tk.Label(vm_window, text="VM Name:").grid(row=0, column=0, padx=10, pady=10)
    entry_vm_name = tk.Entry(vm_window)
    entry_vm_name.grid(row=0, column=1, padx=10, pady=10)
    pass


def create_dockerfile():
    path = input("Enter the full path to save the Dockerfile (including the filename): ")

    # Check if the directory exists, and create it if it doesn't
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    print("Enter the Dockerfile content (use 'Ctrl+D' on a new line to finish input):")
    content = []
    while True:
        try:
            line = input()
            content.append(line)
        except EOFError:
            break

    # Join the lines of content and write it to the specified path
    content = '\n'.join(content)
    
    with open(path, "w+") as writer:
        writer.write(content)

    print(f"Dockerfile created at {path}")
    


    """try:
        with open(path, 'w') as file:
            file.write(content)
        print(f"Dockerfile created at {path}")
    except IOError as e:
        print(f"An error occurred: {e}")


        FROM python:3.8-slim
WORKDIR /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
ENV NAME World
CMD ["python", "./app.py"]




        """


def build_image(client):
    dockerfile_path = input("Enter the path to the Dockerfile: ")
    dockerfile_name = input("Enter the name of the Dockerfile (e.g., aya.dockerfile): ")
    tag = input("Enter the image name/tag: ")
    image, logs = client.images.build(path=dockerfile_path, dockerfile=dockerfile_name, tag=tag)
    for log in logs:
        print(log)
    print(f"Image {tag} built successfully.")


def list_images(client):  # Pass 'client' as an argument
    for image in client.images.list():
        print(image.tags)

def list_containers(client):  # Pass 'client' as an argument
    for container in client.containers.list(all=True):
        print(container.name)

def stop_container(client):  # Pass 'client' as an argument
    container_name = input("Enter the container name to stop: ")
    container = client.containers.get(container_name)
    container.stop()
    print(f"Container {container_name} stopped.")

def search_image(client):  # Pass 'client' as an argument
    image_name = input("Enter the image name to search: ")
    images = client.images.list(name=image_name)
    for image in images:
        print(image.tags)

def search_image_dockerhub(client):  # Pass 'client' as an argument
    image_name = input("Enter the image name to search on DockerHub: ")
    results = client.images.search(term=image_name)
    for result in results:
        print(result['name'])

def pull_image(client):  # Pass 'client' as an argument
    image_name = input("Enter the image name to pull: ")
    image = client.images.pull(image_name)
    print(f"Image {image.tags} pulled successfully.")

def create_virtual_machine():
    print("Functionality to create a virtual machine is not implemented.")

def is_valid_file_path(path):
    return os.path.exists(path)

    # ... [define other methods for commands]

def page():
    window = tk.Tk()
    LoginPage(window)
    window.mainloop()

if __name__ == '__main__':
    page()
