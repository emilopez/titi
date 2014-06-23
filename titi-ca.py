import wx
from MasiveCalcsFrame import MasiveCalcsFrame

# titi launcher

class titi(wx.App):
    def OnInit(self):
        self.MassiveCalcs = MasiveCalcsFrame(None)
        self.MassiveCalcs.Show()

        return True

def main():
    app = titi(0)
    app.MainLoop()

if __name__ == "__main__":
    main()