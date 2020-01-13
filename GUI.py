import tkinter
import oopMain
from PIL import ImageTk, Image

class App(tkinter.Tk):
	def __init__(self):
		super().__init__()
		self.title("Wikipedia Image Viewer")
		self.geometry("800x800")
		self.searchBox = SearchBox(master=self)	
		self.scrubber = oopMain.IMG_SCRUBBER
	
class SearchBox(tkinter.Label):
	def getInput(self):
		self.master.scrubber.setImageName(self.InputBox.get()) #Takes the string from the box and passes it to the scrubber
		try:
			if self.size != 0:
				self.imageSelector.delete(0,self.size())
		except tkinter.TclError: pass
		self.imageSelector.insert(0, *self.master.scrubber.getImageList())
		
	
	def __init__(self, master=None):
		super().__init__()
		self.master = master
		
		
		self.imageSelector = ImageSelection(master=self.master)
		self.InputBox = tkinter.Entry(master=self, text="Enter your text here")
		self.EnterButton = tkinter.Button(master=self, text="Search Wikipedia", command=lambda:self.getInput())
		self.EnterButton.pack(side=tkinter.RIGHT)
		self.InputBox.pack(side=tkinter.LEFT)
		self.pack(side=tkinter.BOTTOM)
		
class ImageSelection(tkinter.Listbox):
        def getNumber(self):
                index = self.index(self.curselection())
                self.master.scrubber.setImageNumber(index)
                load = self.master.scrubber.getImage()
                load.resize((400, 300))

                render = ImageTk.PhotoImage(load)
                img = tkinter.Label(self.master, image=render)
                img.image = render
                img.place(x=0, y=0)
		

        def __init__(self, master=None, width=100):
                super().__init__(master, width=width)
                self.master = master
		
                self.pack()
                self.SelectButton = tkinter.Button(master=self.master, text="Select", command=lambda:self.getNumber()).pack()
				

if __name__ == '__main__':		
	tkMaster = App()
	tkMaster.mainloop()
	
	
