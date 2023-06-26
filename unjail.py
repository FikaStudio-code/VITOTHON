import subprocess
from equipment import Equipment

global jails
jails = '/jails'
arg = "jls host.hostname".split()
jail_list = subprocess.check_output(arg).decode("utf-8").split()
for jailname in jail_list:
    target = Equipment(jailname)
    target.destroy()