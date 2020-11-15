import os
from win10toast import ToastNotifier

class pyWinNotify:
    def __init__(self):
        # move para o diretorio do script
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        self.toast = ToastNotifier()

    def show(self, title, message, icon='icon.ico', duration=30):
        self.toast.show_toast(title, message, icon_path=icon, duration=duration)


n = pyWinNotify()
n.show('Notificação', 'Esta é um notificação padrão do Windows 10')

