# Internet Speed Test using Python
# pip command: pip install speedtest-cli

import speedtest

wifi = speedtest.Speedtest()

print("Wifi Download Speed is: ", wifi.download())
print("Wifi Upload Speed is: ", wifi.upload())