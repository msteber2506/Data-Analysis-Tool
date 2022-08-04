
import csv
import tkinter as tk
from tkinter import ttk, filedialog




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
    

def validateFile():
    filename = uploadFile()
    if filename.split(".")[-1] != "csv":
        warning()
        print("NOT CSV")
    else:
        global pathtofile 
        pathtofile = filename
        print("SUCCESS")
        print(pathtofile)


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

def searchInFile(key):
    dataArray = parsecsv('/Users/mustafasuhateber/Desktop/test.csv')
    count = 0
    for row in dataArray:
        for cell in row:
            if row == key:
                count +=1



if __name__ == "__main__":

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
    button = tk.Button(toolbar, text='Upload', command=validateFile)
    button.grid(sticky='e',row=1,column=0)
    button = tk.Button(toolbar, text='Display', command=displayTable)
    button.grid(sticky='w',row=1,column=1)

    text = tk.Label(toolbar,text="Data Analysis Tools",anchor='center')
    text.grid(sticky='n',row=2,column=0,columnspan=2)
    button = tk.Button(toolbar, text='Search', command=lambda: searchInFile(key))
    button.grid(sticky='e',row=3,column=0)
    button = tk.Button(toolbar, text='Compare', command='')
    button.grid(sticky='w',row=3,column=1)
    toolbar.pack()

    '''
    area = tk.Text(bg='grey',font ="Helvetica 25 bold")
    area.pack(fill='x')
    '''


    window.mainloop()













    '''
    my_game = ttk.Treeview(window)

    my_game['columns'] = ['player_id', 'player_name', 'player_Rank', 'player_states', 'player_city']

    my_game.column("#0", width=0,  stretch='no')
    my_game.column("player_id",anchor=CENTER, width=80)
    my_game.column("player_name",anchor=CENTER,width=80)
    my_game.column("player_Rank",anchor=CENTER,width=80)
    my_game.column("player_states",anchor=CENTER,width=80)
    my_game.column("player_city",anchor=CENTER,width=80)

    my_game.heading("#0",text="",anchor=CENTER)
    my_game.heading("player_id",text="Id",anchor=CENTER)
    my_game.heading("player_name",text="Name",anchor=CENTER)
    my_game.heading("player_Rank",text="Rank",anchor=CENTER)
    my_game.heading("player_states",text="States",anchor=CENTER)
    my_game.heading("player_city",text="States",anchor=CENTER)

    my_game.insert(parent='',index='end',iid=0,
    values=['1','Ninja','101','Oklahoma', 'Moore'])
    my_game.insert(parent='',index='end',iid=1,text='',
    values=('2','Ranger','102','Wisconsin', 'Green Bay'))
    my_game.insert(parent='',index='end',iid=2,text='',
    values=('3','Deamon','103', 'California', 'Placentia'))
    my_game.insert(parent='',index='end',iid=3,text='',
    values=('4','Dragon','104','New York' , 'White Plains'))
    my_game.insert(parent='',index='end',iid=4,text='',
    values=('5','CrissCross','105','California', 'San Diego'))
    my_game.insert(parent='',index='end',iid=5,text='',
    values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))

    my_game.pack()'''