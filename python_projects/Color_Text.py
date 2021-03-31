
from colorama import Fore, Back, Style
import colorama

colorama.init(autoreset=True)

s = input("Enter a String:")
print(Fore.RED+Back.YELLOW+s)
print(Fore.CYAN+Back.GREEN+s)
print(Style.DIM+s) #dim text