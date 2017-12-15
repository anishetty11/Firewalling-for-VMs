
"""
Create a GUI application which allows the user to either
block/unblock particular sites. The user can block/unblock 
the sites either by IP addresses or domain names.
The blocked domains are stored in a file named "fw_rules.txt"
User can also view the list of blocked IPs/Domains using the 
display option 

"""



from Tkinter import *
import logging
import socket

logging.basicConfig(level="DEBUG")
logger=logging.getLogger()


def block_ip():
	"""
	The function gets invoked when the user presses the
	"Block" button. It converts the Domain name, and places 
	it in the file named "fw_rules.txt"

	"""

	data=temp_data.get()
	all_ips=data.split(";")
	file_ips=[]
	with open("fw_rules.txt","r") as fw:
		file_data=fw.read()
		file_ips=file_data.split('\n')
	with open("fw_rules.txt","a+") as fw:
		for i in all_ips:
			i=socket.gethostbyname(i)
			print (i)
			if i not in file_ips:
				fw.write('\n'+i)
				
			
		
def unblock_ip():
	"""
	The function gets invoked when the user presses the
	"Unbnlock" button. It converts the Domain name, and removes
	the entry in the file named "fw_rules.txt" if any

	"""
	
	data=temp_data.get()
	all_ips=data.split(";")
	file_data=[]
	with open("fw_rules.txt") as fw:
		file_data=fw.read()
	
	with open("fw_rules.txt","w+") as fw:
		for i in all_ips:
			i=socket.gethostbyname(i)
			print (i)
			file_data=file_data.replace('\n'+i,'')
		fw.write(file_data)

def display_ip():
	"""
	The function gets invoked when the user presses the
	"Display" button. It displays the domain names which 
	are blocked as per the "fw_rules.txt" file.

	"""
	with open("fw_rules.txt","r") as fw:
		file_data=fw.read()
		print ("\n")
		print ("List of blocked sites")
		file_ips=file_data.split('\n')
		print ("\n".join(file_ips[1:]))
	

# initalize the GUI parameters
root = Tk()
root.geometry('570x300')
topFrame = Frame()
temp_data=StringVar()
topFrame.pack()

# initalize the buttons and text entries
block_button= Button(topFrame,text="Enable Firewall",command=block_ip,height=5,width=20)
unblock_button= Button(topFrame,text="Disable Firewall",command=unblock_ip,height=5,width=20)
display_button= Button(topFrame,text="Display",command=display_ip,height=5,width=20)
text_field= Entry(topFrame,textvariable=temp_data,width=100,font=('Verdana',30)).pack()


# delpoy the buttons onto the frame
block_button.pack(side="left")
unblock_button.pack(side="left")
display_button.pack(side="left")
root.mainloop()
