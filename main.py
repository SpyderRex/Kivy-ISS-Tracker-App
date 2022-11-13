from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
import requests
import webbrowser


class WrappedLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(
            width=lambda *x:
            self.setter('text_size')(self, (self.width, None)),
            texture_size=lambda *x: self.setter('height')(self, self.texture_size[1]))

class MyFloatLayout(FloatLayout):
    def on_pre_enter(self):
        
        url = "https://api.wheretheiss.at/v1/satellites/25544"
        response = requests.get(url)
        Latitude = str(response.json()["latitude"])
        Longitude = str(response.json()["longitude"])
        Altitude= str(response.json()["altitude"])
        self.ids.lat_label.text = str(Latitude)
        self.ids.long_label.text = str(Longitude)
        self.ids.alt_label.text = str(Altitude) + " " + "km"#

        url2 = "https://trueway-geocoding.p.rapidapi.com/ReverseGeocode"
        querystring = {"location":Latitude+","+Longitude,"language":"en"}
        headers = {
	        "X-RapidAPI-Key": "cae07dc70emshf9ff2805075f54ep13f5e7jsn13ad36e92b18",
        	"X-RapidAPI-Host": "trueway-geocoding.p.rapidapi.com"
        }
        response2 = requests.request("GET", url2, headers=headers, params=querystring)
        address = response2.json()["results"][0]["address"]
        self.ids.address_label.text = str(address)      

               
    def get_location(self):
        url = "https://api.wheretheiss.at/v1/satellites/25544"
        response = requests.get(url)
        Latitude = str(response.json()["latitude"])
        Longitude = str(response.json()["longitude"])
        url2 = "https://trueway-geocoding.p.rapidapi.com/ReverseGeocode"
        querystring = {"location":Latitude+","+Longitude,"language":"en"}
        headers = {
	        "X-RapidAPI-Key": "cae07dc70emshf9ff2805075f54ep13f5e7jsn13ad36e92b18",
        	"X-RapidAPI-Host": "trueway-geocoding.p.rapidapi.com"
        }
        response2 = requests.request("GET", url2, headers=headers, params=querystring)
        address = response2.json()["results"][0]["address"]        
        webbrowser.open(f"https://plus.codes/{address}")
            

class ISSApp(App):
    def build(self):
        return MyFloatLayout()

if __name__ == "__main__":
    ISSApp().run()