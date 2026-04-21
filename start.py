#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
XoniGraf 2026 - Lanzador Universal con Gestor de Dependencias
Graficador matemático para equipos de bajos recursos
Soporta sumatorias, series de Fourier y funciones complejas
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
    return os.path.dirname(os.path.abspath(__file__))

def get_xonigraf_path():
    """Detecta la ruta de xonigraf.py en múltiples ubicaciones"""
    script_dir = get_script_dir()
    rutas = [
        os.path.join(script_dir, 'xonigraf.py'),
        os.path.join(script_dir, 'xonigraf', 'xonigraf.py'),
        '/usr/share/xonigraf/xonigraf.py',
        os.path.join(os.path.expanduser("~"), '.xonigraf', 'xonigraf.py'),
        os.path.join(os.path.expanduser("~"), 'xonigraf', 'xonigraf.py'),
        os.path.join(os.getcwd(), 'xonigraf.py')
    ]
    for r in rutas:
        if os.path.exists(r):
            return r
    return None

def print_banner():
    sistema = get_system()
    distro = get_linux_distro()
    sistema_texto = {
        'windows': 'WINDOWS',
        'linux': f'LINUX ({distro.upper()})' if distro else 'LINUX',
        'darwin': 'MACOS'
    }.get(sistema, 'DESCONOCIDO')
    
    banner = f"""
{Colors.PURPLE}{Colors.BOLD}╔══════════════════════════════════════════════════════════╗
║                    XoniGraf 2026 v2.0                      ║
║                Graficador Matemático Ligero                 ║
║                   Optimizado para 1GB RAM                   ║
║                                                            ║
║               Sistema detectado: {sistema_texto:<27} ║
║                                                            ║
║               Desarrollado por: Darian Alberto             ║
║                      Camacho Salas                         ║
║                      Organización: XONIDU                  ║
╚══════════════════════════════════════════════════════════════╝{Colors.END}
    """
    print(banner)

def mostrar_ayuda():
    ayuda = f"""
{Colors.BOLD}USO DE XoniGraf:{Colors.END}

  xonigraf

{Colors.BOLD}CARACTERISTICAS:{Colors.END}

  ✅ Interfaz gráfica simple con Tkinter
  ✅ Soporte para sumatorias con sintaxis Sum()
  ✅ 3 ejemplos precargados
  ✅ Optimizado para 1GB RAM y procesadores lentos

{Colors.BOLD}EJEMPLOS DE EXPRESIONES:{Colors.END}

  Sum(cos(pi*x*n/2), (n,1,10))
  Sum(n*cos(pi*x*n/2), (n,1,5))
  Sum((-4/(pi*x**2))*(cos(pi*x/2)-1)*cos(n/2), (n,1,8))

{Colors.BOLD}FUNCIONES DISPONIBLES:{Colors.END}

  cos, sin, tan, sqrt, exp, log, abs, pi, E
    """
    print(ayuda)

# ============================================================================
# Verificación de dependencias
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
    return False

def install_pip_windows():
    print(f"{Colors.YELLOW}Instalando pip en Windows...{Colors.END}")
    try:
        subprocess.run([sys.executable, '-m', 'ensurepip', '--upgrade'], check=True)
        return True
    except:
        return False

def check_package(package):
    """Verifica si un paquete de Python está instalado"""
    try:
        __import__(package)
        return True
    except ImportError:
        return False

def install_package(package):
    """Instala un paquete de Python usando pip"""
    print(f"{Colors.YELLOW}Instalando {package}...{Colors.END}")
    if not check_pip():
        return False
    flags = get_install_flags()
    try:
        cmd = get_pip_command() + ['install', package] + flags
        subprocess.run(cmd, check=True, capture_output=True)
        print(f"{Colors.GREEN}{package} instalado correctamente.{Colors.END}")
        return True
    except:
        try:
            cmd = get_pip_command() + ['install', package]
            subprocess.run(cmd, check=True)
            print(f"{Colors.GREEN}{package} instalado correctamente.{Colors.END}")
            return True
        except:
            return False

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
        print(f"{Colors.YELLOW}Instala tkinter manualmente:{Colors.END}")
        print("  Ubuntu/Debian: sudo apt install python3-tk")
        print("  Arch/Manjaro: sudo pacman -S tk")
        print("  Fedora: sudo dnf install python3-tkinter")
        return False

def install_all_dependencies():
    """Instala todas las dependencias necesarias para XoniGraf"""
    dependencias = ['sympy', 'numpy', 'matplotlib']
    todas_ok = True
    
    print(f"\n{Colors.BOLD}Verificando dependencias...{Colors.END}")
    
    for dep in dependencias:
        if not check_package(dep):
            print(f"{Colors.YELLOW}⚠️ {dep} no encontrado. Instalando...{Colors.END}")
            if not install_package(dep):
                print(f"{Colors.RED}✗ No se pudo instalar {dep}{Colors.END}")
                todas_ok = False
        else:
            print(f"{Colors.GREEN}✓ {dep} disponible{Colors.END}")
    
    return todas_ok

# ============================================================================
# Gestión de configuración
# ============================================================================
def get_config_dir():
    """Devuelve el directorio de configuración de XoniGraf"""
    home = os.path.expanduser("~")
    config_dir = os.path.join(home, '.xonigraf')
    os.makedirs(config_dir, exist_ok=True)
    return config_dir

# ============================================================================
# Función principal
# ============================================================================
def main():
    if get_system() == 'windows':
        os.system('cls')
    else:
        os.system('clear')
    
    print_banner()
    
    if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help', '/?']:
        mostrar_ayuda()
        if get_system() != 'windows':
            input(f"\n{Colors.YELLOW}Presiona Enter para salir...{Colors.END}")
        return
    
    if not check_python():
        print(f"\n{Colors.RED}❌ Python no esta instalado{Colors.END}")
        sys.exit(1)
    
    ver_py = subprocess.run(get_python_command() + ['--version'], capture_output=True, text=True).stdout.strip()
    print(f"{Colors.BOLD}Python:{Colors.END} {ver_py}")
    
    if not check_pip():
        print(f"\n{Colors.YELLOW}⚠️ Pip no encontrado. Instalando...{Colors.END}")
        sistema = get_system()
        if sistema == 'linux':
            if not install_pip_linux():
                print(f"{Colors.RED}No se pudo instalar pip.{Colors.END}")
                sys.exit(1)
        elif sistema == 'windows':
            if not install_pip_windows():
                print(f"{Colors.RED}No se pudo instalar pip.{Colors.END}")
                sys.exit(1)
    else:
        print(f"{Colors.GREEN}✓ Pip disponible{Colors.END}")
    
    # Verificar tkinter (solo Linux)
    if get_system() == 'linux' and not check_tkinter():
        print(f"\n{Colors.YELLOW}⚠️ tkinter no encontrado. Instalando...{Colors.END}")
        if not install_tkinter_linux():
            print(f"{Colors.YELLOW}⚠️ tkinter no se instaló automáticamente{Colors.END}")
    else:
        print(f"{Colors.GREEN}✓ tkinter disponible{Colors.END}")
    
    # Verificar e instalar dependencias Python
    if not install_all_dependencies():
        print(f"\n{Colors.RED}❌ No se pudieron instalar todas las dependencias{Colors.END}")
        print(f"{Colors.YELLOW}Puedes instalarlas manualmente con:{Colors.END}")
        print("  pip install sympy numpy matplotlib")
        sys.exit(1)
    
    ruta_xonigraf = get_xonigraf_path()
    if not ruta_xonigraf:
        print(f"\n{Colors.RED}❌ No se encuentra xonigraf.py{Colors.END}")
        print(f"{Colors.YELLOW}Buscado en:{Colors.END}")
        print("  - Mismo directorio que start.py")
        print("  - /usr/share/xonigraf/")
        print("  - ~/.xonigraf/")
        print("  - ~/xonigraf/")
        sys.exit(1)
    
    xonigraf_dir = os.path.dirname(ruta_xonigraf)
    print(f"{Colors.GREEN}✓ xonigraf.py encontrado en: {xonigraf_dir}{Colors.END}")
    
    # Crear directorio de configuración
    config_dir = get_config_dir()
    print(f"{Colors.GREEN}✓ Directorio de configuración: {config_dir}{Colors.END}")
    
    os.chdir(xonigraf_dir)
    print(f"\n{Colors.BOLD}🚀 Iniciando XoniGraf...{Colors.END}")
    print(f"{Colors.CYAN}Para salir: cierra la ventana gráfica o presiona Ctrl+C{Colors.END}")
    print("-"*50)
    
    try:
        python_cmd = get_python_command()
        subprocess.run(python_cmd + [ruta_xonigraf])
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}🛑 Programa detenido por el usuario.{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}❌ Error: {e}{Colors.END}")
    
    print(f"\n{Colors.GREEN}Gracias por usar XoniGraf 2026{Colors.END}")
    if get_system() != 'windows':
        input(f"{Colors.YELLOW}Presiona Enter para salir...{Colors.END}")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Saliendo...{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}Error inesperado: {e}{Colors.END}")
