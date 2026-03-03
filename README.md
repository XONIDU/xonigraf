# XoniGraf - Graficador Matemático de Bajos Recursos

Desarrollado por: Darian Alberto Camacho Salas

Aplicación de escritorio liviana para graficar funciones matemáticas, especialmente diseñada para ASUS Eee PC y equipos de bajos recursos. Soporta sumatorias, funciones trigonométricas y expresiones complejas.

---

## 🚀 Instalación Rápida

### 1. Clonar o descargar

```bash
git clone https://github.com/XONIDU/xonigraf.git
cd xonigraf
```

### 2. Instalar dependencias

#### 🐧 ARCH LINUX / Manjaro
```bash
sudo pacman -S python-pip python-sympy python-numpy python-matplotlib tk
pip install --break-system-packages sympy numpy matplotlib
```

#### 🐧 UBUNTU / Debian / antiX / derivados
```bash
sudo apt update
sudo apt install python3 python3-pip python3-tk python3-sympy python3-numpy python3-matplotlib -y
pip3 install --break-system-packages sympy numpy matplotlib
```

#### 🍎 macOS
```bash
# Instalación normal
pip3 install sympy numpy matplotlib

# Si usas Python 3 por defecto
pip install sympy numpy matplotlib

# Para evitar problemas de permisos
pip install --user sympy numpy matplotlib
```

#### 🪟 WINDOWS
```bash
# Instalación normal
pip install sympy numpy matplotlib

# Si tienes varias versiones de Python
py -m pip install sympy numpy matplotlib

# En PowerShell
python -m pip install sympy numpy matplotlib
```

### 3. Verificar instalación
```bash
# Listar paquetes instalados
pip list | grep -E "sympy|numpy|matplotlib"

# Deberías ver: sympy, numpy, matplotlib
```

### 4. Ejecutar
```bash
python start.py
# o
python3 start.py
```

*Nota: Si falta alguna dependencia, el programa intentará instalarla automáticamente.*

---

## 📦 requisitos.txt
```txt
sympy==1.12
numpy==1.24.3
matplotlib==3.7.2
```

---

## 🎮 Cómo usar

1. **Ejecuta** el programa:
   ```bash
   python start.py
   ```

2. **Ingresa tu función** en el campo de texto usando sintaxis de Python/sympy.

3. **Define el rango X** en formato `min,max` (ej: `-10,10`).

4. **Presiona Enter** o el botón "Graficar" para ver el resultado.

---

## 📝 Sintaxis de sumatorias
```
Sum(expresión, (variable, inicio, fin))
```

| Expresión | Significado |
|-----------|-------------|
| `Sum(cos(pi*x*n/2), (n,1,10))` | Σ cos(π·x·n/2) desde n=1 hasta 10 |
| `Sum(n*cos(pi*x*n/2), (n,1,5))` | Σ n·cos(π·x·n/2) desde n=1 hasta 5 |
| `Sum((-4/(pi*x**2))*(cos(pi*x/2)-1)*cos(n/2), (n,1,8))` | Serie de Fourier |

---

## 🖱️ Botones de ejemplo

- **Ejemplo 1:** Suma simple de cosenos
- **Ejemplo 2:** Suma con coeficientes
- **Ejemplo 3:** Serie de Fourier (¡probada!)

---

## 🧮 Funciones matemáticas disponibles

- **Trigonométricas:** `cos`, `sin`, `tan`
- **Constantes:** `pi`, `E` (número e)
- **Otras:** `sqrt`, `exp`, `log`, `abs`
- **Operadores:** `+`, `-`, `*`, `/`, `**` (potencia)

---

## 🔧 Solución de problemas comunes

| Problema | Solución |
|----------|----------|
| `ModuleNotFoundError: No module named 'sympy'` | Ejecuta: `pip install sympy numpy matplotlib` |
| `ImportError: No module named tkinter` | Instala tk: `sudo apt install python3-tk` (Linux) |
| Error `--break-system-packages` no funciona | Usa: `pip install --user sympy numpy matplotlib` |
| Error "name 'sum' is not defined" | Usa siempre `Sum` con mayúscula |
| No se ve la gráfica | Verifica que el rango X sea válido (ej: `-5,5`) |

---

## 📂 Estructura del proyecto
```
xonigraf/
├── start.py                 # Programa principal (ejecutar este)
├── requisitos.txt           # Dependencias del proyecto
├── README.md                # Este archivo
```

---

## ⚡ Optimizado para equipos de bajos recursos

✅ Genera 500 puntos por gráfica (balance calidad/rendimiento)  
✅ Libera memoria automáticamente en cada nueva gráfica  
✅ Interfaz oscura que reduce consumo de batería  
✅ Probado en **ASUS Eee PC 900** (1GB RAM, Celeron M 900MHz)

---

## 📞 Contacto

- **Creador:** Darian Alberto Camacho Salas
- **📧 Email:** xonidu@gmail.com
- **📸 Instagram:** @xonidu
- **💻 GitHub:** [XONIDU/xonigraf](https://github.com/XONIDU/xonigraf)
