import tkinter as tk
import interface

root3 = tk.Tk()
root3.title("View")
root3.geometry("728x410")

search_label = tk.Label(root3,text="Search", font=('Ariel', 15, 'bold'), fg='green', bg='white')
search_entry=tk.Entry(root3, font=('Ariel', 14))
search_entry.pack(pady=5,padx=5)

search_btn=tk.Button(root3 ,text="Search" ,command="SearchB", font=('Times New Roman',9),width=10, height=2, relief="raised", bd=5)
search_btn.pack(side=tk.LEFT,padx=5, pady=7)