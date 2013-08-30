"""Subclass of MainFrameBase, which is generated by wxFormBuilder."""

import wx
import gui
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.cm as cm
import rasterIO
import module as m

# Implementing MainFrameBase
class MainFrame( gui.MainFrameBase ):
    def __init__( self, parent ):
        gui.MainFrameBase.__init__( self, parent )

    def onOpenFile(self, event):
        wildcard = "All files (*.*)|*.*"
        """
        Create and show the Open FileDialog
        """
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultFile="",
            wildcard=wildcard,
            style=wx.OPEN | wx.CHANGE_DIR
            )
            #wx.MULTIPLE |
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPaths()[0]
            #self.filename.SetValue(path)
            self.statusbar.SetStatusText(path)
            self.ax = self.m_figure.add_subplot(111)
            #filename_img = self.filename.GetValue()
            self.filename_img = path
            file_pointer = rasterIO.opengdalraster(self.filename_img)
            driver, self.XSize, self.YSize, proj_wkt, geo = rasterIO.readrastermeta(file_pointer)
            print geo
            self.data = rasterIO.readrasterband(file_pointer, 1)
            self.data = self.data.astype(np.float32)
            eval("self.ax.imshow(self.data, cmap = cm."+self.cmap_cbox.GetValue()+")")
            self.lon0,self.lat0,self.dlon,self.dlat = geo[0],geo[3],geo[1],geo[5]
            self.statusbar.SetStatusText("Proj: " + proj_wkt)
            self.diver_img.SetLabel("Driver: " + driver)
            self.size_img.SetLabel("Size: " + str(self.YSize)+","+str(self.XSize))
            self.lat0_img.SetLabel("Lat0: " + str(self.lat0))
            self.lon0_img.SetLabel("Lon0: " + str(self.lon0))
            self.dlat_img.SetLabel("Dlat: " + str(self.dlat))
            self.dlon_img.SetLabel("Dlon: " + str(self.dlon))
            self.ax.set_xlabel('Col (Lon)')
            self.ax.set_ylabel('Row (Lat)')

            self.ax.grid(True)
            self.m_canvas.draw()
        dlg.Destroy()

    def OnWidgetEnter(self, event):
        name = event.GetEventObject().GetLabel()
        if name == "Choose a file":
            self.statusbar.SetStatusText("Choose a image file")
        elif name == "Show":
            self.statusbar.SetStatusText("Show selected image")
        else:
            self.statusbar.SetStatusText(event.GetEventObject().GetName())
        event.Skip()
    def btnExtractClick(self, event):
        row,col = m.getRowCol(float(self.lat_txt.GetValue()),float(self.lon_txt.GetValue()),self.lat0, self.lon0, self.dlat, self.dlon)
        self.extractedValue_txt.SetLabel("Value: "+str(self.data[row][col]))

    def onFigPick( self, event ):
        # The event received here is of the type
        # matplotlib.backend_bases.PickEvent

        if (0<=event.xdata<=self.XSize) and (0<=event.ydata<=self.YSize):
            col,row = int(event.xdata), int(event.ydata)
            val = self.data[row][col]
            lat,lon = m.getLatLon(row,col,self.lat0,self.lon0,self.dlat,self.dlon)
            self.statusbar.SetStatusText("Value at img["+str(row)+","+str(col)+"] = "+str(val)+" | Georeferended to Lat, Lon = "+str(lat)+", "+str(lon))

    def onCmapChange( self, event ):
        # Redraw the image using the colormap selected
        eval("self.ax.imshow(self.data, cmap = cm."+self.cmap_cbox.GetValue()+")")
        self.m_canvas.draw()