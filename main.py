import wx
from MainFrameSat import MainFrame

#

class titi(wx.App):
    def OnInit(self):
        self.m_frame = MainFrame(None)
        self.m_frame.Show()
        self.SetTopWindow(self.m_frame)
        return True
def main():
    app = titi(0)
    app.MainLoop()

if __name__ == "__main__":
    main()
