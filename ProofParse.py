import re
import sys
import os

try:
	import pyperclip
except:
	print("Installing pyperclip...")
	os.system('pip install pyperclip')
	print()
	os.system('python ProofParse.py')	#Simulate relaunch by launching a nested python session. Pyperclip doesn't work without a relaunch.
	os.exit()							#Close original session when exiting out of nested session.

def ParseLink():
	link = input("Proofpoint link: ")
	print()
	if "proofpoint" in link:
		startReg = re.compile("url\?u=").search(link)
		endReg = re.compile("(&d=|&amp;d=)").search(link)
		
		newLink = link[startReg.end():endReg.start()]
		
		newLink = newLink.replace('_','/')
		for item in URLEncoding.items():
			if item[1] in newLink:
				newLink = newLink.replace(item[1],item[0])
		
		print(newLink)
		
		if newLink.find("?") != -1:
			newLink = newLink[:newLink.find("?")]
			print(newLink)
		
		try:
			pyperclip.copy(newLink)
			print("URL copied to clipboard.")
		except:
			print("", end="")
			#print("URL not copied to clipboard.")
		
		print()
		ParseLink()
	else:
		print("ERROR parsing URL.")
		print()
		ParseLink()
		
global URLEncoding
URLEncoding = {" ":"-20","!":"-21",'"':"-22","#":"-23","$":"-24","%":"-25","&":"-26","'":"-27","(":"-28",")":"-29","*":"-2A","+":"-2B",",":"-2C",".":"-2E","/":"-2F","0":"-30","1":"-31","2":"-32","3":"-33","4":"-34","5":"-35","6":"-36","7":"-37","8":"-38","9":"-39",":":"-3A",";":"-3B","<":"-3C","=":"-3D",">":"-3E","?":"-3F","@":"-40","A":"-41","B":"-42","C":"-43","D":"-44","E":"-45","F":"-46","G":"-47","H":"-48","I":"-49","J":"-4A","K":"-4B","L":"-4C","M":"-4D","N":"-4E","O":"-4F","P":"-50","Q":"-51","R":"-52","S":"-53","T":"-54","U":"-55","V":"-56","W":"-57","X":"-58","Y":"-59","Z":"-5A","[":"-5B","\\":"-5C","]":"-5D","^":"-5E","_":"-5F","`":"-60","a":"-61","b":"-62","c":"-63","d":"-64","e":"-65","f":"-66","g":"-67","h":"-68","i":"-69","j":"-6A","k":"-6B","l":"-6C","m":"-6D","n":"-6E","o":"-6F","p":"-70","q":"-71","r":"-72","s":"-73","t":"-74","u":"-75","v":"-76","w":"-77","x":"-78","y":"-79","z":"-7A","{":"-7B","|":"-7C","}":"-7D","~":"-7E","-":"-2D"}
ParseLink()