#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
XoniGraf 2026 - Graficador Matemático Ligero
Optimizado para equipos de bajos recursos (ASUS Eee PC, 1GB RAM)
Soporta sumatorias, series de Fourier y funciones complejas
Desarrollador: Darian Alberto Camacho Salas
Organización: XONIDU
"""

import tkinter as tk
from tkinter import ttk, messagebox
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os
import sys

class XoniGraf:
    def __init__(self, master):
        self.master = master
        master.title("XoniGraf 2026 - Graficador Matemático")
        master.geometry("800x700")
        master.configure(bg='#2b2b2b')
        
        # Variables
        self.expresion = tk.StringVar(value="Sum(cos(pi*x*n/2), (n,1,10))")
        self.rango_x = tk.StringVar(value="-10,10")
        
        # Directorio de configuración
        self.config_dir = self.get_config_dir()
        
        self.crear_interfaz()
        self.cargar_ultima_expresion()
    
    def get_config_dir(self):
        """Devuelve el directorio de configuración de XoniGraf"""
        home = os.path.expanduser("~")
        config_dir = os.path.join(home, '.xonigraf')
        os.makedirs(config_dir, exist_ok=True)
        return config_dir
    
    def cargar_ultima_expresion(self):
        """Carga la última expresión guardada"""
        config_file = os.path.join(self.config_dir, 'config.txt')
        try:
            with open(config_file, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    if line.startswith('expresion='):
                        self.expresion.set(line.split('=', 1)[1].strip())
                    elif line.startswith('rango='):
                        self.rango_x.set(line.split('=', 1)[1].strip())
        except FileNotFoundError:
            pass
    
    def guardar_configuracion(self):
        """Guarda la expresión actual para la próxima ejecución"""
        config_file = os.path.join(self.config_dir, 'config.txt')
        try:
            with open(config_file, 'w') as f:
                f.write(f"expresion={self.expresion.get()}\n")
                f.write(f"rango={self.rango_x.get()}\n")
        except:
            pass
    
    def crear_interfaz(self):
        # Título
        tk.Label(self.master, text="XoniGraf 2026", fg='white', bg='#2b2b2b',
                font=('Arial', 16, 'bold')).pack(pady=5)
        
        # Subtítulo
        tk.Label(self.master, text="Graficador Matemático Ligero", fg='#aaa', bg='#2b2b2b',
                font=('Arial', 9)).pack(pady=(0,5))
        
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
        tk.Label(frame_rango, text="Rango X (min,max):", fg='white', bg='#2b2b2b').pack(side='left', padx=5)
        self.entry_rango = tk.Entry(frame_rango, textvariable=self.rango_x, width=20,
                                   bg='#3c3c3c', fg='white')
        self.entry_rango.pack(side='left', padx=5)
        self.entry_rango.bind('<Return>', lambda e: self.graficar())
        
        # Info de sumatorias
        frame_info = tk.Frame(self.master, bg='#2b2b2b')
        frame_info.pack(pady=2)
        tk.Label(frame_info, text="Sintaxis: Sum(expresión, (n,inicio,fin))", 
                fg='#888', bg='#2b2b2b', font=('Arial', 8)).pack()
        
        # Canvas para matplotlib
        self.figure = plt.Figure(figsize=(7, 5), dpi=100, facecolor='#2b2b2b')
        self.ax = self.figure.add_subplot(111)
        self.ax.set_facecolor('#1e1e1e')
        self.ax.tick_params(colors='white')
        self.ax.xaxis.label.set_color('white')
        self.ax.yaxis.label.set_color('white')
        self.ax.title.set_color('white')
        self.ax.grid(True, alpha=0.3, color='gray')
        
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.master)
        self.canvas.get_tk_widget().pack(pady=10, fill='both', expand=True)
        
        # Estado
        self.estado = tk.Label(self.master, text="Listo", fg='#aaa', bg='#2b2b2b')
        self.estado.pack(fill='x', padx=10, pady=2)
        
        # Versión
        tk.Label(self.master, text="v2.0 - Optimizado para ASUS Eee PC y equipos de 1GB RAM", 
                fg='#666', bg='#2b2b2b', font=('Arial', 8)).pack()
        
        # BY
        tk.Label(self.master, text="BY: XONIDU - Darian Alberto Camacho Salas", 
                fg='#555', bg='#2b2b2b', font=('Arial', 7)).pack()
    
    def ejemplo1(self):
        """Sum(cos(pi*x*n/2), (n,1,10))"""
        self.expresion.set("Sum(cos(pi*x*n/2), (n,1,10))")
        self.rango_x.set("-5,5")
        self.actualizar_estado("Ejemplo 1 cargado: Suma de cosenos")
        self.graficar()
    
    def ejemplo2(self):
        """Sum(n*cos(pi*x*n/2), (n,1,5))"""
        self.expresion.set("Sum(n*cos(pi*x*n/2), (n,1,5))")
        self.rango_x.set("-5,5")
        self.actualizar_estado("Ejemplo 2 cargado: Suma con coeficientes")
        self.graficar()
    
    def ejemplo3(self):
        """Serie de Fourier"""
        self.expresion.set("Sum((-4/(pi*x**2))*(cos(pi*x/2)-1)*cos(n/2), (n,1,8))")
        self.rango_x.set("-10,10")
        self.actualizar_estado("Ejemplo 3 cargado: Serie de Fourier")
        self.graficar()
    
    def actualizar_estado(self, mensaje):
        self.estado.config(text=mensaje)
        self.master.update_idletasks()
    
    def graficar(self):
        try:
            self.actualizar_estado("Procesando expresión...")
            
            # Obtener rango
            rango_str = self.rango_x.get().strip()
            if ',' not in rango_str:
                raise ValueError("Formato inválido. Usa min,max (ej: -10,10)")
            
            x_min, x_max = map(float, rango_str.split(','))
            
            if x_min >= x_max:
                raise ValueError("El valor mínimo debe ser menor que el máximo")
            
            # Definir variables simbólicas
            x = sp.Symbol('x')
            n = sp.Symbol('n')
            
            # Obtener expresión
            expr_str = self.expresion.get().strip()
            
            if not expr_str:
                raise ValueError("Ingresa una expresión válida")
            
            # Reemplazar Sum por sp.Sum
            expr_str = expr_str.replace('Sum(', 'sp.Sum(')
            
            # Evaluar la expresión
            expr = eval(expr_str, {'sp': sp, 'x': x, 'n': n, 'pi': sp.pi,
                                  'cos': sp.cos, 'sin': sp.sin, 'tan': sp.tan,
                                  'sqrt': sp.sqrt, 'exp': sp.exp, 'log': sp.log,
                                  'abs': sp.Abs})
            
            # Convertir a función numérica
            f_num = sp.lambdify(x, expr, modules=['numpy'])
            
            # Generar puntos (optimizado para bajos recursos: 500 puntos)
            self.actualizar_estado("Generando puntos...")
            x_vals = np.linspace(x_min, x_max, 500)
            y_vals = f_num(x_vals)
            
            # Limpiar y graficar
            self.ax.clear()
            self.ax.set_facecolor('#1e1e1e')
            self.ax.plot(x_vals, y_vals, 'cyan', linewidth=2)
            self.ax.grid(True, alpha=0.3, color='gray')
            self.ax.set_xlabel('x', color='white')
            self.ax.set_ylabel('f(x)', color='white')
            
            # Acortar título si es muy largo
            titulo = expr_str[:60] + "..." if len(expr_str) > 60 else expr_str
            self.ax.set_title(f'f(x) = {titulo}', color='white', fontsize=10)
            self.ax.tick_params(colors='white')
            
            # Ajustar límites Y automáticamente
            y_vals_clean = y_vals[np.isfinite(y_vals)]
            if len(y_vals_clean) > 0:
                y_min, y_max = np.min(y_vals_clean), np.max(y_vals_clean)
                padding = (y_max - y_min) * 0.1
                if padding == 0:
                    padding = 1
                self.ax.set_ylim(y_min - padding, y_max + padding)
            
            self.canvas.draw()
            
            # Guardar configuración
            self.guardar_configuracion()
            
            puntos_validos = np.sum(np.isfinite(y_vals))
            self.actualizar_estado(f"Gráfica generada - {puntos_validos} puntos válidos de 500")
            
        except ValueError as e:
            messagebox.showerror("Error de formato", f"Formato inválido:\n{str(e)}")
            self.actualizar_estado("Error: Formato inválido")
        except SyntaxError as e:
            messagebox.showerror("Error de sintaxis", f"Expresión inválida:\n{str(e)}")
            self.actualizar_estado("Error: Sintaxis inválida")
        except ZeroDivisionError:
            messagebox.showerror("Error matemático", "División entre cero en la expresión")
            self.actualizar_estado("Error: División entre cero")
        except Exception as e:
            messagebox.showerror("Error", f"Error al graficar:\n{str(e)}")
            self.actualizar_estado(f"Error: {str(e)[:50]}")

def verificar_dependencias():
    """Verifica que las dependencias estén instaladas"""
    try:
        import sympy
        import numpy
        import matplotlib
        return True
    except ImportError as e:
        print(f"\n[ERROR] Falta dependencia: {e}")
        print("[INFO] Instala con: pip install sympy numpy matplotlib")
        return False

def main():
    # Verificar dependencias
    if not verificar_dependencias():
        print("\n[INFO] Instalando dependencias automáticamente...")
        os.system("pip3 install sympy numpy matplotlib --break-system-packages")
        
        # Verificar nuevamente
        try:
            import sympy
            import numpy
            import matplotlib
        except ImportError:
            print("[ERROR] No se pudieron instalar las dependencias")
            print("       Instala manualmente: pip install sympy numpy matplotlib")
            sys.exit(1)
    
    # Crear directorio de configuración si no existe
    home = os.path.expanduser("~")
    config_dir = os.path.join(home, '.xonigraf')
    os.makedirs(config_dir, exist_ok=True)
    
    # Iniciar aplicación
    root = tk.Tk()
    app = XoniGraf(root)
    root.mainloop()

if __name__ == "__main__":
    main()
