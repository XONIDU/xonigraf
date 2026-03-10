# XoniGraf - Graficador Matemático de Bajos Recursos

Desarrollador: Darian Alberto Camacho Salas

Aplicación de escritorio liviana para graficar funciones matemáticas, especialmente diseñada para ASUS Eee PC y equipos de bajos recursos. Soporta sumatorias, funciones trigonométricas y expresiones complejas.

---

## ⚠️ ADVERTENCIA
Este código tiene **únicamente fines educativos** para democratizar el acceso al software matemático.

## 📁 Estructura del Proyecto

```
xonigraf/
├── start.py                 # 🟢 LANZADOR UNIVERSAL (¡SOLO EJECUTA ESTE!)
├── xonigraf.py              # 🔵 PROGRAMA PRINCIPAL (graficador)
├── requisitos.txt           # Dependencias del proyecto
└── README.md                # Este archivo
```

---

## 🚀 **ASÍ DE FÁCIL: SOLO EJECUTA start.py**

**¡Ya no necesitas hacer nada más!** El archivo `start.py` hace TODO por ti:

✅ Detecta automáticamente tu sistema operativo  
✅ Verifica qué dependencias faltan (sympy, numpy, matplotlib, tkinter)  
✅ **Las instala automáticamente** con los comandos correctos  
✅ Ejecuta el programa principal  

## 🪟 **PARA WINDOWS**

```bash
# Abre CMD o PowerShell y escribe:
python start.py
```

## 🐧 **PARA LINUX**

```bash
# Abre terminal y escribe:
python3 start.py
```

## 🍎 **PARA macOS**

```bash
# Abre terminal y escribe:
python3 start.py
```

---

## 🎮 CÓMO USAR XoniGraf

1️⃣ **Ejecuta** el programa:
```bash
python start.py
```

2️⃣ **Ingresa tu función** en el campo de texto usando sintaxis de Python/sympy

3️⃣ **Define el rango X** en formato `min,max` (ej: `-10,10`)

4️⃣ **Presiona Enter** o el botón "Graficar" para ver el resultado

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

## 🔧 PROBLEMAS COMUNES (Y SOLUCIONES)

| Problema | Solución |
|----------|----------|
| `ModuleNotFoundError: No module named 'sympy'` | `start.py` lo instala automáticamente |
| `ImportError: No module named tkinter` | En Linux: `sudo apt install python3-tk` (Debian/Ubuntu) o `sudo pacman -S tk` (Arch) |
| Error `--break-system-packages` no funciona | `pip install --user sympy numpy matplotlib` |
| Error "name 'sum' is not defined" | Usa siempre `Sum` con mayúscula |
| No se ve la gráfica | Verifica rango X válido (ej: `-5,5`) |

---

## ⚡ OPTIMIZADO PARA EQUIPOS DE BAJOS RECURSOS

✅ Genera 500 puntos por gráfica (balance calidad/rendimiento)  
✅ Libera memoria automáticamente en cada nueva gráfica  
✅ Interfaz oscura que reduce consumo de batería  
✅ Probado en **ASUS Eee PC 900** (1GB RAM, Celeron M 900MHz)  

---

## 📞 CONTACTO

- **Creador:** Darian Alberto Camacho Salas
- **📧 Email:** xonidu@gmail.com
- **📸 Instagram:** @xonidu
- **💻 GitHub:** [XONIDU/xonigraf](https://github.com/XONIDU/xonigraf)

---

```
╔════════════════════════════════════╗
║   XoniGraf 2026 - Hecho con ❤️     ║
║   por Darian Alberto Camacho Salas ║
║                                    ║
║   ¡SOLO EJECUTA start.py!          ║
║   Él instala todo automáticamente  ║
╚════════════════════════════════════╝
```

