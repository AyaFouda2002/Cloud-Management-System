import tkinter as tk
from tkinter import Label, Entry
from PIL import Image, ImageTk
import subprocess

global_background_photo = None
class VMCreatorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Load and set background image
        self.background_image_path = "C:\\Users\\ayael\\OneDrive\\Desktop\\Project_cloud\\images\\background1.png"
        self.raw_background_image = Image.open(self.background_image_path)
        self.background_photo = ImageTk.PhotoImage(self.raw_background_image)

        self.geometry(f"{self.background_photo.width()}x{self.background_photo.height()}")

        # Keep a reference to the image to prevent garbage collection
        self.background_label = tk.Label(self, image=self.background_photo)
        self.background_label.image = self.background_photo  # Keep a reference
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Initialize user interface
        self.init_ui()


    def init_ui(self):
        # Define input fields and labels
        self.vm_name_entry = self.create_label_entry("VM Name:", 250, 50, 250, 100)
        self.image_file_entry = self.create_label_entry("Disk Image Path:", 700, 50, 700, 100)
        self.os_type_entry = self.create_label_entry("OS Type:", 250, 150, 250, 200)
        self.cpu_cores_entry = self.create_label_entry("CPU Cores:", 700, 150, 700, 200)
        self.memory_entry = self.create_label_entry("RAM (MB):", 250, 250, 250, 300)
        self.network_model_entry = self.create_label_entry("Network Model:", 700, 250, 700, 300)

        # Create VM button
        self.create_vm_button = tk.Button(self, text="Create VM", command=self.handle_create_vm, bg="#0000FF", fg="white",
                         width=20, height=2, font=("Arial", 20, "bold"))
        self.create_vm_button.place(x=400, y=400)

                # Create Exit button
        self.create_vm_button = tk.Button(self, text="Exit", command=self.handle_create_vm, bg="#0000FF", fg="white",
                         width=15, height=2, font=("Arial", 15, "bold"))
        self.create_vm_button.place(x=480, y=500)

    def create_label_entry(self, text, label_x, label_y, entry_x, entry_y):
        label = Label(self, text=text, font=("Arial", 16, "bold"))
        label.place(x=label_x, y=label_y)
        entry = Entry(self, font=("yu gothic ui", 16, "bold"))

        entry.place(x=entry_x, y=entry_y)
        return entry

    def handle_create_vm(self):
        # Retrieve values from the entry fields
        vm_name = self.vm_name_entry.get()
        image_file = self.image_file_entry.get()
        os_type = self.os_type_entry.get()
        cpu_cores = self.cpu_cores_entry.get()
        memory = self.memory_entry.get()
        network_model = self.network_model_entry.get()

        # Call the VM creation function
        self.create_VM(vm_name, image_file, os_type, cpu_cores, memory, network_model)

    def create_VM(self, vm_name, image_file, os_type, cpu_cores, memory, network_model):
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

# Run the application
if __name__ == "__main__":
    app = VMCreatorApp()
    app.mainloop()

