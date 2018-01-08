try:
    from Tkinter import *
    import tkFont
    import ttk
except ImportError:  # Python 3
    from tkinter import *
    import tkinter.font as tkFont
    import tkinter.ttk as ttk
import finder

class pyFinderGUI:
    def __init__(self, master):

        master.title("PyFinder")
        self.master_width = 800
        self.master_height = 400
        self.master_padding_x = master.winfo_screenwidth() // 2 - self.master_width // 2
        self.master_padding_y = master.winfo_screenheight() // 2 - self.master_height // 2
        master.resizable(False, False)
        master.geometry('{}x{}+{}+{}'.format(self.master_width, self.master_height,
                                             self.master_padding_x, self.master_padding_y))

        self.frame_welcome = ttk.Frame(master)
        self.frame_welcome.pack()

        ttk.Label(self.frame_welcome, text="Welcome to the PyFinder!  Search through a Python modules content",
                  font=('Corbel', 10, 'bold'), justify=CENTER).pack(pady=5)

        self.frame_settings = ttk.Frame(master, height=120, width=800)
        self.frame_settings.pack()
        self.frame_settings.pack_propagate(0)
        self.frame_settings_left = ttk.Frame(self.frame_settings)
        self.frame_settings_left.pack(side=LEFT)
        self.frame_settings_right = ttk.Frame(self.frame_settings)
        self.frame_settings_right.pack(side=LEFT)

        ttk.Label(self.frame_settings_left, text='Set directory:', font=('Corbel', 10, 'bold')).grid(row=0, column=0, padx=5, sticky='sw')
        ttk.Label(self.frame_settings_left, text='Search for:',font=('Corbel', 10, 'bold')).grid(row=3, column=0, padx=5, sticky='sw')

        self.entry_dir = ttk.Entry(self.frame_settings_left, width=34)
        self.entry_dir.grid(row=1, column=0, padx=5, sticky='sw')

        self.is_dir_label = ttk.Label(self.frame_settings_left, text="No such directory", font=('Corbel', 8))
        self.is_dir_label.grid(row=2, column=0, columnspan=2, padx=5, sticky='se')

        self.entry_term = ttk.Entry(self.frame_settings_left, width=40)
        self.entry_term.grid(row=4, column=0, columnspan=2,  padx=5, sticky='sw')

        self.is_term_label = ttk.Label(self.frame_settings_left, text="Invalid input", font=('Corbel', 8))
        self.is_term_label.grid(row=5, column=0, columnspan=2,  padx=5, sticky='se')

        self.dir_button = ttk.Button(self.frame_settings_left, width=4, text='...')
        self.dir_button.grid(row=1, column=1, sticky='sw')

        self.modules_button = ttk.Button(self.frame_settings_left, width=12, text='Add path ->')
        self.modules_button.grid(row=1, column=2, padx=17, sticky='sw')

        self.search_button = ttk.Button(self.frame_settings_left, width=12, text='Search!')
        self.search_button.grid(row=4, column=2, padx=17, sticky='sw')

        ttk.Label(self.frame_settings_right, text="Found Py modules:", font=('Corbel', 10, 'bold')).grid(row=0, padx=6, column=0, sticky='sw')
        self.dir_checkbox = ttk.Checkbutton(self.frame_settings_right, text="Show root directory")
        self.dir_checkbox.grid(row=0, column=1, padx=6, sticky='se')

        self.modules_box = Listbox(self.frame_settings_right, width=68)
        self.modules_box.grid(row=1, column=0, columnspan=2, padx=6, sticky='sw')

        self.frame_progress = ttk.Frame(master)
        self.frame_progress.pack()
        self.progress_bar = ttk.Progressbar(self.frame_progress, orient=HORIZONTAL, length=700)
        self.progress_bar.grid(row=0, column=0, pady=10, padx=5)

        self.cancel_button = ttk.Button(self.frame_progress, text='Cancel')
        self.cancel_button.grid(row=0, column=1, pady=10, padx=6, sticky='se')

        self.frame_results = ttk.Frame(master)
        self.frame_results.pack()

        self.frame_results_left = ttk.Frame(self.frame_results)
        self.frame_results_left.pack(side=LEFT)
        self.frame_results_right = ttk.Frame(self.frame_results)
        self.frame_results_right.pack(side=LEFT)

        ttk.Label(self.frame_results_left, text='Display:', font=('Corbel', 10, 'bold')).pack(padx=5, pady=5, anchor='sw')
        self.func_button = ttk.Radiobutton(self.frame_results_left, text="Functions")
        self.func_button.pack(pady=5, padx=5, anchor='sw')
        self.class_button = ttk.Radiobutton(self.frame_results_left, text="Classes")
        self.class_button.pack(pady=5, padx=5, anchor='sw')
        self.text_button = ttk.Radiobutton(self.frame_results_left, text="Other apperance")
        self.text_button.pack(pady=5, padx=5, anchor='sw')

        self.frame_author = ttk.Frame(master)
        self.frame_author.pack()

        ttk.Label(self.frame_author, text="Created by Mariusz Hager, November 2017  mariuszhager@gmail.com", font=('Corbol', 6), justify=CENTER).pack(pady=5)


root = Tk()
gui = pyFinderGUI(root)
root.mainloop()