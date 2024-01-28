from GUIVM import VMCreatorApp
from DOCKERnew import DockerfileCreatorApp
from build_image_gui import DockerImageBuilder
from contrioner_gui import DockerApp
from list_image_gui import DockerApp_list
from pull_image_gui import DockerGUI
from seach_image_local import DockerApp_search
from search_gui import DockerApp_dockerhub
from stop_gui import DockerGUI
import tkinter as tk
from tkinter import messagebox, Label, Frame, Entry, Canvas, Button, Toplevel
from PIL import Image, ImageTk
import customtkinter
from tkinter import ttk

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

        # Login Frame
        self.lgn_frame = Frame(self.window, bg='#040405', width=950, height=600)
        self.lgn_frame.place(x=200, y=70)

        self.txt = "Welcom To Cloud Management System "
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 10, "bold"), bg="#040405",
                             fg='white', bd=10, relief=tk.FLAT)
        self.heading.place(x=80, y=30, width=300, height=30)

        # Left Side Image
        self.side_image = Image.open('images\\vector.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)

        # Sign In Image
        self.sign_in_image = Image.open('images\\hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=130)

        # Sign In label
        self.sign_in_label = Label(self.lgn_frame, text="Sign In", bg="#040405", fg="white",
                                   font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=650, y=240)

        # Username Entry
        self.username_label = Label(self.lgn_frame, text="Username", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=300)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=tk.FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground='#6b6a69')
        self.username_entry.place(x=580, y=335, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=359)

        # Username icon
        self.username_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=332)

        # Login button
        self.lgn_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=450)
        self.login = Button(self.lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',
                            command=self.sign_in)
        self.login.place(x=20, y=10)

        # Forgot password button
        self.forgot_button = Button(self.lgn_frame, text="Forgot Password ?", font=("yu gothic ui", 13, "bold underline"),
                                    fg="white", relief=tk.FLAT, activebackground="#040405", borderwidth=0,
                                    background="#040405", cursor="hand2")
        self.forgot_button.place(x=630, y=510)

        # Sign Up label and button
        self.sign_label = Label(self.lgn_frame, text='No account yet?', font=("yu gothic ui", 11, "bold"),
                                relief=tk.FLAT, borderwidth=0, background="#040405", fg='white')
        self.sign_label.place(x=550, y=560)

        self.signup_img = ImageTk.PhotoImage(file='images\\register.png')
        self.signup_button_label = Button(self.lgn_frame, image=self.signup_img, bg='#98a65d', cursor="hand2",
                                          borderwidth=0, background="#040405", activebackground="#040405")
        self.signup_button_label.place(x=670, y=555, width=111, height=35)

        # Password entry
        self.password_label = Label(self.lgn_frame, text="Password", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=380)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=tk.FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*", insertbackground='#6b6a69')
        self.password_entry.place(x=580, y=416, width=244)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=440)

        # Password icon
        self.password_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=414)

        # Show/hide password
        self.show_image = ImageTk.PhotoImage(file='images\\show.png')
        self.hide_image = ImageTk.PhotoImage(file='images\\hide.png')
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=tk.FLAT,
                                  activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)

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
    # Create the admin window
        admin_window = tk.Toplevel()
        admin_window.geometry("600x400")
        admin_window.configure(background='#4a7a8c')

        # Load and set background image
        background_image = Image.open('images\\background1.png')
        background_photo = ImageTk.PhotoImage(background_image)
        admin_window.geometry(f"{background_photo.width()}x{background_photo.height()}")

        background_label = tk.Label(admin_window, image=background_photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = background_photo

        # Frame to contain buttons, using the correct background color
        frame = tk.Frame(admin_window, bg='#1e1e1f')
        frame.pack(pady=20)  # You might need to adjust this to place the frame where you want it

        color2 = '#264cf5'  # Button text color when not active
        color3 = '#1e26c7'  # Button text color when active
        color4 = 'Black'    # Button background color
        buttons = []
        button_texts = ['Create a Virtual Machine', 'Create Docker File', 'Build Docker Image',
                        'List Docker Images', 'List All Containers', 'Stop a container',
                        'Search Image', 'Search for image on DockerHub', 'Download/Pull image', 'EXIT']
        for text in button_texts:
            button = self.create_button(frame, text, color2, color3, color4)
            button.pack(pady=(10, 5))
            buttons.append(button)

        welcome_label = tk.Label(admin_window, text="Welcome to Cloud Management System", bg='#4a7a8c', fg='white',
                                 font=('Helvetica', 16))
        welcome_label.pack(pady=(10, 5))

    def create_button(self, window, text, background, activebackground, foreground):
        return tk.Button(window,
                         background=background,
                         foreground=foreground,
                         width=100,
                         height=2,
                         highlightthickness=0,
                         highlightbackground=background,
                         highlightcolor='WHITE',
                         activebackground=activebackground,
                         activeforeground=foreground,
                         cursor='hand1',
                         border=0,
                         text=text,
                         font=('Arial', 15, 'bold'))



    def menu_option_selected(self, option, admin_window):
        messagebox.showinfo("Option Selected", f"You selected: {option}")
        admin_window.destroy()
        if option == "Create a Virtual Machine":
            open_vm_creator()
        elif option == "Create Docker File":
            DockerfileCreatorApp()
        elif option == "Build Docker Image":
            DockerImageBuilder()
        elif option == "List Docker Images":
            DockerApp_list()
        elif option == "List All Containers":
            DockerApp()
        elif option == "Stop a container":
            DockerGUI()
        elif option == "Search Image":
            DockerApp_search()
        elif option == "Search for image on DockerHub":
            DockerApp_dockerhub()
        elif option == "Download/Pull image":
            DockerGUI()
        elif option == "EXIT":
            self.window.quit()

    def open_vm_creator(self):
        vm_creator_app = VMCreatorApp()
        vm_creator_app.mainloop()

def page():
    window = tk.Tk()
    LoginPage(window)
    window.mainloop()

if __name__ == '__main__':
    page()
