import subprocess as sp

print(sp.run(['ls -al'], shell=True, check=True))