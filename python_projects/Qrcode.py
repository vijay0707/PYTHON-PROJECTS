# QR CODE GENERATOR
 
import pyqrcode

# paste the link that to be converted

link = input("PASTE THE LINK: ")

# Generate QR Code

url = pyqrcode.create(link)

# create and save the png file 

fname = input("Enter the File name: ")

url.svg(fname+".svg", scale = 8)