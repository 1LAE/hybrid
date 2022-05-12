import wx

class MainFrame(wx.Frame):
	def __init__(self):
		super().__init__(parent = None, title = 'HybridController')
		self.Show()

if __name__ == '__main__':
	app = wx.App()
	frame = MainFrame()
	app.MainLoop()
