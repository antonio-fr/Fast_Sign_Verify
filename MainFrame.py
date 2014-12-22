# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"FastSignVerify  v0.40", pos = wx.DefaultPosition, size = wx.Size( 504,571 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 245, 247, 248 ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.text_signed = wx.TextCtrl( self, wx.ID_ANY, u"Text signed", wx.DefaultPosition, wx.Size( -1,180 ), wx.TE_CHARWRAP|wx.TE_MULTILINE|wx.TE_WORDWRAP )
		self.text_signed.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer1.Add( self.text_signed, 0, wx.ALL|wx.EXPAND, 5 )
		
		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"  Address", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		self.m_staticText2.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		self.m_staticText2.SetMinSize( wx.Size( 60,-1 ) )
		
		fgSizer2.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.address = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 400,-1 ), 0 )
		self.address.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer2.Add( self.address, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer1.Add( fgSizer2, 0, 0, 5 )
		
		
		bSizer1.AddSpacer( ( 0, 20), 0, 0, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Signature :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		self.m_staticText3.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.signature = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,100 ), wx.TE_CHARWRAP|wx.TE_MULTILINE|wx.TE_WORDWRAP )
		self.signature.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		gSizer2.Add( self.signature, 0, wx.ALL, 5 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"COPY", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button1.SetMinSize( wx.Size( 50,50 ) )
		
		gSizer2.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		
		bSizer1.Add( gSizer2, 0, wx.EXPAND, 5 )
		
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )
		
		gSizer3.SetMinSize( wx.Size( -1,75 ) ) 
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"SIGN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button2.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.m_button2.SetMinSize( wx.Size( -1,35 ) )
		
		gSizer3.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_button3 = wx.Button( self, wx.ID_ANY, u"VERIFY", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button3.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.m_button3.SetMinSize( wx.Size( -1,35 ) )
		
		gSizer3.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.check_determin = wx.CheckBox( self, wx.ID_ANY, u"Deterministic", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.check_determin.SetValue(True) 
		gSizer3.Add( self.check_determin, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer1.Add( gSizer3, 0, wx.EXPAND, 5 )
		
		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Copy ALL", wx.DefaultPosition, wx.Size( 120,45 ), 0 )
		self.m_button4.SetFont( wx.Font( 14, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer1.Add( self.m_button4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.copy_sig )
		self.m_button2.Bind( wx.EVT_BUTTON, self.sign_click )
		self.m_button3.Bind( wx.EVT_BUTTON, self.verify_click )
		self.m_button4.Bind( wx.EVT_BUTTON, self.copyall )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def copy_sig( self, event ):
		event.Skip()
	
	def sign_click( self, event ):
		event.Skip()
	
	def verify_click( self, event ):
		event.Skip()
	
	def copyall( self, event ):
		event.Skip()
	

###########################################################################
## Class MyDialog1
###########################################################################

class MyDialog1 ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Checking Status", pos = wx.DefaultPosition, size = wx.Size( 440,160 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.mess_text = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.mess_text.Wrap( -1 )
		self.mess_text.SetFont( wx.Font( 14, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer2.Add( self.mess_text, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

