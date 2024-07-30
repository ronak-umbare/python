import tkinter as tk
from tkinter import Entry, Label, Button
import webbrowser

root = tk.Tk()
root.title("RONAK's Assistant")
root.configure(bg='grey')

def youtube():
    query = entry.get()
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

def google():
    query = entry.get()
    url = f"https://www.google.com/?search?q={query}"
    webbrowser.open(url)

def insta():
   username = entry.get().replace('@',"")
   url = f"www.instagram.com/{username}/"
   webbrowser.open(url)
   
Label(root,text = "Enter ur text to search :").pack(pady=10)
entry = Entry(root, width=50)
entry.pack(pady=50)
Button(root, text = "YOUTUBE", command=youtube).pack(pady=5)
Button(root, text = "Google", command=google).pack(pady=5)
Button(root, text = "Instagram", command=insta).pack(pady=5)

root.mainloop()