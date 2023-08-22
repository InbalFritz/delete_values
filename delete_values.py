import pandas as pd
from tkinter.filedialog import askopenfilename
from tkinter import *
from tkinter import simpledialog


def delete_values():
    Tk().withdraw()
    filename = askopenfilename()
    sheet = simpledialog.askstring("Sheet name", "Enter *Precise* name of sheet")
    new_excel = simpledialog.askstring("Excel name", "Enter name of the new excel")
    new_excel = new_excel+'.xlsx'

    df = pd.read_excel(filename, sheet_name = sheet)
    df['location_at_the_cell'].apply(lambda x: float(x))
    df = df.drop(df[df.location_at_the_cell <= -1].index)
    df = df.drop(df[df.location_at_the_cell >= 1].index)
    df.to_excel(new_excel)

if __name__ == '__main__':
    delete_values()