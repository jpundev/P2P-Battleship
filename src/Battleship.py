import os

try:
    import numpy
except ImportError:
    os.system("pip3 install numpy")

try:
    import netifaces
except ImportError:
    os.system("pip3 install netifaces")

os.system("python main.py")

