import customtkinter


class MyApp:
    def __init__(self):
        self.app = customtkinter.CTk()
        self.app.title("JAPC - Just Another Proxy Checker")
        self.app.geometry("800x600")
        self.app._set_appearance_mode("dark")
        self.setup_widgets()
        self.app.maxsize(width=800, height=600)
        self.app.minsize(width=800, height=600)

    def setup_widgets(self):
        self.setup_run_button()
        self.setup_choose_file_button()
        self.setup_load_to_pane_button()
        self.setup_clear_file_button()
        self.setup_textbox()

    def setup_run_button(self):
        self.run_button = customtkinter.CTkButton(
            self.app,
            text="Run Checker",
            bg_color="#242424",
            fg_color="#F8EF00",
            text_color="black",
            font=("Tommorow", 16, "bold"),
            hover_color="#FFFF33",
            command=self.button_callback,
        )
        self.run_button.place(x=175, y=515)

    def setup_choose_file_button(self):
        self.choose_file_button = customtkinter.CTkButton(
            self.app,
            text="Choose File",
            bg_color="#242424",
            fg_color="#51E0E9",
            text_color="black",
            font=("Tommorow", 16, "bold"),
            hover_color="#97f3f8",
            command=self.button_callback,
        )
        self.choose_file_button.place(x=550, y=225)

    def setup_load_to_pane_button(self):
        self.load_to_pane_button = customtkinter.CTkButton(
            self.app,
            text="Load to Pane",
            bg_color="#242424",
            fg_color="#FFFFFF",
            text_color="black",
            font=("Tommorow", 16, "bold"),
            hover_color="#F2F2F2",
            command=self.button_callback,
        )
        self.load_to_pane_button.place(x=550, y=263)

    def setup_clear_file_button(self):
        self.clear_file_Button = customtkinter.CTkButton(
            self.app,
            text="Clear File",
            bg_color="#242424",
            fg_color="#F8EF00",
            text_color="black",
            font=("Tommorow", 16, "bold"),
            hover_color="#FFFF33",
            command=self.button_callback,
        )
        self.clear_file_Button.place(x=550, y=300)

    def setup_textbox(self):
        self.CkTextbox = customtkinter.CTkTextbox(self.app, width=400, height=400)
        self.CkTextbox.place(x=50, y=90)

    def button_callback(self):
        print("button pressed")

    def run(self):
        self.app.mainloop()


if __name__ == "__main__":
    my_app = MyApp()
    my_app.run()
