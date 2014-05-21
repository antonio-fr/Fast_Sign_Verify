#!/usr/bin/env python
# coding=utf8

# Main of FSV : Fast Sign Verify
# Copyright (C) 2014  Antoine FERRON

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>


import sys
import wx
import MainFrame
from ECDSA_BTC import *
import base64
import clipboard

class MyownApp(wx.App):
    def OnInit(self):
        return True

class MyownFrame ( MainFrame.MyFrame1 ):
    def sign_click( self, event ):
        event.Skip()
        is_deterministic=self.check_determin.GetValue()
        try:
            if is_deterministic: raise Exception("Determinstic signing not yet supported!")
            secret = int(priv_base58_hex(self.address.GetValue()),16)
            pubkey = Public_key( generator_256, secret*generator_256 )
            privkey = Private_key( pubkey, secret )
            self.address_pub = pub_hex_base58( pubkey.point.x(), pubkey.point.y() )
            signature = bitcoin_sign_message( privkey, self.text_signed.GetValue(), randoml(generator_256) )
            signature_str = bitcoin_encode_sig( signature )
            signature64 = base64.b64encode( signature_str )
            self.signature.SetValue(signature64)
        except Exception as inst:
            self.signature.SetValue("Error :\n"+str(inst))
    
    def verify_click( self, event ):
        event.Skip()
        try:
            address=self.address.GetValue()
            signature=self.signature.GetValue()
            message=self.text_signed.GetValue()
            bitcoin_verify_message(address, signature, message)
            aff_msg( "OK, Genuine!" )
        except Exception as inst:
            aff_msg( "FALSE or Error\n"+str(inst))
    
    def copy_sig( self, event ):
        event.Skip()
        clipboard.add_cb(self.signature.GetValue())
    
    def copyall( self, event ):
        event.Skip()
        address=self.address_pub
        signature=self.signature.GetValue()
        message=self.text_signed.GetValue()
        clipboard.add_cb(output_full_sig(message,address,signature))

class MessageDialog( MainFrame.MyDialog1 ):
    None

def aff_msg(message):
    msgdial=MessageDialog(None)
    msgdial.mess_text.SetLabel(message)
    msgdial.Show(True)

if __name__ == '__main__' :
    app = MyownApp(True)
    frame1 = MyownFrame(None)
    frame1.Show(True)
    app.SetTopWindow(frame1)
    app.MainLoop()
    sys.exit()
