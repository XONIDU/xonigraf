"""
XoniGraf 2026 - Lanzador Universal
Este script es el ENCARGADO de ejecutar xonigraf.py
Detecta automáticamente el sistema y verifica dependencias
Desarrollado por: Darian Alberto Camacho Salas
"""

import subprocess
import sys
import os
import platform
import shutil
import time

# Colores para terminal
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    
    @staticmethod
    def supports_color():
        """Verifica si la terminal soporta colores"""
        if platform.system() == 'Windows':
            try:
                import ctypes
                kernel32 = ctypes.windll.kernel32
                return kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
            except:
                return False
        return True

# Desactivar colores si no hay soporte
if not Colors.supports_color():
    for attr in dir(Colors):
        if not attr.startswith('_') and attr != 'supports_color':
            setattr(Colors, attr, '')

def get_system():
    """Detecta el sistema operativo"""
    return platform.system().lower()

def get_linux_distro():
    """Detecta la distribución de Linux específica"""
    if get_system() != 'linux':
        return None
    
    try:
        if os.path.exists('/etc/os-release'):
            with open('/etc/os-release', 'r') as f:
                content = f.read().lower()
                if 'ubuntu' in content:
                    return 'ubuntu'
                elif 'debian' in content:
                    return 'debian'
                elif 'fedora' in content:
                    return 'fedora'
                elif 'centos' in content:
                    return 'centos'
                elif 'arch' in content:
                    return 'arch'
                elif 'manjaro' in content:
                    return 'manjaro'
                elif 'mint' in content:
                    return 'mint'
                elif 'antix' in content:
                    return 'antix'
        return 'linux-generico'
    except:
        return 'linux-generico'

def get_python_command():
    """Obtiene el comando Python correcto"""
    if get_system() == 'windows':
        return ['python']
    else:
        try:
            subprocess.run(['python3', '--version'], capture_output=True, check=True)
            return ['python3']
        except:
            return ['python']

def print_banner():
    """Muestra el banner de XoniGraf"""
    sistema = get_system()
    distro = get_linux_distro()
    
    sistema_texto = {
        'windows': 'WINDOWS',
        'linux': f'LINUX ({distro.upper()})' if distro else 'LINUX',
        'darwin': 'MACOS'
    }.get(sistema, 'DESCONOCIDO')
    
    banner = f"""
{Colors.BLUE}{Colors.BOLD}╔═════════════════════════════════════════════════════════╗
║                     XoniGraf 2026 v1.0                     ║
║                 Graficador Matemático Ligero               ║
║                Para equipos de bajos recursos              ║
║                                                            ║
               Sistema detectado: {sistema_texto}           
║                                                            ║
║               Desarrollado por: Darian Alberto             ║
║                      Camacho Salas                         ║
╚════════════════════════════════════════════════════════════╝{Colors.END}
    """
    print(banner)

def check_python():
    """Verifica que Python está instalado"""
    try:
        cmd = get_python_command() + ['--version']
        subprocess.run(cmd, capture_output=True, check=True)
        return True
    except:
        return False

def check_command(comando):
    """Verifica si un comando existe en el sistema"""
    return shutil.which(comando) is not None

def check_python_package(package):
    """Verifica si un paquete de Python está instalado"""
    try:
        python_cmd = get_python_command()
        subprocess.run(python_cmd + ['-c', f'import {package}'], 
                      capture_output=True, check=True)
        return True
    except:
        return False

def check_tkinter():
    """Verifica específicamente tkinter"""
    try:
        python_cmd = get_python_command()
        result = subprocess.run(python_cmd + ['-c', 'import tkinter; tkinter._test()'], 
                               capture_output=True, timeout=2)
        return result.returncode == 0
    except:
        return False

def check_dependencies():
    """Verifica las dependencias necesarias para xonigraf.py"""
    print(f"\n{Colors.BOLD}Verificando dependencias para XoniGraf...{Colors.END}")
    
    # Verificar tkinter (viene con Python pero a veces falta en Linux)
    tkinter_ok = check_tkinter()
    if tkinter_ok:
        print(f"{Colors.GREEN}  - tkinter OK{Colors.END}")
    else:
        print(f"{Colors.YELLOW}  - tkinter (faltante en el sistema){Colors.END}")
    
    # Verificar paquetes Python
    sympy_ok = check_python_package('sympy')
    numpy_ok = check_python_package('numpy')
    matplotlib_ok = check_python_package('matplotlib')
    
    if sympy_ok:
        print(f"{Colors.GREEN}  - sympy OK{Colors.END}")
    else:
        print(f"{Colors.YELLOW}  - sympy (faltante){Colors.END}")
    
    if numpy_ok:
        print(f"{Colors.GREEN}  - numpy OK{Colors.END}")
    else:
        print(f"{Colors.YELLOW}  - numpy (faltante){Colors.END}")
    
    if matplotlib_ok:
        print(f"{Colors.GREEN}  - matplotlib OK{Colors.END}")
    else:
        print(f"{Colors.YELLOW}  - matplotlib (faltante){Colors.END}")
    
    return tkinter_ok, sympy_ok, numpy_ok, matplotlib_ok

def install_tkinter_linux(distro):
    """Instala tkinter en Linux"""
    print(f"\n{Colors.BOLD}Instalando tkinter...{Colors.END}")
    
    if distro in ['ubuntu', 'debian', 'mint', 'antix']:
        cmd = ['sudo', 'apt', 'install', '-y', 'python3-tk']
    elif distro in ['arch', 'manjaro']:
        cmd = ['sudo', 'pacman', '-S', '--noconfirm', 'tk']
    elif distro in ['fedora']:
        cmd = ['sudo', 'dnf', 'install', '-y', 'python3-tkinter']
    else:
        print(f"{Colors.YELLOW}Distribución no reconocida. Instala tkinter manualmente.{Colors.END}")
        print(f"  Ubuntu/Debian: sudo apt install python3-tk")
        print(f"  Arch/Manjaro: sudo pacman -S tk")
        return False
    
    try:
        print(f"Ejecutando: {' '.join(cmd)}")
        subprocess.run(cmd, check=True)
        print(f"{Colors.GREEN}tkinter instalado correctamente{Colors.END}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"{Colors.RED}Error en la instalación: {e}{Colors.END}")
        return False

def install_python_packages(packages):
    """Instala paquetes de Python"""
    python_cmd = get_python_command()
    
    for package in packages:
        print(f"Instalando {package}...")
        try:
            # Usar --break-system-packages en Linux, en Windows no
            if get_system() == 'linux':
                subprocess.run(python_cmd + ['-m', 'pip', 'install', '--user', package, '--break-system-packages'], 
                             check=True, capture_output=True)
            else:
                subprocess.run(python_cmd + ['-m', 'pip', 'install', '--user', package], 
                             check=True, capture_output=True)
            print(f"{Colors.GREEN}  ✓ {package} instalado{Colors.END}")
        except subprocess.CalledProcessError as e:
            print(f"{Colors.RED}  ✗ Error instalando {package}{Colors.END}")
            # Segundo intento sin --break-system-packages
            try:
                print(f"Reintentando sin --break-system-packages...")
                subprocess.run(python_cmd + ['-m', 'pip', 'install', '--user', package], 
                             check=True, capture_output=True)
                print(f"{Colors.GREEN}  ✓ {package} instalado en segundo intento{Colors.END}")
            except:
                return False
    return True

def mostrar_instrucciones_python():
    """Muestra instrucciones para instalar Python"""
    sistema = get_system()
    
    if sistema == 'windows':
        print("   Descarga Python desde: https://www.python.org/downloads/")
        print("   IMPORTANTE: Al instalar, marca 'Add Python to PATH'")
    elif sistema == 'linux':
        distro = get_linux_distro()
        if distro in ['ubuntu', 'debian', 'mint', 'antix']:
            print("   sudo apt update")
            print("   sudo apt install python3 python3-pip python3-venv")
        elif distro in ['arch', 'manjaro']:
            print("   sudo pacman -S python python-pip")
        else:
            print("   Instala Python 3 desde: https://www.python.org/downloads/")
    elif sistema == 'darwin':
        print("   Instala con: brew install python3")
        print("   O descarga desde: https://www.python.org/downloads/")

def crear_accesos_directos():
    """Crea accesos directos según el sistema"""
    sistema = get_system()
    
    if sistema == 'windows':
        # Crear .bat para Windows
        with open('INICIAR_XONIGRAF.bat', 'w') as f:
            f.write("""@echo off
title XoniGraf 2026 - Graficador Matemático
color 1F
echo ========================================
echo      XoniGraf 2026 - Graficador Matemático
echo      Para equipos de bajos recursos
echo      Desarrollado por Darian Alberto
echo ========================================
echo.
python start.py
pause
""")
        print(f"{Colors.GREEN}Creado INICIAR_XONIGRAF.bat - Haz doble clic para ejecutar{Colors.END}")
    
    elif sistema == 'linux':
        # Crear .sh para Linux
        with open('INICIAR_XONIGRAF.sh', 'w') as f:
            f.write("""#!/bin/bash
echo "========================================"
echo "      XoniGraf 2026 - Graficador Matemático"
echo "      Para equipos de bajos recursos"
echo "      Desarrollado por Darian Alberto"
echo "========================================"
echo ""
python3 start.py
read -p "Presiona Enter para salir"
""")
        os.chmod('INICIAR_XONIGRAF.sh', 0o755)
        print(f"{Colors.GREEN}Creado INICIAR_XONIGRAF.sh - Ejecuta con: ./INICIAR_XONIGRAF.sh{Colors.END}")
    
    elif sistema == 'darwin':
        # Crear .command para Mac
        with open('INICIAR_XONIGRAF.command', 'w') as f:
            f.write("""#!/bin/bash
cd "$(dirname "$0")"
echo "========================================"
echo "      XoniGraf 2026 - Graficador Matemático"
echo "      Para equipos de bajos recursos"
echo "      Desarrollado por Darian Alberto"
echo "========================================"
echo ""
python3 start.py
""")
        os.chmod('INICIAR_XONIGRAF.command', 0o755)
        print(f"{Colors.GREEN}Creado INICIAR_XONIGRAF.command - Haz doble clic para ejecutar{Colors.END}")

def main():
    """Función principal - Ejecuta xonigraf.py"""
    # Limpiar pantalla según sistema
    if get_system() == 'windows':
        os.system('cls')
    else:
        os.system('clear')
    
    # Mostrar banner
    print_banner()
    
    sistema = get_system()
    distro = get_linux_distro()
    
    # Verificar Python
    if not check_python():
        print(f"\n{Colors.RED}Error: Python no está instalado{Colors.END}")
        mostrar_instrucciones_python()
        input(f"\n{Colors.YELLOW}Presiona Enter para salir...{Colors.END}")
        return
    
    python_version = subprocess.run(get_python_command() + ['--version'], 
                                   capture_output=True, text=True).stdout.strip()
    print(f"{Colors.BOLD}Python:{Colors.END} {python_version}")
    print(f"{Colors.BOLD}Ruta:{Colors.END} {os.path.dirname(os.path.abspath(__file__))}")
    
    # Verificar dependencias
    tkinter_falta, sympy_falta, numpy_falta, matplotlib_falta = check_dependencies()
    
    # Instalar tkinter si falta (solo Linux)
    if sistema == 'linux' and not tkinter_falta:
        print(f"\n{Colors.YELLOW}Falta tkinter (dependencia del sistema){Colors.END}")
        respuesta = input("Instalar tkinter automáticamente? (s/n): ")
        if respuesta.lower() == 's':
            if install_tkinter_linux(distro):
                time.sleep(1)
            else:
                print(f"\n{Colors.YELLOW}Puedes instalarlo manualmente:{Colors.END}")
                if distro in ['ubuntu', 'debian', 'mint', 'antix']:
                    print("  sudo apt install python3-tk")
                elif distro in ['arch', 'manjaro']:
                    print("  sudo pacman -S tk")
    
    # Instalar paquetes Python faltantes
    paquetes_instalar = []
    
    if sympy_falta:
        paquetes_instalar.append('sympy')
    if numpy_falta:
        paquetes_instalar.append('numpy')
    if matplotlib_falta:
        paquetes_instalar.append('matplotlib')
    
    if paquetes_instalar:
        print(f"\n{Colors.YELLOW}Faltan paquetes de Python: {', '.join(paquetes_instalar)}{Colors.END}")
        respuesta = input("Instalar automáticamente? (s/n): ")
        if respuesta.lower() == 's':
            install_python_packages(paquetes_instalar)
    
    # Verificar que existe xonigraf.py
    if not os.path.exists('xonigraf.py'):
        print(f"\n{Colors.RED}Error: No se encuentra xonigraf.py{Colors.END}")
        print(f"   Archivos encontrados: {', '.join(os.listdir('.')[:5])}")
        input(f"\n{Colors.YELLOW}Presiona Enter para salir...{Colors.END}")
        return
    
    print(f"\n{Colors.BOLD}Iniciando XoniGraf...{Colors.END}")
    print(f"{Colors.BOLD}Para salir:{Colors.END} Ctrl+C o cierra la ventana")
    print("-" * 60)
    
    # Ejecutar xonigraf.py
    try:
        python_cmd = get_python_command()
        subprocess.run(python_cmd + ['xonigraf.py'])
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Programa detenido por el usuario{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}Error ejecutando xonigraf.py: {e}{Colors.END}")
    
    print(f"\n{Colors.BLUE}Gracias por usar XoniGraf 2026{Colors.END}")
    print(f"{Colors.BLUE}Desarrollado por Darian Alberto Camacho Salas{Colors.END}")
    
    if sistema != 'windows':
        input(f"\n{Colors.YELLOW}Presiona Enter para salir...{Colors.END}")

if __name__ == '__main__':
    try:
        # Crear accesos directos
        crear_accesos_directos()
        
        # Ejecutar programa principal
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Saliendo...{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}Error inesperado: {e}{Colors.END}")
        input(f"\n{Colors.YELLOW}Presiona Enter para salir...{Colors.END}")
