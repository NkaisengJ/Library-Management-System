import tkinter as tk
from tkinter import PhotoImage, messagebox
from BooksDB import book_database
from MembersDB import member_database
import os

BooksDB = book_database('Books.db')
MembersDB = member_database('Members.db')

# The main window
root = tk.Tk()
root.title("LBMMS")
root.geometry("728x410")

# function to add background image to the given window
def set_background(window, image_name):

    # Load the background image
    image_path = os.path.join(os.path.dirname(__file__), image_name)
    background1_image = PhotoImage(file="back-tk.png")

    # Create a Label to hold the background image
    background1_label = tk.Label(window, image=background1_image)
    background1_label.image = background1_image  # Keep a reference to avoid garbage collection
    background1_label.place(relwidth=1, relheight=1)



# Functions to callback for buttons
def add_book():
    root1 = tk.Toplevel()
    root1.title("Add Book")
    root1.geometry("800x450")

    set_background(root1, "back-tk.png")


    label_title = tk.Label(root1, text='Title:', font=('Ariel', 15, 'bold'), fg='green', bg='white')
    label_title.pack()
    entry_title = tk.Entry(root1, font=('Ariel', 14))
    entry_title.pack()

    label_author = tk.Label(root1, text='Author:', font=('Ariel', 15, 'bold'), fg='green', bg='white')
    label_author.pack()
    entry_author = tk.Entry(root1, font=('Ariel', 14))
    entry_author.pack()

    label_isbn = tk.Label(root1, text='ISBN:', font=('Ariel', 15, 'bold'), fg='green', bg='white')
    label_isbn.pack()
    entry_isbn = tk.Entry(root1, font=('Ariel', 14))
    entry_isbn.pack()

    label_genre = tk.Label(root1, text='Genre:', font=('Ariel', 15, 'bold'), fg='green', bg='white')
    label_genre.pack()
    entry_genre = tk.Entry(root1, font=('Ariel', 14))
    entry_genre.pack()

    label_availability = tk.Label(root1, text='Availability:', font=('Ariel', 15, 'bold'), fg='green', bg='white')
    label_availability.pack()
    entry_availability = tk.Entry(root1, font=('Ariel', 14))
    entry_availability.pack()




    def addB():
        title = entry_title.get().strip()
        author = entry_author.get().strip()
        isbn = entry_isbn.get().strip()
        genre = entry_genre.get().strip()
        availability = entry_availability.get().strip()

        if BooksDB.check_isbn_exists(isbn):
            messagebox.showerror("Duplicate ISBN", "A book with this ISBN already exists.")
            return
        if BooksDB.check_title_exists(title):
            messagebox.showerror("Duplicate Name", "A book with this Name already exists.")
            return
        if not title or not author or not isbn:
            messagebox.showerror("Missing Data", "Please fill in all required fields.")
            return

        BooksDB.add_book(title, author, isbn, genre, availability)
        messagebox.showinfo("Success", "Book added successfully!")
        root1.destroy()

    def deleteB():
        isbn = entry_isbn.get().strip()
        if not isbn.isdigit():
            messagebox.showerror("Invalid Input", "ISBN must be numeric.")
            return

        BooksDB.delete_book(isbn)
        messagebox.showinfo("Success", "Book deleted successfully.")
        root1.destroy()

    def updateB():

        title = entry_title.get().strip()
        author = entry_author.get().strip()
        isbn = entry_isbn.get().strip()
        genre = entry_genre.get().strip()
        availability = entry_availability.get().strip()

        if not isbn.isdigit():
            messagebox.showerror("Invalid Input", "ISBN must be numeric.")
            return

        BooksDB.update_book(isbn, title, author, isbn, genre, availability)
        messagebox.showinfo("Success", "Book updated successfully.")
        root1.destroy()


    add_btn = tk.Button(root1, text="Add", command=addB, font=('Calibri', 9), width=10, height=2,
                        relief="raised", bd=5)
    add_btn.pack(side=tk.LEFT, padx=5, pady=7)

    delete_btn = tk.Button(root1, text="Delete", command=deleteB, font=('Calibri', 9), width=10, height=2,
                           relief="raised", bd=5)
    delete_btn.pack(side=tk.LEFT, padx=5, pady=7)

    update_btn = tk.Button(root1, text="Update", command=updateB, font=('Calibri', 9), width=10, height=2,
                           relief="raised", bd=5)
    update_btn.pack(side=tk.LEFT, padx=5, pady=7)



def member_info():
    root2 = tk.Toplevel()
    root2.title("Member Info")
    root2.geometry("728x410")

    set_background(root2, "back-tk.png")

    def addM():
        id_member = entry_id.get().strip()
        name = entry_name.get().strip()
        phone = entry_phone.get().strip()

        if not id_member.isdigit():
            messagebox.showerror("Invalid Input", "Member ID must be numeric.")
            return
        if not name:
            messagebox.showerror("Missing Name", "Name cannot be empty.")
            return

        MembersDB.add_member(id_member, name, phone)
        messagebox.showinfo("Success", "Member added successfully.")
        root2.destroy()

    def deleteM():
        id_member = entry_id.get().strip()
        if not id_member.isdigit():
            messagebox.showerror("Invalid Input", "Member ID must be numeric.")
            return

        MembersDB.delete_member(id_member)
        messagebox.showinfo("Success", "Member deleted successfully.")
        root2.destroy()

    def updateM():
        id_member = entry_id.get().strip()
        name = entry_name.get().strip()
        phone = entry_phone.get().strip()

        if not id_member.isdigit():
            messagebox.showerror("Invalid Input", "Member ID must be numeric.")
            return

        MembersDB.update_member(id_member, name, phone)
        messagebox.showinfo("Success", "Member updated successfully.")
        root2.destroy()

    def searchM():
        member_lookingFor = entry_search.get().strip()
        if not member_lookingFor.isdigit():
            messagebox.showerror("Invalid Input", "Member ID must be numeric.")
            return
        member = MembersDB.search_member_by_id(member_lookingFor)
        if member:
            messagebox.showinfo("Member Found", f"Name: {member[1]}\nPhone: {member[2]}")
        else:
            messagebox.showerror("Member Not Found", "Member not found in the database.")

    add_btn = tk.Button(root2, text="Add", command=addM, font=('Calibri', 9), width=10, height=2,
                        relief="raised", bd=5)
    add_btn.pack(side=tk.LEFT, padx=5, pady=7)

    delete_btn = tk.Button(root2, text="Delete", command=deleteM, font=('Calibri', 9), width=10,
                           height=2,
                           relief="raised", bd=5)
    delete_btn.pack(side=tk.LEFT, padx=5, pady=7)

    update_btn = tk.Button(root2, text="Update", command=updateM, font=('Calibri', 9), width=10,
                           height=2,
                           relief="raised", bd=5)
    update_btn.pack(side=tk.LEFT, padx=5, pady=7)

    search_btn = tk.Button(root2, text="Search", command=searchM, font=('Calibri', 9), width=10,
                           height=2,
                           relief="raised", bd=5)
    search_btn.pack(side=tk.LEFT, padx=5, pady=7)



    label_id = tk.Label(root2, text='Member ID:', font=('Ariel', 15, 'bold'), fg='green', bg='white')
    label_id.pack()
    entry_id = tk.Entry(root2, font=('Ariel', 14))
    entry_id.pack()

    label_name = tk.Label(root2, text='Name:', font=('Ariel', 15, 'bold'), fg='green', bg='white')
    label_name.pack()
    entry_name = tk.Entry(root2, font=('Ariel', 14))
    entry_name.pack()

    label_phone = tk.Label(root2, text='Phone:', font=('Ariel', 15, 'bold'), fg='green', bg='white')
    label_phone.pack()
    entry_phone = tk.Entry(root2, font=('Ariel', 14))
    entry_phone.pack()

    label_search = tk.Label(root2, text='Search by Name:', font=('Ariel', 15, 'bold'), fg='green', bg='white')
    label_search.pack()
    entry_search = tk.Entry(root2, font=('Ariel', 14))
    entry_search.pack()

    button_frame = tk.Frame(root2, bg='white')
    button_frame.pack(pady=(10, 0))



def view_library():
    root3 = tk.Toplevel()
    root3.title("View Library")
    root3.geometry("728x410")

    set_background(root3, "back-tk.png")

    def searchB():
        book_lookingFor = entry_search.get().strip()
        if not book_lookingFor.isdigit():
            messagebox.showerror("Invalid Input", "Book ISBN must be numeric.")
            return
        book = BooksDB.search_book_by_id(book_lookingFor)
        if book:
            messagebox.showinfo("Book Found", f"Title: {book[1]}\nAuthor: {book[2]}\nISBN: {book[3]}\nGenre: {book[4]}\nAvailability: {book[5]}")
        else:
            messagebox.showerror("Book Not Found", "Book not found in the database.")

    label_search = tk.Label(root3, text='Search by ISBN:', font=('Ariel', 15, 'bold'), fg='green', bg='white')
    label_search.pack(side=tk.TOP)
    entry_search = tk.Entry(root3, font=('Ariel', 14))
    entry_search.pack(side=tk.TOP)

    search_btn = tk.Button(root3, text="Search", command=searchB, font=('Calibri', 9), width=10, height=2,
                           relief="raised", bd=5)
    search_btn.pack(side=tk.LEFT, padx=5, pady=7)


    displayB = tk.Listbox(root3, width=100, height=20)
    displayB.pack(pady=10, padx=10)

    books = BooksDB.get_all_books()
    for book in books:
        displayB.insert(tk.END,f" Title: {book[0]} - Author: {book[1]} - ISBN: {book[2]} - Genre: {book[3]} - Availability: {book[4]}")

def view_members():
    root4 = tk.Toplevel()
    root4.title("View Members")
    root4.geometry("728x410")

    set_background(root4, "back-tk.png")

    displayM = tk.Listbox(root4, width=100, height=20)
    displayM.pack(pady=10, padx=10)

    members = MembersDB.get_all_members()
    for member in members:
        displayM.insert(tk.END, f"ID: {member[0]} - Name: {member[1]} - Phone: {member[2]}")

def exit_application():
    answer = messagebox.askquestion('Exit', 'Are you sure you want to exit this program?')
    if answer == 'yes':
        root.destroy()
    else:
        messagebox.showinfo('Stay in application', 'You have chosen to stay in the application')

# Displays the background image
background_image = PhotoImage(file="good.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Create a frame to hold the labels and buttons
frame = tk.Frame(root, bg='white')
frame.place(relx=0.5, rely=0.5, anchor='center')

# Labels
welcome_label = tk.Label(frame, text="Welcome to Belgium Library System", font=('Arial', 15, 'bold'),
                         fg='brown', bg='white')
welcome_label.pack(pady=(10, 0))

message_label = tk.Label(frame, text="Your access to library resources", font=('Arial', 15, 'italic'),
                         fg='brown', bg='white')
message_label.pack(pady=(5, 0))

final_label = tk.Label(frame, text="Choose options below to get started:", font=('Arial', 9, 'italic'),
                       fg='brown', bg='white')
final_label.pack(pady=(5, 15))

# Create a frame for buttons to center them
button_frame = tk.Frame(frame, bg='white')
button_frame.pack(pady=(10, 0))

# Create buttons
add_book_button = tk.Button(button_frame, text="Add Book", command=add_book, font=("Times New Roman", 9),
                            fg='brown', bg='white', width=10, height=2, relief="raised", bd=5)
add_book_button.pack(side=tk.LEFT, padx=10)

member_info_button = tk.Button(button_frame, text="Member Info", command=member_info,
                               font=("Times New Roman", 9), fg='brown', bg='white', width=10, height=2,
                               relief="raised", bd=5)
member_info_button.pack(side=tk.LEFT, padx=10)

view_library_button = tk.Button(button_frame, text="View Library", command=view_library,
                                font=("Times New Roman", 9), fg='brown', bg='white', width=10, height=2,
                                relief="raised", bd=5)
view_library_button.pack(side=tk.LEFT, padx=10)

view_members_button = tk.Button(button_frame, text="View Members", command=view_members,
                                font=("Times New Roman", 9), fg='brown', bg='white', width=10, height=2,
                                relief="raised", bd=5)
view_members_button.pack(side=tk.LEFT, padx=10)

exit_button = tk.Button(button_frame, text="Exit", command=exit_application, font=("Times New Roman", 9),
                        fg='brown', bg='white', width=10, height=2, relief="raised", bd=5)
exit_button.pack(side=tk.LEFT, padx=10)

root.mainloop()