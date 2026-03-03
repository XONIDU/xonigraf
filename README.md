# XONICHAT 🚀

Cliente Gemini para terminal optimizado para equipos de bajos recursos (ASUS Eee PC, etc.)

## 📋 Descripción

XONICHAT es un cliente ligero de Google Gemini que funciona completamente en terminal. Ideal para equipos con recursos limitados.

## ✨ Características

- ✅ 100% interfaz terminal - Rápido y ligero
- ✅ Múltiples API keys - Cambio automático cuando una se agota
- ✅ Historial de conversación - Contexto entre mensajes
- ✅ Optimizado - Funciona en ASUS Eee PC y equipos similares

## ⚙️ Instalación Rápida

### 1. Clonar el repositorio
```
git clone https://github.com/xonidu/xonichat.git
cd xonichat
```

### 2. Instalar dependencia por sistema operativo

#### 🐧 Arch Linux / Manjaro
```bash
sudo pacman -S python-pip
pip install requests --break-system-packages
```

#### 🐧 Debian / Ubuntu / antiX
```bash
sudo apt update
sudo apt install python3 python3-pip -y
pip3 install requests --break-system-packages
```

#### 🍎 macOS
```bash
pip3 install requests
```

#### 🪟 Windows
```bash
pip install requests
```

### 3. Configurar API keys

Obtén tus API keys gratis en: https://aistudio.google.com/app/apikey

Crea un archivo `keys.txt` en la misma carpeta con tus API keys (una por línea):
```
# Tus API keys de Gemini (una por línea)
AIzaSyCH5JpDDvI7gE87FN7iDUG5a78********
AIzaSyDYOETiQqB7od-Mzs_qC99vk9n********
```

## 🚀 Uso

```
python start.py
# o
python3 start.py
```

- Escribe tu mensaje y presiona Enter
- Escribe `/salir` para salir
- El programa cambia automáticamente de key cuando una se agota

## 📁 Archivos

- `start.py` - Programa principal
- `keys.txt` - API keys (crear manualmente)

## 👤 Autor

Darian Alberto Camacho Salas (XONIDU)

Email: xonidu@gmail.com

## 📄 Licencia

MIT License
