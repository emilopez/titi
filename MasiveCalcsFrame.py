"""Subclass of AboutFrame, which is generated by wxFormBuilder."""

import wx
import gui

# Implementing AboutFrame
class MasiveCalcsFrame( gui.MasiveCalcsFrame ):
    def __init__( self, parent ):
        gui.MasiveCalcsFrame.__init__( self, parent )
	
    def onTreeItemRClick( self, event ):
        '''
            Right click over a tree item add files or
            directorys to the listbox to be processed
        '''
        if self.mc_gDir.GetPath() not in self.mc_LBox_Files2Process.GetStrings():
            self.mc_LBox_Files2Process.InsertItems([self.mc_gDir.GetPath()],1)

    def onStartExtractionClick( self, event ):
        print self.mc_LBox_points.GetStrings()

    def onBtnAddPointClick( self, event ):
        # get lat/row and lon/col
        lat_row = self.mc_txt_lat.GetValue()
        lon_col = self.mc_txt_lon.GetValue()
        point = "[" + lat_row + "," + lon_col + "]"

        # concatenate the type of point: lat/lon or row/col
        choice = self.mc_rBox_points_type.GetStringSelection()
        if choice == "Row/Col":
            point += "  (R/C)"
        else:
            point += "  (L/L)"

        # insert into the points listbox
        self.mc_LBox_points.InsertItems([point],1)

    def onPointsTypeClick( self, event ):
        choice = self.mc_rBox_points_type.GetStringSelection()
        if choice == "Row/Col":
            self.mc_stxt_lat.SetLabel("Row")
            self.mc_stxt_lon.SetLabel("Column")
        else:
            self.mc_stxt_lat.SetLabel("Latitude")
            self.mc_stxt_lon.SetLabel("Longitude")