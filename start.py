#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
XoniGraf 2026 - Lanzador Universal (Robusto)
Graficador matemático para equipos de bajos recursos
Incluye instalación automática de pip, dependencias y múltiples estrategias
Desarrollador: Darian Alberto Camacho Salas
Organización: XONIDU
"""

import subprocess
import sys
import os
import platform
import shutil
import time
from pathlib import Path

# ============================================================================
# Colores para terminal
# ============================================================================
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    END = '\033[0m'
    BOLD = '\033[1m'
    
    @staticmethod
    def supports_color():
        if platform.system() == 'Windows':
            try:
                import ctypes
                kernel32 = ctypes.windll.kernel32
                return kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
            except:
                return False
        return True

if not Colors.supports_color():
    for attr in dir(Colors):
        if not attr.startswith('_') and attr != 'supports_color':
            setattr(Colors, attr, '')

# ============================================================================
# Detección del sistema
# ============================================================================
def get_system():
    return platform.system().lower()

def get_linux_distro():
    if get_system() != 'linux':
        return None
    try:
        if os.path.exists('/etc/os-release'):
            with open('/etc/os-release', 'r') as f:
                content = f.read().lower()
                if 'ubuntu' in content or 'debian' in content or 'mint' in content or 'antix' in content:
                    return 'debian-based'
                elif 'arch' in content or 'manjaro' in content:
                    return 'arch-based'
                elif 'fedora' in content:
                    return 'fedora'
                elif 'centos' in content or 'rhel' in content:
                    return 'centos'
                elif 'opensuse' in content:
                    return 'opensuse'
        if shutil.which('apt'):
            return 'debian-based'
        elif shutil.which('pacman'):
            return 'arch-based'
        elif shutil.which('dnf'):
            return 'fedora'
        elif shutil.which('yum'):
            return 'centos'
        elif shutil.which('zypper'):
            return 'opensuse'
        return 'linux-generico'
    except:
        return 'linux-generico'

def get_python_command():
    if get_system() == 'windows':
        return ['python']
    else:
        try:
            subprocess.run(['python3', '--version'], capture_output=True, check=True)
            return ['python3']
        except:
            return ['python']

def get_pip_command():
    return [sys.executable, '-m', 'pip']

def get_install_flags():
    flags = []
    sistema = get_system()
    distro = get_linux_distro()
    if sistema == 'linux':
        if distro in ['arch-based', 'fedora']:
            flags.append('--break-system-packages')
        else:
            flags.append('--user')
    elif sistema == 'darwin':
        flags.append('--user')
    return flags

def get_script_dir():
    """Obtiene el directorio donde está guardado este script (start.py)"""
    return os.path.dirname(os.path.abspath(__file__))

def get_fixed_xonigraf_dir():
    """Devuelve la ruta fija /home/usuario/xonigraf/"""
    usuario = os.path.expanduser("~")
    nombre_usuario = os.path.basename(usuario)
    return os.path.join('/home', nombre_usuario, 'xonigraf')

def get_xonigraf_path():
    """
    Detecta la ruta de xonigraf.py:
    1. Primero busca en el mismo directorio que start.py
    2. Si no, busca en la carpeta xonigraf/
    3. Si no, usa la ruta fija /home/usuario/xonigraf/
    """
    script_dir = get_script_dir()
    
    # Opción 1: Mismo directorio
    ruta_local = os.path.join(script_dir, 'xonigraf.py')
    if os.path.exists(ruta_local):
        return ruta_local, 'local'
    
    # Opción 2: Subcarpeta xonigraf/
    ruta_subcarpeta = os.path.join(script_dir, 'xonigraf', 'xonigraf.py')
    if os.path.exists(ruta_subcarpeta):
        return ruta_subcarpeta, 'subcarpeta'
    
    # Opción 3: Ruta fija
    ruta_fija = os.path.join(get_fixed_xonigraf_dir(), 'xonigraf.py')
    if os.path.exists(ruta_fija):
        return ruta_fija, 'fija'
    
    # Si no existe en ningún lado, devolvemos la local como predeterminada
    return ruta_local, 'ninguna'

def get_xonigraf_dir():
    """Devuelve el directorio donde está xonigraf.py"""
    ruta, _ = get_xonigraf_path()
    return os.path.dirname(ruta)

def print_banner():
    sistema = get_system()
    distro = get_linux_distro()
    ruta_xonigraf, origen = get_xonigraf_path()
    sistema_texto = {
        'windows': 'WINDOWS',
        'linux': f'LINUX ({distro.upper()})' if distro else 'LINUX',
        'darwin': 'MACOS'
    }.get(sistema, 'DESCONOCIDO')
    
    origen_texto = {
        'local': 'MISMO DIRECTORIO',
        'subcarpeta': 'SUBCARPETA xonigraf/',
        'fija': '/HOME/USUARIO/XONIGRAF',
        'ninguna': 'NO ENCONTRADO'
    }.get(origen, 'DESCONOCIDO')
    
    banner = f"""
{Colors.PURPLE}{Colors.BOLD}╔══════════════════════════════════════════════════════════╗
║                    XoniGraf 2026 v2.0                      ║
║                Graficador Matemático Ligero                 ║
║                   Optimizado para 1GB RAM                   ║
║                                                            ║
║               Sistema detectado: {sistema_texto:<27} ║
║               Origen xonigraf.py: {origen_texto:<27} ║
║                                                            ║
║               Desarrollado por: Darian Alberto             ║
║                      Camacho Salas                         ║
║                      Organización: XONIDU                  ║
╚══════════════════════════════════════════════════════════════╝{Colors.END}
    """
    print(banner)

# ============================================================================
# Verificación e instalación de pip
# ============================================================================
def check_python():
    try:
        cmd = get_python_command() + ['--version']
        subprocess.run(cmd, capture_output=True, check=True)
        return True
    except:
        return False

def check_pip():
    try:
        cmd = get_pip_command() + ['--version']
        subprocess.run(cmd, capture_output=True, check=True)
        return True
    except:
        return False

def install_pip_linux():
    distro = get_linux_distro()
    print(f"{Colors.YELLOW}Instalando pip en Linux ({distro})...{Colors.END}")
    if distro == 'debian-based':
        try:
            subprocess.run(['sudo', 'apt', 'update'], check=False)
            subprocess.run(['sudo', 'apt', 'install', '-y', 'python3-pip'], check=True)
            return True
        except:
            return False
    elif distro == 'arch-based':
        try:
            subprocess.run(['sudo', 'pacman', '-S', '--noconfirm', 'python-pip'], check=True)
            return True
        except:
            return False
    elif distro == 'fedora':
        try:
            subprocess.run(['sudo', 'dnf', 'install', '-y', 'python3-pip'], check=True)
            return True
        except:
            return False
    elif distro == 'centos':
        try:
            subprocess.run(['sudo', 'yum', 'install', '-y', 'python3-pip'], check=True)
            return True
        except:
            return False
    elif distro == 'opensuse':
        try:
            subprocess.run(['sudo', 'zypper', 'install', '-y', 'python3-pip'], check=True)
            return True
        except:
            return False
    return False

def install_pip_windows():
    print(f"{Colors.YELLOW}Instalando pip en Windows...{Colors.END}")
    try:
        subprocess.run([sys.executable, '-m', 'ensurepip', '--upgrade'], check=True)
        return True
    except:
        try:
            import urllib.request
            urllib.request.urlretrieve('https://bootstrap.pypa.io/get-pip.py', 'get-pip.py')
            subprocess.run([sys.executable, 'get-pip.py'], check=True)
            os.remove('get-pip.py')
            return True
        except:
            return False

# ============================================================================
# Instalación de dependencias Python
# ============================================================================
def check_package(package):
    """Verifica si un paquete de Python está instalado"""
    try:
        __import__(package)
        return True
    except ImportError:
        return False

def install_package(package):
    """Instala un paquete de Python usando pip con los flags adecuados"""
    print(f"{Colors.YELLOW}Instalando {package}...{Colors.END}")
    
    if not check_pip():
        print(f"{Colors.RED}No se encontró pip. Instálalo primero.{Colors.END}")
        return False
    
    flags = get_install_flags()
    try:
        cmd = get_pip_command() + ['install', package] + flags
        subprocess.run(cmd, check=True, capture_output=True)
        print(f"{Colors.GREEN}{package} instalado correctamente.{Colors.END}")
        return True
    except:
        # Intentar sin flags
        try:
            cmd = get_pip_command() + ['install', package]
            subprocess.run(cmd, check=True)
            print(f"{Colors.GREEN}{package} instalado correctamente.{Colors.END}")
            return True
        except Exception as e:
            print(f"{Colors.RED}Error instalando {package}: {e}{Colors.END}")
            return False

def install_all_dependencies():
    """Instala todas las dependencias necesarias para XoniGraf"""
    dependencias = ['sympy', 'numpy', 'matplotlib']
    todas_ok = True
    
    for dep in dependencias:
        if not check_package(dep):
            print(f"\n{Colors.YELLOW}⚠️ {dep} no encontrado. Instalando...{Colors.END}")
            if not install_package(dep):
                print(f"{Colors.RED}Fallo crítico: no se pudo instalar {dep}. Abortando.{Colors.END}")
                todas_ok = False
        else:
            print(f"{Colors.GREEN}✓ {dep} disponible{Colors.END}")
    
    return todas_ok

# ============================================================================
# Verificación de tkinter (dependencia del sistema)
# ============================================================================
def check_tkinter():
    """Verifica si tkinter está disponible"""
    try:
        python_cmd = get_python_command()
        result = subprocess.run(python_cmd + ['-c', 'import tkinter'], 
                               capture_output=True, timeout=2)
        return result.returncode == 0
    except:
        return False

def install_tkinter_linux():
    """Instala tkinter en Linux según la distribución"""
    distro = get_linux_distro()
    print(f"{Colors.YELLOW}Instalando tkinter en Linux ({distro})...{Colors.END}")
    
    if distro == 'debian-based':
        try:
            subprocess.run(['sudo', 'apt', 'update'], check=False)
            subprocess.run(['sudo', 'apt', 'install', '-y', 'python3-tk'], check=True)
            return True
        except:
            return False
    elif distro == 'arch-based':
        try:
            subprocess.run(['sudo', 'pacman', '-S', '--noconfirm', 'tk'], check=True)
            return True
        except:
            return False
    elif distro == 'fedora':
        try:
            subprocess.run(['sudo', 'dnf', 'install', '-y', 'python3-tkinter'], check=True)
            return True
        except:
            return False
    else:
        print(f"{Colors.YELLOW}No se pudo instalar tkinter automáticamente.{Colors.END}")
        print("  Instálalo manualmente:")
        print("    Ubuntu/Debian: sudo apt install python3-tk")
        print("    Arch/Manjaro: sudo pacman -S tk")
        print("    Fedora: sudo dnf install python3-tkinter")
        return False

# ============================================================================
# Verificación de xonigraf.py y ejecución
# ============================================================================
def check_xonigraf():
    ruta, origen = get_xonigraf_path()
    existe = os.path.exists(ruta)
    if not existe:
        print(f"{Colors.RED}❌ No se encuentra xonigraf.py{Colors.END}")
        print(f"   Buscado en: {ruta}")
    return existe

def mostrar_ayuda():
    """Muestra ayuda de uso"""
    ayuda = f"""
{Colors.BOLD}USO DE XoniGraf:{Colors.END}

  python start.py

{Colors.BOLD}DESCRIPCION:{Colors.END}

  XoniGraf es un graficador matemático ligero que permite visualizar
  funciones complejas, incluyendo sumatorias y series de Fourier,
  optimizado para equipos de bajos recursos como ASUS Eee PC.

{Colors.BOLD}CARACTERISTICAS:{Colors.END}

  ✅ Interfaz gráfica simple con Tkinter
  ✅ Soporte para sumatorias con sintaxis Sum()
  ✅ 3 ejemplos precargados
  ✅ Optimizado para 1GB RAM y procesadores lentos

{Colors.BOLD}EJEMPLOS DE EXPRESIONES:{Colors.END}

  Sum(cos(pi*x*n/2), (n,1,10))
  Sum(n*cos(pi*x*n/2), (n,1,5))
  Sum((-4/(pi*x**2))*(cos(pi*x/2)-1)*cos(n/2), (n,1,8))
    """
    print(ayuda)

def main():
    # Limpiar pantalla
    if get_system() == 'windows':
        os.system('cls')
    else:
        os.system('clear')
    
    print_banner()
    
    # Verificar argumentos de ayuda
    if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help', '/?']:
        mostrar_ayuda()
        if get_system() != 'windows':
            input(f"\n{Colors.YELLOW}Presiona Enter para salir...{Colors.END}")
        return
    
    sistema = get_system()
    distro = get_linux_distro()
    script_dir = get_script_dir()
    ruta_xonigraf, origen = get_xonigraf_path()
    xonigraf_dir = get_xonigraf_dir()
    
    print(f"{Colors.BOLD}Sistema operativo:{Colors.END} {sistema}")
    if distro:
        print(f"{Colors.BOLD}Distribución:{Colors.END} {distro}")
    print(f"{Colors.BOLD}Directorio de start.py:{Colors.END} {script_dir}")
    print(f"{Colors.BOLD}Origen de xonigraf.py:{Colors.END} {origen}")
    print(f"{Colors.BOLD}Ruta de xonigraf.py:{Colors.END} {ruta_xonigraf}")
    
    # Crear directorio si es necesario (solo para ruta fija)
    if origen == 'ninguna' and not os.path.exists(xonigraf_dir):
        print(f"\n{Colors.YELLOW}⚠️ El directorio {xonigraf_dir} no existe. Creándolo...{Colors.END}")
        os.makedirs(xonigraf_dir, exist_ok=True)
        print(f"{Colors.GREEN}✓ Directorio creado: {xonigraf_dir}{Colors.END}")
    
    # Verificar Python
    if not check_python():
        print(f"\n{Colors.RED}❌ Python no está instalado o no está en el PATH.{Colors.END}")
        print("   Descarga Python desde: https://www.python.org/downloads/")
        sys.exit(1)
    
    # Mostrar versión de Python
    ver_py = subprocess.run(get_python_command() + ['--version'], capture_output=True, text=True).stdout.strip()
    print(f"{Colors.BOLD}Python:{Colors.END} {ver_py}")
    
    # Verificar pip e instalarlo si falta
    if not check_pip():
        print(f"\n{Colors.YELLOW}⚠️ Pip no encontrado. Instalando...{Colors.END}")
        if sistema == 'linux':
            if not install_pip_linux():
                print(f"{Colors.RED}No se pudo instalar pip. Instálalo manualmente.{Colors.END}")
                sys.exit(1)
        elif sistema == 'windows':
            if not install_pip_windows():
                print(f"{Colors.RED}No se pudo instalar pip. Ejecuta como administrador.{Colors.END}")
                sys.exit(1)
        else:
            print(f"{Colors.YELLOW}Instala pip manualmente con: python -m ensurepip --upgrade{Colors.END}")
            sys.exit(1)
    else:
        print(f"{Colors.GREEN}✓ Pip disponible{Colors.END}")
    
    # Verificar e instalar tkinter (solo Linux)
    if sistema == 'linux' and not check_tkinter():
        print(f"\n{Colors.YELLOW}⚠️ tkinter no encontrado. Instalando...{Colors.END}")
        if not install_tkinter_linux():
            print(f"{Colors.YELLOW}⚠️ tkinter no se instaló automáticamente. Instálalo manualmente si es necesario.{Colors.END}")
    else:
        print(f"{Colors.GREEN}✓ tkinter disponible{Colors.END}")
    
    # Verificar e instalar dependencias Python
    if not install_all_dependencies():
        print(f"{Colors.RED}Fallo crítico: no se pudieron instalar todas las dependencias. Abortando.{Colors.END}")
        sys.exit(1)
    
    # Verificar que existe xonigraf.py
    if not check_xonigraf():
        print(f"\n{Colors.RED}❌ Error crítico: No se encuentra xonigraf.py{Colors.END}")
        if origen == 'ninguna':
            print(f"   Puedes copiar xonigraf.py a:")
            print(f"     - {script_dir} (donde está start.py)")
            print(f"     - O a {get_fixed_xonigraf_dir()}")
        sys.exit(1)
    
    # Cambiar al directorio de xonigraf.py
    os.chdir(xonigraf_dir)
    print(f"{Colors.GREEN}✓ Cambiando al directorio: {xonigraf_dir}{Colors.END}")
    
    # Ejecutar xonigraf.py
    print(f"\n{Colors.BOLD}🚀 Iniciando XoniGraf...{Colors.END}")
    print(f"{Colors.CYAN}Para salir: cierra la ventana gráfica o presiona Ctrl+C{Colors.END}")
    print("-"*50)
    try:
        python_cmd = get_python_command()
        subprocess.run(python_cmd + ['xonigraf.py'])
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}🛑 Programa detenido por el usuario.{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}❌ Error ejecutando xonigraf.py: {e}{Colors.END}")
    
    print(f"\n{Colors.GREEN}Gracias por usar XoniGraf 2026{Colors.END}")
    if sistema != 'windows':
        input(f"{Colors.YELLOW}Presiona Enter para salir...{Colors.END}")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Saliendo...{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}Error inesperado: {e}{Colors.END}")
