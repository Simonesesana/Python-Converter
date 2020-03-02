import Funzioni as fz
import tkinter as tk

class finestra(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)

        self.master.geometry("200x150")
        self.master.resizable(0,0)
        self.master.title("Convertitore")

        self.grid()
        self.main()

    def main(self):

        #Binario
        self.b = tk.IntVar()

        self.etc1 = tk.Label(self, text = "Binario")
        self.txt1 = tk.Entry(self, textvariable = self.b)

        self.etc1.grid(row = 0, column = 0)
        self.txt1.grid(row = 0, column = 1)

        #Ottale
        self.o = tk.IntVar()

        self.etc2 = tk.Label(self, text = "Ottale")
        self.txt2 = tk.Entry(self, textvariable = self.o)

        self.etc2.grid(row = 1, column = 0)
        self.txt2.grid(row = 1, column = 1)

        #Decimale
        self.d = tk.IntVar()

        self.etc3 = tk.Label(self, text = "Decimale")
        self.txt3 = tk.Entry(self, textvariable = self.d)

        self.etc3.grid(row = 2, column = 0)
        self.txt3.grid(row = 2, column = 1)

        #Esadecimale
        self.e = tk.IntVar()

        self.etc4 = tk.Label(self, text = "Esadecimale")
        self.txt4 = tk.Entry(self, textvariable = self.e)

        self.etc4.grid(row = 3, column = 0)
        self.txt4.grid(row = 3, column = 1)

        #Bottoni
        #Converti
        btn1 = tk.Button(self, text = "Converti", command = self.conv)
        btn1.grid(row = 4, column = 1)

        #Azzera
        btn1 = tk.Button(self, text = "Azzera", command = self.rezero)
        btn1.grid(row = 4, column = 0)

        #Esci
        btn2 = tk.Button(self, text = "Esci", command = self.master.destroy)
        btn2.grid(row = 5, column = 0)

#Conversione
    def conv(self):
        b = int(self.txt1.get())
        o = int(self.txt2.get())
        d = int(self.txt3.get())
        e = self.txt4.get()

        if(b != 0):
            self.d.set(fz.btd(b))               #Decimale
            self.o.set(fz.dto(fz.btd(b)))       #Ottale
            self.e.set(fz.dte(fz.btd(b)))       #Esadecimale
        elif(o !=0):
            self.b.set(fz.dtb(fz.otd(o)))       #Binario
            self.d.set(fz.otd(o))               #Decimale
            self.e.set(fz.dte(fz.otd(o)))       #Ottale
        elif(d !=0):
            self.b.set(fz.dtb(d))               #Binario
            self.o.set(fz.dto(d))               #Ottale
            self.e.set(fz.dte(d))               #Esadecimale
        elif(e != "0"):
            self.b.set(fz.dtb(fz.etd(e)))       #Binario
            self.o.set(fz.dto(fz.etd(e)))       #Ottale
            self.d.set(fz.etd(e))               #Decimale

#Azzeramento
    def rezero(self):
        o = self.txt2.get()
        b = self.txt1.get()
        d = self.txt3.get()
        e = self.txt4.get()

        self.b.set(0)
        self.o.set(0)
        self.d.set(0)
        self.e.set(0)

f = finestra()
f.mainloop
