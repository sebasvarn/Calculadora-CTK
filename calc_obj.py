from tkinter import *
import customtkinter as ctk

class Calculator:
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.window = ctk.CTk()
        self.WIDTH = 300
        self.HEIGHT = 475
        self.window.geometry('{}x{}'.format(self.WIDTH, self.HEIGHT))   
        self.window.title('Calculadora CAMPER')
        self.window.resizable(0, 0)

        self.total_expresion = '0'
        self.current_expresion = '0'

        
        #FRAME PRINCIPAL
        self.frame = ctk.CTkFrame(self.window, width=self.WIDTH-50, height=self.HEIGHT-50, bg='white')
        self.frame.pack(fill=BOTH, expand=1, padx=10, pady=10, ipadx=10, ipady=10, side=TOP)
        
        #FRAME RESULTADO
        self.frame_result = ctk.CTkFrame(self.frame, width=self.WIDTH, height=50)
        self.frame_result.pack(fill=BOTH, expand=1, padx=10, pady=10, ipadx=10, ipady=10, side=TOP)
        
        #label resultado
        self.label_result = ctk.CTkLabel(self.frame_result, text=self.total_expresion, width=self.WIDTH, height=50, )
        self.label_result.pack(fill=BOTH, expand=1, anchor= E)
        self.label_result.config(font=("Arial", 20, "bold"))

        #FRAME OPERACIONES
        self.frame_operaciones = ctk.CTkFrame(self.frame, width=self.WIDTH, height=self.WIDTH)
        self.frame_operaciones.pack(fill=BOTH, expand=1, padx=10, pady=10, ipadx=10, ipady=10, side=TOP)
        for x in range(0,4):
            self.frame_operaciones.columnconfigure(x, weight=1)
        for y in range(0,4):
            self.frame_operaciones.rowconfigure(y, weight=1)
        


        #botones de clear 
        self.button_clear = ctk.CTkButton(self.frame_operaciones, text='CLEAR', width=50, height=50)
        self.button_clear.grid(row=0, column=1, sticky=W, padx=5, pady=5, ipadx=5, ipady=5, columnspan=2)



        #botones de numeros
        self.numeros = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0']
        self.buttons = []
        for i in range(len(self.numeros)):
            self.buttons.append(ctk.CTkButton(self.frame_operaciones, text=self.numeros[i], width=50, height=50))
            self.buttons[i].grid(row=i//3+1, column=i%3, sticky=W, padx=5, pady=5, ipadx=2, ipady=2)


        #botones de operaciones
        self.operaciones = ['+', '-', '*', '/']
        self.buttons_operaciones = []
        for i in range(len(self.operaciones)):
            self.buttons_operaciones.append(ctk.CTkButton(self.frame_operaciones, text=self.operaciones[i], width=50, height=50))
            self.buttons_operaciones[i].grid(row=i, column=3, sticky=W, padx=5, pady=5, ipadx=2, ipady=2)
        
        #boton resultado
        self.button_result = ctk.CTkButton(self.frame_operaciones, text='=', width=50, height=50)
        self.button_result.grid(row=4, column=1, sticky=W, padx=5, pady=5, ipadx=5, ipady=5, columnspan=3)
        

    def center(self, win):
            """
            ## Función que centra una ventana en la pantalla
            - param win: la ventana principal o frame a centrar
            """
            win.update_idletasks()
            width = win.winfo_width()
            frm_width = win.winfo_rootx() - win.winfo_x()
            win_width = width + 2 * frm_width
            height = win.winfo_height()
            titlebar_height = win.winfo_rooty() - win.winfo_y()
            win_height = height + titlebar_height + frm_width
            x = win.winfo_screenwidth() // 2 - win_width // 2
            y = win.winfo_screenheight() // 2 - win_height // 2
            win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
            win.deiconify()





    def run(self):
        self.center(self.window)
        self.window.mainloop()

if __name__ == '__main__':

    calculator = Calculator()
    calculator.run()





        



        