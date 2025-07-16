import os
from tkinter import *
from tkinter import filedialog
import test2
job="test"

class DocxBrowser:
    # Initializes the first window for the GUI and sets up the title for it
    def __init__(self, root):
        self.root = root
        self.root.title("Resume Job Finder")
        self.current_dir = os.getcwd()
        self.selected_file = None
        self.frame1 = Frame(root)
        self.frame2 = None
        self.frame1.pack(fill=BOTH, expand=True)
        #sets up buttons and labels for the window
        self.label = Label(self.frame1, text=f"Current Directory:\n{self.current_dir}")
        self.label.pack(pady=5)
        self.listbox = Listbox(self.frame1, width=50)
        self.listbox.pack(padx=10, pady=5)
        self.open_button = Button(self.frame1, text="Change Directory", command=self.change_directory)
        self.open_button.pack(pady=5)
        self.next_button = Button(self.frame1, text="Next", command=self.go_to_next_screen)
        self.next_button.pack(pady=10)
        self.refresh_file_list()
    # Displays file select screen once you exit from the results shown on resume
    def show_file_select_screen(self):
        # Gets rid of previous frame and then reverts back to initial one
        self.frame2.destroy()
        self.frame1 = Frame(self.root)
        self.frame1.pack(fill=BOTH, expand=True)
        self.label = Label(self.frame1, text=f"Current Directory:\n{self.current_dir}")
        self.label.pack(pady=5)
        self.listbox = Listbox(self.frame1, width=50)
        self.listbox.pack(padx=10, pady=5)
        self.open_button = Button(self.frame1, text="Change Directory", command=self.change_directory)
        self.open_button.pack(pady=5)
        self.next_button = Button(self.frame1, text="Next", command=self.go_to_next_screen)
        self.next_button.pack(pady=10)
        self.refresh_file_list()


    # Changes the files displayed once you switch directories
    def refresh_file_list(self):
        self.listbox.delete(0, END)
        try:
            files = os.listdir(self.current_dir)
            docx_files = [f for f in files if f.lower().endswith('.docx')]
            pdf_files = [f for f in files if f.lower().endswith('.pdf')]
            if not docx_files and not pdf_files:
                    self.listbox.insert(END, "No compatible files found.")
            else:
                for file in docx_files:
                    self.listbox.insert(END, file)
                for file in pdf_files:
                    self.listbox.insert(END, file)

        except Exception as e:
            self.listbox.insert(END, f"Error: {e}")

        self.label.config(text=f"Current Directory:\n{self.current_dir}")

    # Changes directory for the first screen based on which file you picked
    def change_directory(self):
        new_dir = filedialog.askdirectory(initialdir=self.current_dir, title="Select a directory")
        if new_dir:
            self.current_dir = new_dir
            self.refresh_file_list()

    # Sets everything up to switch to second screen and makes sure a valid docx file was selected
    def go_to_next_screen(self):
        try:
            selected_index = self.listbox.curselection()
            if not selected_index:
                self.label.config(text="Please select a file before proceeding.")
                return

            filename = self.listbox.get(selected_index)
            self.selected_file = os.path.join(self.current_dir, filename)

            # Gets rid of the first screen and moves on to the job listing
            self.frame1.destroy()
            self.show_next_screen()
        except Exception as e:
            self.label.config(text=f"Error: {e}")

    # Switches to the results after the resume was analyzed and documented
    def show_next_screen(self):
        self.frame2 = Frame(self.root)
        self.frame2.pack(fill=BOTH, expand=True)
        test2.selected_file=self.selected_file
        test2.main()
        job = str(test2.best_match) if test2.best_match else "No match found"
        # Sets up button and text for the second window
        Label(self.frame2, text="You selected this file:", font=("Arial", 14)).pack(pady=10)
        Label(self.frame2, text=self.selected_file, wraplength=500).pack(pady=5)
        Label(self.frame2, text="Recommended Job: ", wraplength=700, font=("Arial", 14), justify="left").pack(pady=10)
        Label(self.frame2, text=str(job), wraplength=700, font=("Arial", 14), justify="left").pack(pady=10)
        Button(self.frame2, text="Back", command=self.show_file_select_screen).pack(pady=20)


# Main thing that runs the GUI and sets the size of the window
window = Tk()
window.geometry("600x300")
app = DocxBrowser(window)
window.mainloop()
