import os
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
from beehive import *


class App:
    """create a tkinter app to run the genetic algorithm"""

    def __init__(self) -> None:
        self.app = Tk()
        self.app.title('Genetic Algorithm')
        self.app.geometry('765x397')
        """background image"""
        background_image = ImageTk.PhotoImage(Image.open('img/bees.png'))
        background_label = Label(self.app, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = background_image

        """set the app's size"""
        self.app.resizable(False, False)
        """entry label"""
        entry_label = Label(self.app, text='Enter the number of generations', font=('bold', 20), bg='lightskyblue1', fg='black')
        entry_label.pack(pady=20)
        """entry to set the number of generations"""
        entry_text = IntVar()
        self.generations_entry = Entry(self.app, textvariable=entry_text, font=('bold', 14), bg='azure1', fg='black', borderwidth=5, justify='center')
        self.generations_entry.pack(pady=50)

        """load the csv file button"""
        load_csv_button = Button(self.app, text='Load csv file', command=self.load_csv, font=('bold', 14), bg='plum4', fg='lavenderblush1', borderwidth=5)
        load_csv_button.pack(pady=20)

        """run the genetic algorithm and show the results"""
        run_button = Button(self.app, text='Run', command=self.GA, font=('bold', 14), bg='mistyrose4', fg='mintcream', borderwidth=5)
        run_button.pack(pady=20)
        
        """csv file path label"""
        self.file = ""

        self.app.mainloop()


    """function to load the csv file"""
    def load_csv(self):
        global csv_file
        csv_file = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select a csv file', filetypes=(('csv files', '*.csv'), ('all files', '*.*')))
        csv_file_label = Label(self.app, text=csv_file)
        csv_file_label.pack(pady=20)
        self.file = csv_file


    """function to convert the csv file into a list of flower's positions"""    
    def convert_csv_to_list(self, file):
        flowers_list = pd.read_csv(file)
        flowers_list = np.array(flowers_list)
        flowers_list = flowers_list.tolist()
        return flowers_list
    

    def GA(self):
        """create a list of flowers and a hive """
        if self.file == "":
            messagebox.showerror('Error', 'Please load a csv file')
        flowers_list = self.convert_csv_to_list(self.file)
        hive = Hive(flowers_list)
        """get the number of generations"""
        self.gen_num = int(self.generations_entry.get())
        if self.gen_num == 0 or type(self.gen_num) != int:
            messagebox.showerror('Error', 'Please enter a number of generations')
            return
        hive.generate_population()

        for x in range(self.gen_num):
            hive.evaluate()
            hive.evaluate_average()
            hive.selection()
            hive.crossover()
            if x % 10 == 0:
                hive.mutation()
    
        hive.visualize_best_bee()
        hive.visualize_best_bee_through_generations()
        hive.visualize_average_fitness()
        hive.visualize_genealogical_tree_of_best_bee()


if __name__ == '__main__':
    app = App()