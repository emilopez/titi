# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct  8 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import matplotlib
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure

###########################################################################
## Class MainFrameBase
###########################################################################

class MainFrameBase ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"titi", pos = wx.DefaultPosition, size = wx.Size( 882,683 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_figure = Figure()
		self.m_canvas = FigureCanvas(self, -1, self.m_figure)
		#
		# ---== Bind MATPLOTLIB EVENTS ==---
		self.m_canvas.mpl_connect('button_press_event', self.onFigureClicked)
		self.m_canvas.mpl_connect('axes_enter_event', self.onEnterAxes)
		self.m_canvas.mpl_connect('axes_leave_event', self.onLeaveAxes)
		self.m_canvas.mpl_connect('motion_notify_event', self.onMouseMotion)
		self.m_canvas.mpl_connect('scroll_event',self.onZoom)
		
		# ---== Add this to the end==---
		#def onFigureClicked( self, event ):
		#    event.Skip()
		#def onEnterAxes( self, event ):
		#    event.Skip()
		#def onLeaveAxes( self, event ):
		#    event.Skip()
		#def onMouseMotion( self, event ):
		#    event.Skip()
		#def onZoom( self, event ):
		#    event.Skip()
		
		
		bSizer4.Add( self.m_canvas, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer3.Add( bSizer4, 1, wx.EXPAND|wx.ALIGN_BOTTOM, 5 )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_btn_file = wx.FilePickerCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer5.Add( self.m_btn_file, 0, wx.ALL|wx.EXPAND, 5 )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_stxt_colormap = wx.StaticText( self.m_panel, wx.ID_ANY, u"Colormap", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_stxt_colormap.Wrap( -1 )
		gSizer1.Add( self.m_stxt_colormap, 0, wx.ALL, 5 )
		
		m_cmb_colormapChoices = [ u"gist_earth", u"gist_gray", u"gist_heat", u"gist_ncar", u"gist_rainbow", u"gist_stern", u"gist_yarg", u"autumn", u"bone", u"cool", u"copper", u"flag", u"gray", u"hot", u"hsv", u"jet", u"pink", u"prism", u"spring", u"summer", u"winter", u"spectral" ]
		self.m_cmb_colormap = wx.ComboBox( self.m_panel, wx.ID_ANY, u"gist_earth", wx.DefaultPosition, wx.Size( 100,-1 ), m_cmb_colormapChoices, 0 )
		gSizer1.Add( self.m_cmb_colormap, 0, wx.ALL, 5 )
		
		self.m_stxt_band = wx.StaticText( self.m_panel, wx.ID_ANY, u"Band", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_stxt_band.Wrap( -1 )
		gSizer1.Add( self.m_stxt_band, 0, wx.ALL, 5 )
		
		m_cmb_bandChoices = []
		self.m_cmb_band = wx.ComboBox( self.m_panel, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 100,-1 ), m_cmb_bandChoices, 0 )
		gSizer1.Add( self.m_cmb_band, 0, wx.ALL, 5 )
		
		
		bSizer5.Add( gSizer1, 0, wx.EXPAND, 5 )
		
		self.m_staticline2 = wx.StaticLine( self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer5.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		m_rBox_extract_input_typeChoices = [ u"Lat/Lon", u"Row/Col" ]
		self.m_rBox_extract_input_type = wx.RadioBox( self.m_panel, wx.ID_ANY, u"Input Type", wx.DefaultPosition, wx.DefaultSize, m_rBox_extract_input_typeChoices, 2, wx.RA_SPECIFY_COLS )
		self.m_rBox_extract_input_type.SetSelection( 0 )
		bSizer5.Add( self.m_rBox_extract_input_type, 0, wx.ALL|wx.EXPAND, 5 )
		
		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_stxt_lat = wx.StaticText( self.m_panel, wx.ID_ANY, u"Latitude", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_stxt_lat.Wrap( -1 )
		gSizer2.Add( self.m_stxt_lat, 0, wx.ALL, 5 )
		
		self.m_txt_lat = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_txt_lat, 0, wx.ALL, 5 )
		
		self.m_stxt_lon = wx.StaticText( self.m_panel, wx.ID_ANY, u"Longitude", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_stxt_lon.Wrap( -1 )
		gSizer2.Add( self.m_stxt_lon, 0, wx.ALL, 5 )
		
		self.m_txt_lon = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_txt_lon, 0, wx.ALL, 5 )
		
		self.m_btn_extract = wx.Button( self.m_panel, wx.ID_ANY, u"Extract", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		gSizer2.Add( self.m_btn_extract, 0, wx.ALL, 5 )
		
		self.m_txt_extracted_value = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_txt_extracted_value, 0, wx.ALL, 5 )
		
		
		bSizer5.Add( gSizer2, 0, wx.EXPAND, 5 )
		
		self.m_staticline3 = wx.StaticLine( self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer5.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		gSizer3 = wx.GridSizer( 0, 1, 0, 0 )
		
		
		bSizer5.Add( gSizer3, 0, wx.EXPAND, 5 )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer6.SetMinSize( wx.Size( 100,100 ) )
		self.m_figure_preview = Figure()
		self.m_canvas_preview = FigureCanvas(self, -1, self.m_figure_preview)
		bSizer6.Add( self.m_canvas_preview, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )
		
		
		bSizer5.Add( bSizer6, 0, wx.ALIGN_CENTER|wx.FIXED_MINSIZE, 0 )
		
		
		bSizer3.Add( bSizer5, 0, wx.EXPAND|wx.FIXED_MINSIZE, 5 )
		
		
		bSizer2.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		
		self.m_panel.SetSizer( bSizer2 )
		self.m_panel.Layout()
		bSizer2.Fit( self.m_panel )
		bSizer1.Add( self.m_panel, 1, wx.EXPAND, 5 )
		
		self.m_txt_log = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,60 ), wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer1.Add( self.m_txt_log, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu_file = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.AppendItem( self.m_menuItem1 )
		
		self.m_menubar1.Append( self.m_menu_file, u"File" )
		
		self.m_menu_options = wx.Menu()
		self.m_mitem_massive_calcs = wx.MenuItem( self.m_menu_options, wx.ID_ANY, u"Massive Calcs", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_options.AppendItem( self.m_mitem_massive_calcs )
		
		self.m_menubar1.Append( self.m_menu_options, u"Options" )
		
		self.m_menu_help = wx.Menu()
		self.m_mitem_about = wx.MenuItem( self.m_menu_help, wx.ID_ANY, u"About titi...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_help.AppendItem( self.m_mitem_about )
		
		self.m_menubar1.Append( self.m_menu_help, u"Help" )
		
		self.SetMenuBar( self.m_menubar1 )
		
		self.m_statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		# Connect Events
		self.Bind( wx.EVT_ACTIVATE, self.onActivateApp )
		self.m_btn_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.onOpenFile )
		self.m_cmb_colormap.Bind( wx.EVT_TEXT, self.onCmapChanged )
		self.m_cmb_band.Bind( wx.EVT_TEXT, self.onBandChanged )
		self.m_rBox_extract_input_type.Bind( wx.EVT_RADIOBOX, self.onExtractInputTypeClick )
		self.m_btn_extract.Bind( wx.EVT_BUTTON, self.onExtractClicked )
		self.Bind( wx.EVT_MENU, self.onMassiveCalcsSelected, id = self.m_mitem_massive_calcs.GetId() )
		self.Bind( wx.EVT_MENU, self.onAboutSelected, id = self.m_mitem_about.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onActivateApp( self, event ):
		event.Skip()
	
	def onOpenFile( self, event ):
		event.Skip()
	
	def onCmapChanged( self, event ):
		event.Skip()
	
	def onBandChanged( self, event ):
		event.Skip()
	
	def onExtractInputTypeClick( self, event ):
		event.Skip()
	
	def onExtractClicked( self, event ):
		event.Skip()
	
	def onMassiveCalcsSelected( self, event ):
		event.Skip()
	
	def onAboutSelected( self, event ):
		event.Skip()
	def onFigureClicked( self, event ):
		event.Skip()
	def onEnterAxes( self, event ):
		event.Skip()
	def onLeaveAxes( self, event ):
		event.Skip()
	def onMouseMotion( self, event ):
		event.Skip()
	def onZoom( self, event ):
		event.Skip()
	

###########################################################################
## Class MasiveCalcsFrame
###########################################################################

class MasiveCalcsFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Massive calcs", pos = wx.DefaultPosition, size = wx.Size( 868,435 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel2 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.mc_gDir = wx.GenericDirCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,100 ), wx.DIRCTRL_3D_INTERNAL|wx.SUNKEN_BORDER, wx.EmptyString, 0 )
		
		self.mc_gDir.ShowHidden( False )
		bSizer13.Add( self.mc_gDir, 0, wx.ALL|wx.EXPAND, 5 )
		
		mc_LBox_Files2ProcessChoices = [ u"Files or dirs to be process" ]
		self.mc_LBox_Files2Process = wx.ListBox( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.Size( 250,220 ), mc_LBox_Files2ProcessChoices, 0 )
		bSizer13.Add( self.mc_LBox_Files2Process, 0, wx.ALL, 5 )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		mc_rBox_points_typeChoices = [ u"Lat/Lon", u"Row/Col" ]
		self.mc_rBox_points_type = wx.RadioBox( self.m_panel2, wx.ID_ANY, u"Points type", wx.DefaultPosition, wx.DefaultSize, mc_rBox_points_typeChoices, 1, 0 )
		self.mc_rBox_points_type.SetSelection( 0 )
		bSizer14.Add( self.mc_rBox_points_type, 0, wx.ALL|wx.EXPAND, 5 )
		
		gSizer5 = wx.GridSizer( 2, 2, 0, 0 )
		
		self.mc_stxt_lat = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Latitude", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mc_stxt_lat.Wrap( -1 )
		gSizer5.Add( self.mc_stxt_lat, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.mc_txt_lat = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		gSizer5.Add( self.mc_txt_lat, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.mc_stxt_lon = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Longitude", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mc_stxt_lon.Wrap( -1 )
		gSizer5.Add( self.mc_stxt_lon, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.mc_txt_lon = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 35,-1 ), 0 )
		gSizer5.Add( self.mc_txt_lon, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.mc_btn_add_point = wx.Button( self.m_panel2, wx.ID_ANY, u"Add Point", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		gSizer5.Add( self.mc_btn_add_point, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.mc_btn_file_points = wx.FilePickerCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		gSizer5.Add( self.mc_btn_file_points, 0, wx.ALL, 5 )
		
		
		bSizer14.Add( gSizer5, 0, wx.EXPAND, 5 )
		
		self.m_staticline3 = wx.StaticLine( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer14.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		gSizer51 = wx.GridSizer( 2, 2, 0, 0 )
		
		self.m_staticText23 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Band", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		gSizer51.Add( self.m_staticText23, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.mc_txt_band = wx.TextCtrl( self.m_panel2, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		gSizer51.Add( self.mc_txt_band, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer14.Add( gSizer51, 1, wx.EXPAND, 5 )
		
		
		bSizer13.Add( bSizer14, 0, wx.ALIGN_TOP, 5 )
		
		mc_LBox_pointsChoices = [ u"Points to extract" ]
		self.mc_LBox_points = wx.ListBox( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,-1 ), mc_LBox_pointsChoices, 0 )
		bSizer13.Add( self.mc_LBox_points, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer12.Add( bSizer13, 0, wx.EXPAND, 5 )
		
		bSizer17 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText13 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Filename Output", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		bSizer16.Add( self.m_staticText13, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.mc_txt_filename_out = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 450,-1 ), 0 )
		bSizer16.Add( self.mc_txt_filename_out, 0, wx.ALL, 5 )
		
		self.mc_btn_start_extraction = wx.Button( self.m_panel2, wx.ID_ANY, u"Start extraction", wx.DefaultPosition, wx.Size( 240,-1 ), wx.BU_EXACTFIT )
		bSizer16.Add( self.mc_btn_start_extraction, 0, wx.ALL, 5 )
		
		
		bSizer17.Add( bSizer16, 0, wx.EXPAND, 5 )
		
		self.mc_txt_log = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer17.Add( self.mc_txt_log, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer12.Add( bSizer17, 1, wx.EXPAND, 5 )
		
		
		self.m_panel2.SetSizer( bSizer12 )
		self.m_panel2.Layout()
		bSizer12.Fit( self.m_panel2 )
		self.m_notebook1.AddPage( self.m_panel2, u"Extraction", True )
		self.m_panel7 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_notebook1.AddPage( self.m_panel7, u"Band Calcs", False )
		
		bSizer7.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer7 )
		self.Layout()
		self.m_statusBar2 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.mc_gDir.Bind( wx.EVT_TREE_ITEM_RIGHT_CLICK, self.onTreeItemRClick )
		self.mc_rBox_points_type.Bind( wx.EVT_RADIOBOX, self.onPointsTypeClick )
		self.mc_btn_add_point.Bind( wx.EVT_BUTTON, self.onBtnAddPointClick )
		self.mc_btn_file_points.Bind( wx.EVT_FILEPICKER_CHANGED, self.onOpenPointsFile )
		self.mc_btn_start_extraction.Bind( wx.EVT_BUTTON, self.onStartExtractionClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onTreeItemRClick( self, event ):
		event.Skip()
	
	def onPointsTypeClick( self, event ):
		event.Skip()
	
	def onBtnAddPointClick( self, event ):
		event.Skip()
	
	def onOpenPointsFile( self, event ):
		event.Skip()
	
	def onStartExtractionClick( self, event ):
		event.Skip()
	

