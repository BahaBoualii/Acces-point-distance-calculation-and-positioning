import subprocess
import re
import platform

# this function is for retrieving data from the cmd
# it returns the names and the signal strength pourcentage
# for each AP

def decouvrir_rizou():
    p = subprocess.Popen("netsh wlan show networks mode=bssid", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = p.stdout.read().decode('unicode_escape').strip()
    if platform.system() == 'Linux':
        m = re.findall('Name.*?:.*?([A-z0-9 ]*).*?Signal.*?:.*?([0-9]*)%', out, re.DOTALL)
    elif platform.system() == 'Windows':
        res = re.findall('Signal.*?:.*?([0-9]*)%', out, re.DOTALL)
        name = re.findall(r'\bSSID.*?:.*?([a-zA-Z0-9_-]*)\r', out, re.DOTALL)
    else:
        raise Exception('reached else of if statement')
    return res, name
