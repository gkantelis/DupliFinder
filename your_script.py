import os
import difflib
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from collections import defaultdict

class CustomDialog(tk.Toplevel):

    def __init__(self, parent, message, options):
        tk.Toplevel.__init__(self, parent)

        self.title("File Deletion")
        self.geometry('400x200')
        
        tk.Label(self, text=message).pack(pady=10)
        
        self.var = tk.StringVar(self)
        self.var.set(options[0]) # default value

        self.dropdown = tk.OptionMenu(self, self.var, *options)
        self.dropdown.pack(pady=10)

        tk.Button(self, text="Delete", command=self.ok).pack(pady=10)

    def ok(self):
        self.user_input = self.var.get()
        self.destroy()

def find_similar_files(directory, similarity_threshold):
    files_dict = defaultdict(list)

    for root, dirs, files in os.walk(directory):
        for file in files:
            files_dict[file.lower().split('.')[0]].append(os.path.join(root, file))

    similar_files = [file_group for file_group in files_dict.values() if len(file_group) > 1]

    return similar_files

def main():
    root = tk.Tk()
    root.withdraw()

    similarity_threshold = simpledialog.askfloat("Similarity Threshold", 
                                                 "Please set the similarity threshold (0.1 - 1.0):",
                                                 initialvalue=0.85,
                                                 minvalue=0.1, 
                                                 maxvalue=1.0)

    directory = filedialog.askdirectory()
    similar_files = find_similar_files(directory, similarity_threshold)

    if not similar_files:
        messagebox.showinfo("Result", "No similar files found in the selected directory.")
        return

    for file_group in similar_files:
        message = f"Similar files found: {' , '.join(file_group)}"
        options = file_group + ["None"]

        dialog = CustomDialog(root, message, options)
        root.wait_window(dialog)

        user_input = dialog.user_input
        if user_input and user_input != "None" and os.path.exists(user_input):
            os.remove(user_input)
            messagebox.showinfo("Success", f"File {user_input} deleted successfully!")

if __name__ == "__main__":
    main()
