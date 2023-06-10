#!/usr/bin/env python
import subprocess
subprocess.call("clear")
print('''
 __   __                  .                      __   __             _       
 |    |    __.  , __   ` _/_     __.  .___       |    |    __.    ___/   ___ 
 |\  /|  .'   \ |'  `. |  |    .'   \ /   \      |\  /|  .'   \  /   | .'   `
 | \/ |  |    | |    | |  |    |    | |   '      | \/ |  |    | ,'   | |----'
 /    /   `._.' /    | /  \__/  `._.' /          /    /   `._.' `___,' `.___,
                                                     `       
                                By KAMIKAZE.INK                                                      
''')

print("Listing all network interfaces:")
subprocess.call("ifconfig")
interface = input("Wireless Interface > ")

while interface =="":
	interface = input("Wireless Interface > ")

else:
	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["airmon-ng", "check", "kill"])
	subprocess.call(["iwconfig", interface, "mode", "monitor"])
	subprocess.call(["ifconfig", interface, "up"])
