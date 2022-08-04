
import csv
import tkinter as tk
from tkinter import ttk, filedialog, simpledialog

class File:
    def __init__(self,path=""):
        self.path = path


def parsecsv(dir):
    dataArray = []
    with open(dir, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for row in data:
            dataArray.append(row)
    return dataArray

def uploadFile(event=None):
    filename = filedialog.askopenfilename()
    return(filename)

def validateFile(filename):
    if filename.split(".")[-1] != "csv":
        warning()
        print("NOT CSV")
        return False
    else:
        print("SUCCESS")
        print(filename)
        return True

def searchInFile(key):
    dataArray = parsecsv('/Users/mustafasuhateber/Desktop/test.csv')
    count = 0
    for row in dataArray:
        for cell in row[1:]:
            if cell == key:
                count +=1
    return count

def searchButton():
    inp = simpledialog.askstring("Monkey", "Please enter the word...")
    count = searchInFile(inp)
    print(count)
    return count

def uploadButton(file):
    if validateFile:
        file.path = validateFile(uploadFile())


def warning():
    popup = tk.Tk()
    popup.title("Tool")
    popup_width = 300
    popup_height = 150
    center_x = int(screen_width/2 - popup_width / 2)
    center_y = int(screen_height/2 - popup_height / 2)
    popup.geometry(f'{popup_width}x{popup_height}+{center_x}+{center_y}')
    message = tk.Label(popup,text="ERROR")
    message.grid(column=0,row=0)

def displayTable():
    dataArray = parsecsv('/Users/mustafasuhateber/Desktop/test.csv')
    table = ttk.Treeview(window, show="tree headings", height=100)
    columns = []
    for x in range(len(dataArray[0])+1):
        columns.append(x)
    table['columns'] = columns
    table.column("#0", width=0,  stretch='no')
    table.column(0,anchor='w',width=10)
    table.heading(0,text='',anchor='center')
    for x in range(1,len(columns)):
        table.column(x,anchor='center',width=80)
        table.heading(x,text=dataArray[0][x-1],anchor='center')
    for row in dataArray[1:]:
        row.insert(0,dataArray.index(row))  # row id
        table.insert(parent='',index='end',iid=dataArray.index(row),values=row)
    table.pack()

if __name__ == "__main__":

    file = File()

    window = tk.Tk()
    window.title("Tool")
    window_width = 1200
    window_height = 600
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    ttk.Style().configure(  '.',              # every class of object
            relief = '',  # flat ridge for separator
            borderwidth = 0,  # zero width for the border
                )

    toolbar = tk.Frame(window)

    text = tk.Label(toolbar,text="Welcome to Data Analysis Application. Please Upload a File to Continue...",anchor='center')
    text.grid(sticky='n',row=0,column=0,columnspan=2)
    button = tk.Button(toolbar, text='Upload', command=lambda: uploadButton(file))
    button.grid(sticky='e',row=1,column=0)
    button = tk.Button(toolbar, text='Display', command=displayTable)
    button.grid(sticky='w',row=1,column=1)

    text = tk.Label(toolbar,text="Data Analysis Tools",anchor='center')
    text.grid(sticky='n',row=2,column=0,columnspan=2)
    button = tk.Button(toolbar, text='Search', command=searchButton)
    button.grid(sticky='e',row=3,column=0)
    button = tk.Button(toolbar, text='Compare', command='')
    button.grid(sticky='w',row=3,column=1)
    toolbar.pack()

    '''
    area = tk.Text(bg='grey',font ="Helvetica 25 bold")
    area.pack(fill='x')
    '''


    window.mainloop()












