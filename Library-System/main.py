# This program has been created by Selim Eren Kaya.
# This program provides a library system that stores the books we have read.
# Anyone who wants to use it can use it however they want.

# Importing required packages
import subprocess
import sys
import os
import sqlite3
from tkinter import ttk
import tkinter as tk

# Checks if packages are available
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'customtkinter'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pillow'])
from PIL import Image
import customtkinter as ctk


# Creating App
class App(ctk.CTk):
    def __init__(self):

        # Settings
        super().__init__()
        self.book_name = ctk.StringVar()
        self.author_name = ctk.StringVar()
        self.number_of_pages = ctk.IntVar()
        self.book_list: list = list()

        # Window Settings
        # Window Title
        self.title("Library System")

        # Window Size
        self.window_width = 900
        self.window_height = 600
        self.geometry(f"{self.window_width}x{self.window_height}")
        self.resizable(False, False)

        # Window Background Image
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.background_image = ctk.CTkImage(Image.open(current_path + "/background_image.jpg"),
                                             size=(self.window_width, self.window_height))
        self.background_image_label = ctk.CTkLabel(self, text="", image=self.background_image)
        self.background_image_label.grid(row=0, column=0)

        # Menu Settings
        # Menu Frame
        self.menu = ctk.CTkFrame(self, corner_radius=0)
        self.menu.grid(column=0, row=0, sticky="ns")

        # Menu Titles
        self.menu_title = ctk.CTkLabel(self.menu, text="Library System", font=("Adobe Devanagari", 24))
        self.menu_title.grid(row=0, column=0, padx=30, pady=(0, 15))

        self.menu_choose = ctk.CTkLabel(self.menu, text="Choose Option", font=("Adobe Devanagari", 16))
        self.menu_choose.grid(row=0, column=0, padx=30, pady=(120, 15))

        # Menu Buttons
        # Show Book List Button
        self.show_books_button = ctk.CTkButton(self.menu, text="Show Book List", font=("Adobe Devanagari", 15),
                                               corner_radius=15, width=250, command=lambda: self.show_book_interface())
        self.show_books_button.grid(row=0, column=0, padx=30, pady=(180, 0))

        # Add Book to List Button
        self.add_books_button = ctk.CTkButton(self.menu, text="Add Book to List", font=("Adobe Devanagari", 15),
                                              corner_radius=15, width=250, command=lambda: self.add_book_interface())
        self.add_books_button.grid(row=0, column=0, padx=30, pady=(270, 0))

        # Delete Book from List Button
        self.del_books_button = ctk.CTkButton(self.menu, text="Delete Book from List", font=("Adobe Devanagari", 15),
                                              corner_radius=15, width=250, command=lambda: self.del_book_interface())
        self.del_books_button.grid(row=0, column=0, padx=30, pady=(360, 0))

        # Database Settings
        # Checks if database is available else creating it
        self.con = sqlite3.connect("library.db")
        self.cursor = self.con.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Book_List (Book_Name TEXT, Author_Name TEXT,"
                            " Number_of_Pages INT)")

        # Starts the app
        self.mainloop()

    # Show Book List Functions
    # 1 - Menu Interface Function
    def show_book_interface(self):
        # Clearing the interface of the previous menu
        self.menu_title.grid_forget()
        self.menu_choose.grid_forget()
        self.show_books_button.grid_forget()
        self.add_books_button.grid_forget()
        self.del_books_button.grid_forget()

        # Get Book List from Library Database
        self.book_list = list(self.cursor.execute("SELECT * FROM Book_List"))

        # Creating new menu interface
        # Title of menu
        menu_title = ctk.CTkLabel(self.menu, text="Book List", font=("Adobe Devanagari", 24))
        menu_title.grid(row=0, column=0, padx=10, pady=(50, 0), sticky="n")

        # Book List Frame
        frame = ctk.CTkFrame(self.menu, width=500, height=360)
        frame.grid(row=0, column=0, padx=20, pady=(70, 0))

        scrollbar = ctk.CTkScrollbar(frame)
        scrollbar.pack(side="right", fill="y")

        # Tree View for Book List
        column_headings: list = ["Book Name", "Author Name", "Number of Pages"]
        tree_view = ttk.Treeview(frame, show="headings", yscrollcommand=scrollbar.set,
                                 columns=column_headings, height=15, style="CTK.TLabel")
        tree_view.pack(padx=15, pady=15)

        scrollbar.configure(command=tree_view.yview())

        # Tree View Headings
        tree_view.column("Book Name", width=180)
        tree_view.heading("Book Name", text="Book Name")

        tree_view.column("Author Name", width=150)
        tree_view.heading("Author Name", text="Author Name")

        tree_view.column("Number of Pages", width=150, anchor="center")
        tree_view.heading("Number of Pages", text="Number of Pages")

        # Inserting Book List values into Tree View
        for value_tuple in self.book_list:
            tree_view.insert("", tk.END, values=value_tuple)

        # Back to Main Menu Button
        back_main_menu_button = ctk.CTkButton(self.menu, text="Back to Main Menu",
                                              font=("Adobe Devanagari", 15), width=150, corner_radius=15,
                                              command=lambda: self.return_to_main_menu(menu_title, frame, tree_view,
                                                                                       back_main_menu_button))
        back_main_menu_button.grid(row=0, column=0, padx=30, pady=(530, 0), sticky="n")

    # Add Book to List Functions
    # 1 - Menu Interface Function
    def add_book_interface(self):
        # Clearing the interface of the previous menu
        self.menu_title.grid_forget()
        self.menu_choose.grid_forget()
        self.show_books_button.grid_forget()
        self.add_books_button.grid_forget()
        self.del_books_button.grid_forget()

        # Get Book List from Library Database
        self.book_list = list(self.cursor.execute("SELECT * FROM Book_List"))

        # Creating new menu interface
        # Title of menu
        menu_title = ctk.CTkLabel(self.menu, text="Add Book to List", font=("Adobe Devanagari", 24))
        menu_title.grid(row=0, column=0, padx=10, pady=(100, 0), sticky="n")

        # Menu Info
        menu_info = ctk.CTkLabel(self.menu, text="Fill in the book information", font=("Adobe Devanagari", 16))
        menu_info.grid(row=0, column=0, padx=10, pady=(160, 0), sticky="n")

        # Book Name Entry Section
        book_name_entry = ctk.CTkEntry(self.menu, placeholder_text="Book Name",
                                       font=("Adobe Devanagari", 15), width=200, corner_radius=16)
        book_name_entry.grid(row=0, column=0, padx=30, pady=(190, 0), sticky="n")

        # Author Name Entry Section
        author_name_entry = ctk.CTkEntry(self.menu, placeholder_text="Author Name",
                                         font=("Adobe Devanagari", 15), width=200, corner_radius=16)
        author_name_entry.grid(row=0, column=0, padx=30, pady=(230, 0), sticky="n")

        # Number of Pages Entry Section
        number_pages_entry = ctk.CTkEntry(self.menu, placeholder_text="Number of Pages",
                                          font=("Adobe Devanagari", 15), width=200, corner_radius=16)
        number_pages_entry.grid(row=0, column=0, padx=30, pady=(270, 0), sticky="n")

        # Add Book to List Button
        add_button = ctk.CTkButton(self.menu, text="Confirm and Add", font=("Adobe Devanagari", 15),
                                   width=150, corner_radius=15,
                                   command=lambda: self.add_book_function(book_name_entry,
                                                                          author_name_entry,
                                                                          number_pages_entry))
        add_button.grid(row=0, column=0, padx=30, pady=(320, 0), sticky="n")

        # Back to Main Menu Button
        back_main_menu_button = ctk.CTkButton(self.menu, text="Back to Main Menu",
                                              font=("Adobe Devanagari", 15), width=150, corner_radius=15,
                                              command=lambda: self.return_to_main_menu(menu_title, menu_info,
                                                                                       book_name_entry,
                                                                                       author_name_entry,
                                                                                       number_pages_entry,
                                                                                       add_button,
                                                                                       back_main_menu_button))
        back_main_menu_button.grid(row=0, column=0, padx=30, pady=(440, 0), sticky="n")

    # 2 - Add Book Function
    def add_book_function(self, book_name, author_name, number_of_pages):
        try:
            # Get Book List from Library Database
            self.book_list = list(self.cursor.execute("SELECT * FROM Book_List"))

            int(number_of_pages.get())
            for i in self.book_list:
                if i[0].lower() == book_name.get().lower() and i[1].lower() == author_name.get().lower():
                    # Result Message
                    process = ctk.CTkLabel(self.menu, text="The book is\nalready on the list",
                                           font=("Adobe Devanagari", 20),
                                           text_color="#FF0000")
                    process.grid(row=0, column=0, padx=30, pady=(380, 0), sticky="n")
                    process.after(3000, lambda: process.destroy())
                    break
            else:
                self.cursor.execute("INSERT INTO Book_List VALUES(?, ?, ?)", (book_name.get(), author_name.get(),
                                                                              number_of_pages.get(),))
                self.con.commit()

                # Result Message
                process = ctk.CTkLabel(self.menu, text="Successfully Added", font=("Adobe Devanagari", 20),
                                       text_color="#00FF00")
                process.grid(row=0, column=0, padx=30, pady=(380, 0), sticky="n")
                process.after(3000, lambda: process.destroy())
        except Exception as e:
            # Result Message
            process = ctk.CTkLabel(self.menu, text="Can't Be Added\n"
                                                   "Please enter correct information type",
                                   font=("Adobe Devanagari", 20),
                                   text_color="#FF0000")
            process.grid(row=0, column=0, padx=30, pady=(380, 0), sticky="n")
            process.after(3000, lambda: process.destroy())
            print(e)

    # Delete Book from List Functions
    # 1 - Menu Interface Function
    def del_book_interface(self):
        # Clearing the interface of the previous menu
        self.menu_title.grid_forget()
        self.menu_choose.grid_forget()
        self.show_books_button.grid_forget()
        self.add_books_button.grid_forget()
        self.del_books_button.grid_forget()

        # Creating new menu interface
        # Title of menu
        menu_title = ctk.CTkLabel(self.menu, text="Delete Book from List", font=("Adobe Devanagari", 24))
        menu_title.grid(row=0, column=0, padx=10, pady=(100, 0), sticky="n")

        # Menu Info
        menu_info = ctk.CTkLabel(self.menu, text="Fill in the book information", font=("Adobe Devanagari", 16))
        menu_info.grid(row=0, column=0, padx=10, pady=(160, 0), sticky="n")

        # Book Name Entry Section
        book_name_entry = ctk.CTkEntry(self.menu, placeholder_text="Book Name",
                                       font=("Adobe Devanagari", 15), width=200, corner_radius=16)
        book_name_entry.grid(row=0, column=0, padx=30, pady=(190, 0), sticky="n")

        # Author Name Entry Section
        author_name_entry = ctk.CTkEntry(self.menu, placeholder_text="Author Name",
                                         font=("Adobe Devanagari", 15), width=200, corner_radius=16)
        author_name_entry.grid(row=0, column=0, padx=30, pady=(230, 0), sticky="n")

        # Delete Book from List Button
        del_button = ctk.CTkButton(self.menu, text="Confirm and Delete", font=("Adobe Devanagari", 15),
                                   width=150, corner_radius=15, command=lambda: self.del_book_function(book_name_entry,
                                                                                                       author_name_entry
                                                                                                       ))
        del_button.grid(row=0, column=0, padx=30, pady=(280, 0), sticky="n")

        # Back to Main Menu Button
        back_main_menu_button = ctk.CTkButton(self.menu, text="Back to Main Menu",
                                              font=("Adobe Devanagari", 15), width=150, corner_radius=15,
                                              command=lambda: self.return_to_main_menu(menu_title, menu_info,
                                                                                       book_name_entry,
                                                                                       author_name_entry,
                                                                                       del_button,
                                                                                       back_main_menu_button))
        back_main_menu_button.grid(row=0, column=0, padx=30, pady=(440, 0), sticky="n")

    # 2 - Delete Book Function
    def del_book_function(self, book_name, author_name):
        # Get Book List from Library Database
        self.book_list = list(self.cursor.execute("SELECT * FROM Book_List"))

        is_process_successful = False
        try:
            for i in self.book_list:
                if i[0].lower() == book_name.get().lower() and i[1].lower() == author_name.get().lower():
                    self.cursor.execute("DELETE FROM Book_List WHERE Book_Name = ? AND Author_Name = ?",
                                        (i[0], i[1], ))  # i[0] equals Book Name and i[1] equals Author Name
                    self.con.commit()

                    # Result Message
                    process = ctk.CTkLabel(self.menu, text="Successfully Deleted", font=("Adobe Devanagari", 20),
                                           text_color="#00FF00")
                    process.grid(row=0, column=0, padx=30, pady=(380, 0), sticky="n")
                    process.after(3000, lambda: process.destroy())
                    is_process_successful = True
                    break
            if not is_process_successful:
                # Result Message
                process = ctk.CTkLabel(self.menu, text="Can't Be Deleted\n"
                                                       "There is no book with this information",
                                       font=("Adobe Devanagari", 20),
                                       text_color="#FF0000")
                process.grid(row=0, column=0, padx=30, pady=(380, 0), sticky="n")
                process.after(3000, lambda: process.destroy())
        except Exception as e:
            # Result Message
            process = ctk.CTkLabel(self.menu, text="Can't Be Deleted\n"
                                                   "Please enter correct information type",
                                   font=("Adobe Devanagari", 20),
                                   text_color="#FF0000")
            process.grid(row=0, column=0, padx=30, pady=(380, 0), sticky="n")
            process.after(3000, lambda: process.destroy())
            print(e)

    # Returning to Main Menu Function
    def return_to_main_menu(self, *grids):
        # Clean-up Add Book Menu
        for i in grids:
            i.grid_forget()

        # Make Main Menu Visible
        self.menu_title.grid(row=0, column=0, padx=30, pady=(0, 15))
        self.menu_choose.grid(row=0, column=0, padx=30, pady=(120, 15))
        self.show_books_button.grid(row=0, column=0, padx=30, pady=(180, 0))
        self.add_books_button.grid(row=0, column=0, padx=30, pady=(270, 0))
        self.del_books_button.grid(row=0, column=0, padx=30, pady=(360, 0))


App()
