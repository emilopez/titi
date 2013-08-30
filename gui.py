# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Dec 17 2009)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import matplotlib
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure

class PageOne(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is a PageOne object", (20,20))

class PageTwo(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is a PageTwo object", (40,40))

###########################################################################
## Class MainFrameBase
###########################################################################

class MainFrameBase ( wx.Frame ):
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"titi", pos = wx.DefaultPosition, size = wx.Size( 800,492 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		menubar = wx.MenuBar()
		file = wx.Menu()
		help = wx.Menu()
		
		quit = wx.MenuItem(file, 105, '&Quit\tCtrl+Q', 'Quit the Application')
		about = wx.MenuItem(help, 106, '&About titi\tCtrl+Q', 'Credits, licences, etc.')
		file.AppendItem(quit)
		help.AppendItem(about)
		menubar.Append(file, '&File')
                menubar.Append(help, '&Help')
		self.SetMenuBar(menubar)
		
		self.m_figure = Figure()
		self.m_canvas = FigureCanvas(self, -1, self.m_figure)

		bSizer3.Add( self.m_canvas, 1, wx.ALL|wx.EXPAND, 5 )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		cmaps = ['gist_earth','gist_gray','gist_heat','gist_ncar','gist_rainbow','gist_stern','gist_yarg','autumn','bone','cool','copper','flag','gray','hot','hsv',
		    'jet','pink','prism','spring','summer','winter','spectral']
		#self.btDraw = wx.Button( self.m_panel, wx.ID_ANY, u"Draw!", wx.DefaultPosition, wx.DefaultSize, 0 )
		#self.btShow = wx.Button( self.m_panel, wx.ID_ANY, u"Show", wx.DefaultPosition, wx.DefaultSize, 0 )
		#self.filename = wx.TextCtrl(self.m_panel, size=(140, -1))
		self.btnFile = wx.Button(self.m_panel, label="Choose a file")
		self.diver_img = wx.StaticText(self.m_panel, -1, "Driver: ", style=wx.ALIGN_CENTRE)
		self.size_img = wx.StaticText(self.m_panel, -1, "Size: ", style=wx.ALIGN_CENTRE)
		self.lat0_img = wx.StaticText(self.m_panel, -1, "Lat0: ", style=wx.ALIGN_CENTRE)
		self.lon0_img = wx.StaticText(self.m_panel, -1, "Lon0: ", style=wx.ALIGN_CENTRE)
		self.dlat_img = wx.StaticText(self.m_panel, -1, "Dlat: ", style=wx.ALIGN_CENTRE)
		self.dlon_img = wx.StaticText(self.m_panel, -1, "Dlon: ", style=wx.ALIGN_CENTRE)
		self.lat_txt = wx.TextCtrl(self.m_panel, size=(150, -1))
		self.lon_txt = wx.TextCtrl(self.m_panel, size=(150, -1))
		self.btnExtract = wx.Button(self.m_panel, label="Extract")
		self.extractedValue_txt = wx.StaticText(self.m_panel, -1, "Value: ", style=wx.ALIGN_CENTRE)
		self.cmap_cbox = wx.ComboBox(self.m_panel, 1, value='gist_earth', pos=(50, 170), size=(150, -1), choices=cmaps, style=wx.CB_READONLY)
		self.statusbar = self.CreateStatusBar()

		#bSizer4.Add( self.btDraw, 0, wx.ALL, 5 )
		#bSizer4.Add( self.btShow, 0, wx.ALL, 5 )
				
		bSizer4.Add( self.btnFile, 0, wx.ALL, 5 )
		bSizer4.Add( self.cmap_cbox, 0, wx.ALL, 5 )
		bSizer4.Add( self.diver_img, 0, wx.ALL, 5 )
		bSizer4.Add( self.size_img, 0, wx.ALL, 5 )
		bSizer4.Add( self.lat0_img, 0, wx.ALL, 5 )
		bSizer4.Add( self.lon0_img, 0, wx.ALL, 5 )
		bSizer4.Add( self.dlat_img, 0, wx.ALL, 5 )
		bSizer4.Add( self.dlon_img, 0, wx.ALL, 5 )
		bSizer4.Add( self.lat_txt, 0, wx.ALL, 5 )
		bSizer4.Add( self.lon_txt, 0, wx.ALL, 5 )	
		bSizer4.Add( self.btnExtract, 0, wx.ALL, 5 )
		bSizer4.Add( self.extractedValue_txt, 0, wx.ALL, 5 )
		
		bSizer3.Add( bSizer4, 0, wx.EXPAND, 5 )
		
		bSizer2.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		self.m_panel.SetSizer( bSizer2 )
		self.m_panel.Layout()
		bSizer2.Fit( self.m_panel )
		bSizer1.Add( self.m_panel, 1, wx.EXPAND |wx.ALL, 0 )
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		# Connect Events

		self.btnFile.Bind(wx.EVT_BUTTON, self.onOpenFile)
		self.btnExtract.Bind(wx.EVT_BUTTON, self.btnExtractClick)
	        self.btnFile.Bind(wx.EVT_ENTER_WINDOW, self.OnWidgetEnter)
	        # Bind the 'click' event for clicking on the Fig
                self.m_canvas.mpl_connect('button_press_event', self.onFigPick)
                #self.m_canvas.mpl_connect('figure_enter_event', self.onFigPick)
                self.cmap_cbox.Bind(wx.EVT_TEXT, self.onCmapChange)
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	#def btDrawClick( self, event ):
            #event.Skip()
	#def btShowlick( self, event ):
	    #event.Skip()
	def onOpenFile( self, event ):
	    event.Skip()
	def OnWidgetEnter( self, event ):
	    event.Skip()
        def btExtractlick( self, event ):
            event.Skip()
        def onFigPick( self, event ):
            event.Skip()
        def onCmapChange( self, event ):
            event.Skip()

