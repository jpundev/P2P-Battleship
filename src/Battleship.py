import os

try:
    import numpy
except ImportError:
    os.system("pip install numpy")

try:
    import netifaces
except ImportError:
    os.system("pip install netifaces")

os.system("python main.py")

