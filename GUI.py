import tkinter
import oopMain

class App(tkinter.Tk):
	def __init__(self):
		super().__init__()
		self.GUI = Display(master=self)
		pass

class Display(tkinter.Frame):
	def __init__(self, master=None ):
		super().__init__(self, master)
		self.master = master
		self.width = 500
		self.height = 500
		
	def newPhoto(self, file, **kw):
		if type(self.Photo) == PhotoViewer:
			self.Photo.destroy()
		param = {
			'file':file,
			'master' : self,
		}
		if kw:
			if 'width' in kw.keys():
				param{'width'} = kw{'width'}
			if 'height' in kw.keys():
				param{'height'} = kw{'height'}
			if 'name' in kw.keys():
				param{'name'} = kw{'name'}
				
		self.Photo = PhotoViewer(**param)
		self.Photo.pack(side=TOP)
		

class PhotoViewer(BitmapImage):
	def __init__(self, master=None, name=None, file=None):
		super().__init__(self, master, name)
		self.file = file
		self.master = master 
		self.name = name
	
	
		



if __name__ == '__main__':		
	tkMaster = App()
	tkMaster.mainloop()
	
	