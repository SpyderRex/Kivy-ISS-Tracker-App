# Kivy-ISS-Tracker-App
Track the location of the International Space Station 

This Kivy app uses the "Where the ISS at?" REST
API (https://wheretheiss.at/w/developer) to get
the latitude, longitude, altitude, and address
code location for the ISS. A button sends the 
user to Google maps to pinpoint the exact
location of those coordinates in a graphic 
manner. I built the APK for this app using
Google Colab and installed a working version of
it on my phone. The buildozer.spec file is set
for 32 bit  only, but I can be easily changed
to include 64 bit architecture as well.
