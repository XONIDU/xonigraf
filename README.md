# XoniGraf Simple - Graficador Matemático con Sumatorias

Aplicación de escritorio liviana para graficar funciones matemáticas, especialmente diseñada para **ASUS Eee PC** y equipos de bajos recursos. Soporta **sumatorias**, funciones trigonométricas y expresiones complejas.

## ⚡ Características

- 📈 Graficador en tiempo real con matplotlib
- ∑ Soporte para sumatorias con sintaxis `Sum(expresión, (n,inicio,fin))`
- 🎯 3 ejemplos precargados (incluyendo tu expresión de Fourier)
- 🖥️ Interfaz oscura amigable para la vista
- 🚀 Optimizado para equipos con pocos recursos

## 📦 Requisitos

- Python 3.6+
- Dependencias: `sympy`, `numpy`, `matplotlib`, `tkinter`

## 🔧 Instalación rápida

```bash
# Instalar dependencias
pip install sympy numpy matplotlib

# Ejecutar
python start.py

#o

python3 start.py

*Nota: Si falta alguna dependencia, el programa intentará instalarla automáticamente.*

## 🎮 Cómo usar

1. **Ejecuta** el programa:
   ```bash
   python start.py

   #o

   python3 start.py
   ```

2. **Ingresa tu función** en el campo de texto usando sintaxis de Python/sympy.

3. **Define el rango X** en formato `min,max` (ej: `-10,10`).

4. **Presiona Enter o el botón "Graficar"** para ver el resultado.

## 📝 Sintaxis de sumatorias

```
Sum(expresión, (variable, inicio, fin))
```

### Ejemplos:

| Expresión | Significado |
|-----------|-------------|
| `Sum(cos(pi*x*n/2), (n,1,10))` | Σ cos(π·x·n/2) desde n=1 hasta 10 |
| `Sum(n*cos(pi*x*n/2), (n,1,5))` | Σ n·cos(π·x·n/2) desde n=1 hasta 5 |
| `Sum((-4/(pi*x**2))*(cos(pi*x/2)-1)*cos(n/2), (n,1,8))` | Tu expresión compleja |

## 🧮 Funciones matemáticas disponibles

- **Trigonométricas**: `cos`, `sin`, `tan`
- **Constantes**: `pi`, `E` (número e)
- **Otras**: `sqrt`, `exp`, `log`, `abs`
- **Operadores**: `+`, `-`, `*`, `/`, `**` (potencia)

## 🖱️ Botones de ejemplo

- **Ejemplo 1**: Suma simple de cosenos
- **Ejemplo 2**: Suma con coeficientes
- **Ejemplo 3**: Tu expresión de Fourier (¡probada!)

## 🎯 Ejemplo de tu expresión

Para graficar la función que pediste:

```
Sum((-4/(pi*x**2))*(cos(pi*x/2)-1)*cos(n/2), (n,1,8))
```

1. Presiona el botón **"Ejemplo 3"**
2. Ajusta el rango X si es necesario
3. Presiona **"Graficar"**

## ⚠️ Solución de problemas

**Error "name 'sum' is not defined"**
- Usa siempre `Sum` con mayúscula (es la función de sympy)
- El programa ya maneja esto automáticamente

**No se ve la gráfica**
- Verifica que el rango X sea válido (ej: `-5,5`)
- Asegúrate de que la expresión no tenga errores de sintaxis

## 💡 Tips

- Usa el botón **"Graficar"** o presiona **Enter** en el campo de texto
- Las gráficas se generan con 500 puntos para un balance entre calidad y rendimiento
- La interfaz oscura reduce el consumo de batería en portátiles

## 📧 Contacto

**Creador:** Darian Alberto Camacho Salas  
**Email:** [xonidu@gmail.com](mailto:xonidu@gmail.com)  
**Proyecto:** XoniGraf - Para equipos de bajos recursos

---

*Optimizado para correr en ASUS Eee PC 900 con 1GB RAM y procesador Celeron M 900MHz* 🚀

