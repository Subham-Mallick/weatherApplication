# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import requests

###########################################################################
## Class mainDialogBox
###########################################################################

class mainDialogBox ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Weather", pos = wx.DefaultPosition, size = wx.Size( 343,344 ), style = wx.DEFAULT_DIALOG_STYLE )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        mainBoxSizer = wx.BoxSizer( wx.VERTICAL )
        
        self.mainNotebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.panelWeather = wx.Panel( self.mainNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer3 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText1 = wx.StaticText( self.panelWeather, wx.ID_ANY, u"Enter City or Country Name", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        bSizer3.Add( self.m_staticText1, 0, wx.ALL, 5 )
        
        
        bSizer2.Add( bSizer3, 0, wx.EXPAND, 5 )
        
        gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
        
        self.textCtrl_CityOrCountryName = wx.TextCtrl( self.panelWeather, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.textCtrl_CityOrCountryName, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
        
        self.buttonGo = wx.Button( self.panelWeather, wx.ID_ANY, u"Go!", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.buttonGo, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer2.Add( gSizer1, 0, wx.EXPAND, 5 )
        
        gSizer2 = wx.GridSizer( 0, 2, 0, 0 )
        
        self.staticText_Temperature = wx.StaticText( self.panelWeather, wx.ID_ANY, u"Temperature", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticText_Temperature.Wrap( -1 )
        gSizer2.Add( self.staticText_Temperature, 0, wx.ALL, 5 )
        
        self.staticTextTemperature_value = wx.StaticText( self.panelWeather, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticTextTemperature_value.Wrap( -1 )
        gSizer2.Add( self.staticTextTemperature_value, 0, wx.ALL, 5 )
        
        self.staticTextHumidity = wx.StaticText( self.panelWeather, wx.ID_ANY, u"Humidity", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticTextHumidity.Wrap( -1 )
        gSizer2.Add( self.staticTextHumidity, 0, wx.ALL, 5 )
        
        self.staticTextHumidity_value = wx.StaticText( self.panelWeather, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticTextHumidity_value.Wrap( -1 )
        gSizer2.Add( self.staticTextHumidity_value, 0, wx.ALL, 5 )
        
        self.staticTextForcast = wx.StaticText( self.panelWeather, wx.ID_ANY, u"Forcast", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticTextForcast.Wrap( -1 )
        gSizer2.Add( self.staticTextForcast, 0, wx.ALL, 5 )
        
        self.staticTextForcast_value = wx.StaticText( self.panelWeather, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticTextForcast_value.Wrap( -1 )
        gSizer2.Add( self.staticTextForcast_value, 0, wx.ALL, 5 )
        
        self.staticTextCloudiness = wx.StaticText( self.panelWeather, wx.ID_ANY, u"Cloudiness", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticTextCloudiness.Wrap( -1 )
        gSizer2.Add( self.staticTextCloudiness, 0, wx.ALL, 5 )
        
        self.staticTextCloudiness_value = wx.StaticText( self.panelWeather, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticTextCloudiness_value.Wrap( -1 )
        gSizer2.Add( self.staticTextCloudiness_value, 0, wx.ALL, 5 )
        
        
        bSizer2.Add( gSizer2, 0, wx.EXPAND, 5 )
        
        
        self.panelWeather.SetSizer( bSizer2 )
        self.panelWeather.Layout()
        bSizer2.Fit( self.panelWeather )
        self.mainNotebook.AddPage( self.panelWeather, u"Weather", True )
        
        mainBoxSizer.Add( self.mainNotebook, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( mainBoxSizer )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.buttonGo.Bind( wx.EVT_BUTTON, self.buttonGoOnButtonClick )
    
    def __del__( self ):
        pass
    
    def getDataFromAPI(self,name):
        #name = self.textCtrl_CityOrCountryName.value
        api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
        url = api_address + name
        json_data = requests.get(url).json()
        try:
            int(json_data['main']['temp']) - 273.15
            #print(format_add)
        except :
            return str(json_data['message'])
        
        
        temperature = str(int(json_data['main']['temp'] - 273.15))+ " Degree Celcius"
        
        humidity = str(int(json_data['main']['humidity']))+ "%"
        
        forcast = str(json_data['weather'][0]['main'])+","+str(json_data['weather'][0]['description'])
        
        cloudiness = str(int(json_data['clouds']['all']))+ "%"
        
        return [temperature,humidity,forcast,cloudiness]
        
        
        
        
        
    # Virtual event handlers, overide them in your derived class
    def buttonGoOnButtonClick( self, event ):
        name = self.textCtrl_CityOrCountryName.GetValue()
        listOfData = self.getDataFromAPI(name)
        if type(listOfData) is list:
            self.staticTextTemperature_value.SetLabel(listOfData[0])
            self.staticTextHumidity_value.SetLabel(listOfData[1])
            self.staticTextForcast_value.SetLabel(listOfData[2])
            self.staticTextCloudiness_value.SetLabel(listOfData[3])
#        gSizer2.Layout()
            
            
class MainApp(wx.App):
	def OnInit(self):
		mainFrame1 = mainDialogBox(None)
		mainFrame1.Show(True)
		return True

if __name__ == "__main__":
	app = MainApp()
	app.MainLoop()
            
            
            
            
            
            
            
            