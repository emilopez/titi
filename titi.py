import wx
from MainFrameBase import MainFrameBase

# titi launcher

class titi(wx.App):
    def OnInit(self):
        self.m_frame = MainFrameBase(None)
        self.m_frame.Show()
        self.SetTopWindow(self.m_frame)
        return True

def main():
    app = titi(0)
    app.MainLoop()

if __name__ == "__main__":
    main()
