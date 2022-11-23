import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.nombreLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.nombreLabel["font"] = ft
        self.nombreLabel["fg"] = "#333333"
        self.nombreLabel["justify"] = "center"
        self.nombreLabel["text"] = "Nombre:"
        self.nombreLabel.place(x=50,y=60,width=70,height=25)

        self.nombreEntry=tk.Entry(root)
        self.nombreEntry["bg"] = "#ffffff"
        self.nombreEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.nombreEntry["font"] = ft
        self.nombreEntry["fg"] = "#333333"
        self.nombreEntry["justify"] = "center"
        self.nombreEntry["text"] = ""
        self.nombreEntry.place(x=120,y=60,width=462,height=30)

        self.generoLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.generoLabel["font"] = ft
        self.generoLabel["fg"] = "#333333"
        self.generoLabel["justify"] = "center"
        self.generoLabel["text"] = "Género:"
        self.generoLabel.place(x=50,y=100,width=70,height=25)

        self.generoEntry=tk.Entry(root)
        self.generoEntry["bg"] = "#ffffff"
        self.generoEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.generoEntry["font"] = ft
        self.generoEntry["fg"] = "#333333"
        self.generoEntry["justify"] = "center"
        self.generoEntry["text"] = ""
        self.generoEntry.place(x=120,y=100,width=461,height=30)

        self.duracionLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.duracionLabel["font"] = ft
        self.duracionLabel["fg"] = "#333333"
        self.duracionLabel["justify"] = "center"
        self.duracionLabel["text"] = "Duración:"
        self.duracionLabel.place(x=50,y=140,width=70,height=25)

        self.duracionEntry=tk.Entry(root)
        self.duracionEntry["bg"] = "#ffffff"
        self.duracionEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.duracionEntry["font"] = ft
        self.duracionEntry["fg"] = "#333333"
        self.duracionEntry["justify"] = "center"
        self.duracionEntry["text"] = ""
        self.duracionEntry.place(x=120,y=140,width=460,height=30)

        self.descripcionLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.descripcionLabel["font"] = ft
        self.descripcionLabel["fg"] = "#333333"
        self.descripcionLabel["justify"] = "center"
        self.descripcionLabel["text"] = "Descripción: "
        self.descripcionLabel.place(x=40,y=180,width=70,height=25)

        self.descripcionEntry=tk.Entry(root)
        self.descripcionEntry["bg"] = "#ffffff"
        self.descripcionEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.descripcionEntry["font"] = ft
        self.descripcionEntry["fg"] = "#333333"
        self.descripcionEntry["justify"] = "center"
        self.descripcionEntry["text"] = ""
        self.descripcionEntry.place(x=120,y=180,width=459,height=30)

        self.idiomaLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.idiomaLabel["font"] = ft
        self.idiomaLabel["fg"] = "#333333"
        self.idiomaLabel["justify"] = "center"
        self.idiomaLabel["text"] = "Idioma:"
        self.idiomaLabel.place(x=50,y=300,width=70,height=25)

        self.idiomaEntry=tk.Entry(root)
        self.idiomaEntry["bg"] = "#ffffff"
        self.idiomaEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.idiomaEntry["font"] = ft
        self.idiomaEntry["fg"] = "#333333"
        self.idiomaEntry["justify"] = "center"
        self.idiomaEntry["text"] = ""
        self.idiomaEntry.place(x=120,y=300,width=459,height=30)

        self.clasificacionLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.clasificacionLabel["font"] = ft
        self.clasificacionLabel["fg"] = "#333333"
        self.clasificacionLabel["justify"] = "center"
        self.clasificacionLabel["text"] = "Clasificación:"
        self.clasificacionLabel.place(x=40,y=220,width=70,height=25)

        self.clasificacionEntry=tk.Entry(root)
        self.clasificacionEntry["bg"] = "#ffffff"
        self.clasificacionEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.clasificacionEntry["font"] = ft
        self.clasificacionEntry["fg"] = "#333333"
        self.clasificacionEntry["justify"] = "center"
        self.clasificacionEntry["text"] = ""
        self.clasificacionEntry.place(x=120,y=220,width=457,height=30)

        self.tipoLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.tipoLabel["font"] = ft
        self.tipoLabel["fg"] = "#333333"
        self.tipoLabel["justify"] = "center"
        self.tipoLabel["text"] = "Tipo:"
        self.tipoLabel.place(x=60,y=260,width=70,height=25)

        self.tipoEntry=tk.Entry(root)
        self.tipoEntry["bg"] = "#ffffff"
        self.tipoEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.tipoEntry["font"] = ft
        self.tipoEntry["fg"] = "#333333"
        self.tipoEntry["justify"] = "center"
        self.tipoEntry["text"] = ""
        self.tipoEntry.place(x=120,y=260,width=458,height=30)

        self.tituloLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=33)
        self.tituloLabel["font"] = ft
        self.tituloLabel["fg"] = "#333333"
        self.tituloLabel["justify"] = "center"
        self.tituloLabel["text"] = "Alta de Películas"
        self.tituloLabel.place(x=60,y=20,width=488,height=30)

        self.guardarButton=tk.Button(root)
        self.guardarButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=13)
        self.guardarButton["font"] = ft
        self.guardarButton["fg"] = "#000000"
        self.guardarButton["justify"] = "center"
        self.guardarButton["text"] = "Guardar"
        self.guardarButton.place(x=310,y=440,width=268,height=30)
        self.guardarButton["command"] = self.self.guardarButton_command

        self.cancelarButton=tk.Button(root)
        self.cancelarButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=13)
        self.cancelarButton["font"] = ft
        self.cancelarButton["fg"] = "#000000"
        self.cancelarButton["justify"] = "center"
        self.cancelarButton["text"] = "Cancelar"
        self.cancelarButton.place(x=20,y=440,width=268,height=32)
        self.cancelarButton["command"] = self.self.cancelarButton_command
        
    def guardarButton_command(self):
        print(self.nombreEntry.get())
        list = [self.nombreEntry.get(),self.generoEntry.get(),self.duracionEntry.get(),self.descripcionEntry.get(),self.clasificacionEntry.get(),self.tipoEntry.get(),self.idiomaEntry.get()]




    def cancelarButton_command(self):
        print("cancelar")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()


