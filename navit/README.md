Adding navit navigation software to raspberry pi 3.

Follow this guide:
https://wiki.navit-project.org/index.php/Raspberry_Pi


Overwrite the default xml, with the xml specified in this folder (`navit.xml`)

Go to your Pi's desktop:
`cd ~/Desktop`

And create a desktop icon:
`nano navit.desktop`

Add the following:
`
[Desktop Entry]
Version=1.0
Name=Navit
Comment=Opens Navit
Exec=/home/pi/navit-build/navit/navit
Terminal=false
Type=Application
Categories=Utility;Application;
Icon=/home/pi/Pictures/navit128.png
`


