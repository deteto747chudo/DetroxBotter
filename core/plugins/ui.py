from core import *
from core.plugins.log import *
from core.plugins.cfg import *
import fade

class UI:
    def banner():
        banner = '''
██████╗ ███████╗████████╗██████╗  ██████╗ ██╗  ██╗
██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗╚██╗██╔╝
██║  ██║█████╗     ██║   ██████╔╝██║   ██║ ╚███╔╝ 
██║  ██║██╔══╝     ██║   ██╔══██╗██║   ██║ ██╔██╗ 
██████╔╝███████╗   ██║   ██║  ██║╚██████╔╝██╔╝ ██╗
╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝'''

        banner = pystyle.Center.XCenter(banner)
        print(fade.purpleblue(banner))