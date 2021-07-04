# Shutdown Computer using Python

import os

def pc_shutdown():
    os.system("shutdown /s /t 1")

pc_shutdown()