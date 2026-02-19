import tkinter as tk
from tkinter import ttk, messagebox
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class XoniGrafSimple:
    def __init__(self, master):
        self.master = master
        master.title("XoniGraf Simple - Eee PC")
        master.geometry("800x700")
        master.configure(bg='#2b2b2b')

        # Variables
        self.expresion = tk.StringVar(value="Sum(cos(pi*x*n/2)/n, (n,1,10))")
        self.rango_x = tk.StringVar(value="-10,10")
        
        self.crear_interfaz()
        
    def crear_interfaz(self):
        # Título
        tk.Label(self.master, text="XoniGraf Simple", fg='white', bg='#2b2b2b',
                font=('Arial', 16, 'bold')).pack(pady=5)

        # Frame de entrada
        frame_input = tk.Frame(self.master, bg='#2b2b2b')
        frame_input.pack(pady=5, fill='x', padx=10)
        
        tk.Label(frame_input, text="f(x) =", fg='white', bg='#2b2b2b',
                font=('Arial', 11)).pack(side='left')
        
        self.entry = tk.Entry(frame_input, textvariable=self.expresion,
                             font=('Courier', 11), bg='#3c3c3c', fg='white',
                             insertbackground='white', width=60)
        self.entry.pack(side='left', fill='x', expand=True, padx=5)
        self.entry.bind('<Return>', lambda e: self.graficar())

        # Frame de botones
        frame_buttons = tk.Frame(self.master, bg='#2b2b2b')
        frame_buttons.pack(pady=5)
        
        tk.Button(frame_buttons, text="Graficar", command=self.graficar,
                 bg='#4CAF50', fg='white', width=10).pack(side='left', padx=2)
        tk.Button(frame_buttons, text="Ejemplo 1", command=self.ejemplo1,
                 bg='#FF9800', fg='white', width=10).pack(side='left', padx=2)
        tk.Button(frame_buttons, text="Ejemplo 2", command=self.ejemplo2,
                 bg='#FF9800', fg='white', width=10).pack(side='left', padx=2)
        tk.Button(frame_buttons, text="Ejemplo 3", command=self.ejemplo3,
                 bg='#FF9800', fg='white', width=10).pack(side='left', padx=2)

        # Rango X
        frame_rango = tk.Frame(self.master, bg='#2b2b2b')
        frame_rango.pack(pady=5)
        tk.Label(frame_rango, text="Rango X:", fg='white', bg='#2b2b2b').pack(side='left', padx=5)
        tk.Entry(frame_rango, textvariable=self.rango_x, width=20,
                bg='#3c3c3c', fg='white').pack(side='left', padx=5)

        # Canvas para matplotlib
        self.figure = plt.Figure(figsize=(7, 5), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.master)
        self.canvas.get_tk_widget().pack(pady=10, fill='both', expand=True)

        # Estado
        self.estado = tk.Label(self.master, text="Listo", fg='#aaa', bg='#2b2b2b')
        self.estado.pack(fill='x', padx=10, pady=2)

    def ejemplo1(self):
        """Sum(cos(pi*x*n/2), (n,1,10))"""
        self.expresion.set("Sum(cos(pi*x*n/2), (n,1,10))")
        self.rango_x.set("-5,5")
        self.actualizar_estado("Ejemplo 1 cargado")

    def ejemplo2(self):
        """Sum(n*cos(pi*x*n/2), (n,1,5))"""
        self.expresion.set("Sum(n*cos(pi*x*n/2), (n,1,5))")
        self.rango_x.set("-5,5")
        self.actualizar_estado("Ejemplo 2 cargado")

    def ejemplo3(self):
        """Tu expresión: Sum((-4/(pi*x**2))*(cos(pi*x/2)-1)*cos(n/2), (n,1,8))"""
        self.expresion.set("Sum((-4/(pi*x**2))*(cos(pi*x/2)-1)*cos(n/2), (n,1,8))")
        self.rango_x.set("-10,10")
        self.actualizar_estado("Ejemplo 3 cargado (tu expresión)")

    def actualizar_estado(self, mensaje):
        self.estado.config(text=mensaje)

    def graficar(self):
        try:
            # Obtener rango
            x_min, x_max = map(float, self.rango_x.get().split(','))
            
            # Definir variable simbólica
            x = sp.Symbol('x')
            n = sp.Symbol('n')
            
            # Obtener expresión
            expr_str = self.expresion.get()
            
            # Reemplazar Sum por sp.Sum
            expr_str = expr_str.replace('Sum(', 'sp.Sum(')
            
            # Evaluar la expresión
            expr = eval(expr_str, {'sp': sp, 'x': x, 'n': n, 'pi': sp.pi,
                                  'cos': sp.cos, 'sin': sp.sin, 'tan': sp.tan,
                                  'sqrt': sp.sqrt, 'exp': sp.exp, 'log': sp.log})
            
            # Convertir a función numérica
            f_num = sp.lambdify(x, expr, modules=['numpy'])
            
            # Generar puntos
            x_vals = np.linspace(x_min, x_max, 500)
            y_vals = f_num(x_vals)
            
            # Limpiar y graficar
            self.ax.clear()
            self.ax.plot(x_vals, y_vals, 'b-', linewidth=2)
            self.ax.grid(True, alpha=0.3)
            self.ax.set_xlabel('x')
            self.ax.set_ylabel('f(x)')
            self.ax.set_title(f'Gráfica: {expr_str}')
            
            # Ajustar límites Y automáticamente
            y_min, y_max = np.nanmin(y_vals), np.nanmax(y_vals)
            padding = (y_max - y_min) * 0.1
            self.ax.set_ylim(y_min - padding, y_max + padding)
            
            self.canvas.draw()
            self.actualizar_estado(f"Gráfica generada - {len(x_vals)} puntos")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al graficar:\n{str(e)}")
            self.actualizar_estado("Error")

def main():
    # Instalar sympy si no está
    import subprocess
    import sys
    
    try:
        import sympy
    except ImportError:
        print("Instalando sympy...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "sympy"])
        print("Sympy instalado. Reinicia el programa.")
        sys.exit()
    
    root = tk.Tk()
    app = XoniGrafSimple(root)
    root.mainloop()

if __name__ == "__main__":
    main()
