"""
Program: videostoreGUI_KR.py
Python Final Project
Kevin Ryan
1/26/2024

**NOTE: the module breezypythongui.py MUST be in the same directory as this file for the app to run correctly!

GUI-based version of the Video Store rental app which calaculates a customer's total cost for however many videos they're renting.
"""

from breezypythongui import EasyFrame
from tkinter.font import Font

# Class header
class VideoStoreCalaculator(EasyFrame):

	# Definition of constructor method
	def __init__(self):
		# Call to the Easy Frame class constructor
		EasyFrame.__init__(self, title = "Video Store Calculator 2.0", background = "goldenrod", width = 700, height = 250, resizable = False)
		# variable to store a Font design for multiple labels
		labelFont = Font(family = "System", size = 20)

		# Add the widgets to the window
		self.addLabel(text = "Goldstar Video Calculator", row = 0, column = 0, sticky = "NSEW", columnspan = 2, background = "goldenrod", font = Font(family = "Terminal", size = 24) )
		self.addLabel(text = "Number of New Rentals", row = 1, column = 0, background = "goldenrod", foreground = "saddlebrown", font = labelFont)
		self.newRentals = self.addIntegerField(value = 0, row = 1, column = 1)
		self.addLabel(text = "Number of Old Rentals", row = 2, column = 0, background = "goldenrod", foreground = "saddlebrown", font = labelFont)
		self.oldRentals = self.addIntegerField(value = 0, row = 2, column = 1)

		# Add button to the window
		self.button = self.addButton(text = "Compute", row = 3, column = 0, columnspan = 2, command = self.compute)
		self.button["background"] = "palegoldenrod"
		self.button["width"] = 20
		
		# Displays the total cost when user hits compute
		self.outputLabel = self.addLabel(text = "", row = 4, column = 0, background = "goldenrod", font = labelFont)

	# Definition of the compute() function which is the event handler
	def compute(self):
		newRentals = self.newRentals.getNumber() * 3.50
		oldRentals = self.oldRentals.getNumber() * 2
		rentalCost = newRentals + oldRentals
		self.outputLabel["text"] = "The cost of this purchase is: $%0.2f" % rentalCost

# Global definition of the main() method
def main():
	# Instantiate an object from the class into mainloop()
	VideoStoreCalaculator().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
	main()