# XoniGraf - Graficador Matemático de Bajos Recursos

[![AUR version](https://img.shields.io/aur/version/xonigraf)](https://aur.archlinux.org/packages/xonigraf)
[![AUR votes](https://img.shields.io/aur/votes/xonigraf)](https://aur.archlinux.org/packages/xonigraf)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/XONIDU/xonigraf?tab=MIT-1-ov-file#readme)

**Desarrollado por:** Darian Alberto Camacho Salas  
**Organización:** XONIDU

Aplicación de escritorio liviana para graficar funciones matemáticas, especialmente diseñada para **ASUS Eee PC** y equipos de bajos recursos. Soporta sumatorias, funciones trigonométricas y expresiones complejas.

---

## ⚠️ ADVERTENCIA

Este código tiene **únicamente fines educativos** para democratizar el acceso al software matemático.

---

## 📁 Estructura del Proyecto

```
xonigraf/
├── start.py                 # 🟢 LANZADOR UNIVERSAL
├── xonigraf.py              # 🔵 PROGRAMA PRINCIPAL
├── requirements.txt         # Dependencias
├── README.md                # Este archivo
└── LICENSE                  # MIT License
```

---

## 🚀 INSTALACIÓN

### 📦 **Opción 1 – Arch Linux / Manjaro (AUR)**

```bash
# Instalar desde AUR
yay -S xonigraf

# O con paru
paru -S xonigraf

# Ejecutar
xonigraf
```

### 🛠️ **Opción 2 – Comando `xoninstall` (recomendado para futuras herramientas XONI)**

Agrega la siguiente función a tu `~/.bashrc` con un solo comando:

```bash
echo 'xoninstall() { if [ -z "$1" ]; then echo "Uso: xoninstall <repo>"; echo "Ej: xoninstall xoniran"; else git clone "https://github.com/XONIDU/$1.git"; cd "$1"; fi }' >> ~/.bashrc && source ~/.bashrc
```

Luego simplemente escribe:

```bash
xoninstall xonigraf
cd xonigraf
pip install -r requirements.txt   # o pip install sympy numpy matplotlib
python start.py
```

> **Nota:** Esta función te servirá para instalar cualquier otra herramienta futura de XONIDU (por ejemplo `xoninstall xonichat`, `xoninstall xoniran`).

### 🐧 **Opción 3 – Otras distribuciones Linux**

```bash
# Clonar repositorio
git clone https://github.com/XONIDU/xonigraf.git
cd xonigraf

# Instalar dependencias
pip install sympy numpy matplotlib

# En Debian/Ubuntu/antiX instalar tkinter
sudo apt install python3-tk

# En Fedora
sudo dnf install python3-tkinter

# Ejecutar
python start.py
```

### 🪟 **Opción 4 – Windows**

```bash
# Clonar o descargar
git clone https://github.com/XONIDU/xonigraf.git
cd xonigraf

# Instalar dependencias
pip install sympy numpy matplotlib

# Ejecutar
python start.py
```

### 🍎 **Opción 5 – macOS**

```bash
# Clonar repositorio
git clone https://github.com/XONIDU/xonigraf.git
cd xonigraf

# Instalar dependencias
pip3 install sympy numpy matplotlib

# Ejecutar
python3 start.py
```

---

## 🎮 CÓMO USAR

1. **Ejecuta** el programa:
   ```bash
   xonigraf   # Si instalaste desde AUR
   # o
   python start.py
   ```

2. **Ingresa tu función** en el campo de texto usando sintaxis de Python/sympy

3. **Define el rango X** en formato `min,max` (ej: `-10,10`)

4. **Presiona Enter** o el botón "Graficar" para ver el resultado

---

## 📝 SINTAXIS DE SUMATORIAS

```
Sum(expresión, (variable, inicio, fin))
```

| Expresión | Significado |
|-----------|-------------|
| `Sum(cos(pi*x*n/2), (n,1,10))` | Σ cos(π·x·n/2) desde n=1 hasta 10 |
| `Sum(n*cos(pi*x*n/2), (n,1,5))` | Σ n·cos(π·x·n/2) desde n=1 hasta 5 |
| `Sum((-4/(pi*x**2))*(cos(pi*x/2)-1)*cos(n/2), (n,1,8))` | Serie de Fourier |

---

## 🖱️ BOTONES DE EJEMPLO

- **Ejemplo 1:** Suma simple de cosenos
- **Ejemplo 2:** Suma con coeficientes
- **Ejemplo 3:** Serie de Fourier (¡probada!)

---

## 🧮 FUNCIONES MATEMÁTICAS DISPONIBLES

- **Trigonométricas:** `cos`, `sin`, `tan`
- **Constantes:** `pi`, `E` (número e)
- **Otras:** `sqrt`, `exp`, `log`, `abs`
- **Operadores:** `+`, `-`, `*`, `/`, `**` (potencia)

---

## 🔧 SOLUCIÓN DE PROBLEMAS COMUNES

| Problema | Solución |
|----------|----------|
| `ModuleNotFoundError: No module named 'sympy'` | `pip install sympy numpy matplotlib` |
| `ImportError: No module named tkinter` | En Linux: `sudo apt install python3-tk` (Debian/Ubuntu) o `sudo pacman -S tk` (Arch) |
| `No se ve la gráfica` | Verifica rango X válido (ej: `-5,5`) |
| `Error en sumatorias` | Usa siempre `Sum` con mayúscula |

---

## ⚡ OPTIMIZADO PARA EQUIPOS DE BAJOS RECURSOS

✅ Genera 500 puntos por gráfica (balance calidad/rendimiento)  
✅ Libera memoria automáticamente en cada nueva gráfica  
✅ Interfaz oscura que reduce consumo de batería  
✅ Probado en **ASUS Eee PC 900** (1GB RAM, Celeron M 900MHz)  
✅ Guarda automáticamente la última expresión en `~/.xonigraf/config.txt`

---

## 📦 DEPENDENCIAS

- Python 3.8+
- sympy
- numpy
- matplotlib
- tkinter (viene con Python, en Linux a veces requiere instalación separada)

---

## 📂 ARCHIVOS DE CONFIGURACIÓN

XoniGraf guarda la última expresión usada en:
```
~/.xonigraf/config.txt
```

---

## 📞 CONTACTO

- **Creador:** Darian Alberto Camacho Salas
- **📧 Email:** xonidu@gmail.com
- **📸 Instagram:** @xonidu
- **💻 GitHub:** [XONIDU/xonigraf](https://github.com/XONIDU/xonigraf)
- **📦 AUR:** [xonigraf](https://aur.archlinux.org/packages/xonigraf)

---

```
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   XoniGraf 2026 - Hecho con ❤️ por XONIDU                    ║
║   Graficador matemático ligero para todos                    ║
║                                                              ║
║   GitHub: https://github.com/XONIDU/xonigraf                ║
║   AUR: yay -S xonigraf                                       ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

---

**BY: XONIDU - Darian Alberto Camacho Salas**  
