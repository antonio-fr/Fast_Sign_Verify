#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ClipBoard of FSV
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


import wx

def add_cb(text):
    clipdata = wx.TextDataObject()
    clipdata.SetText(text)
    wx.TheClipboard.Open()
    wx.TheClipboard.SetData(clipdata)
    wx.TheClipboard.Close()