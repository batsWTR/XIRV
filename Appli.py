#
from tkinter import *


class Appli:
	def __init__(self):
		self.ip = "aa"
		self.port = "9999"
		self.confFile = ""
		self.fenetre = Tk()
		self.fenetre.title("XIRV")
		#self.fenetre.size("800x600")
		# Frame 1
		self.frame1 = Frame(self.fenetre)
		self.frame1.pack(side=TOP, padx=30, pady=30)
		# Bouton connect
		self.bConnection = Button(self.frame1, text="Connect", command=self.Connexion)
		self.bConnection.pack(side=BOTTOM)
		# entree IP
		self.entreeIP = Entry(self.frame1, textvariable=self.ip, width=15, text="ip")
		self.entreeIP.pack(side=LEFT)
		# Entree port
		self.entreePort = Entry(self.frame1, textvariable=self.port, width=5)
		self.entreePort.pack(side=RIGHT)
		# Frame 2
		self.frame2 = Frame(self.fenetre)
		self.frame2.pack(side=BOTTOM, padx=30, pady=30)
		# liste 1
		self.list1 = Listbox(self.frame2)
		self.list1.pack(side=LEFT)
		# liste 2
		self.list2 = Listbox(self.frame2)
		self.list2.pack(side=RIGHT)
	def launch(self):
		self.fenetre.mainloop()
	# Fonction du bouton Connect
	def Connexion(self):
		print("Connexion..")
		# recuperation ip et port
		self.ip = self.entreeIP.get()
		self.port = self.entreePort.get()
		print("IP: ",self.ip)
		print("Port: ",self.port)
	# Fichier de conf des variables IOCP
	def LoadConfFile(self):
		pass



