#!/usr/bin/python
# -*- coding: latin-1 -*-
import cgi, os
import cgitb; cgitb.enable()
import shutil

print ("""Content-Type: text/html\n
<html>
<head>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="w3.css">
	<link rel="stylesheet" href="font-awesome.min.css">
	<link rel="stylesheet" href="material-icons.css">
    <link rel="stylesheet" type="text/css" href="mystyle.css">
</head>
<body>
<!-- Entete -->
<div class="w3-container w3-center w3-section">
<h1>Retour &agrave la configuration d'usine</h1>
</div>
<hr>
<div class="w3-container w3-section w3-topbar w3-bottombar w3-border-grey w3-margin">
<h3>Fichiers supprim&eacute;s :</h3>
""")

filelist = [
    '.conf/RpiRoadbook.cfg',
    '.conf/RpiRoadbook_setup.cfg',
    '.conf/RpiRoadbook_screen.cfg',
    '.conf/route.cfg',
    '.conf/screen.cfg',
    '.log/chrono.cfg',
    '.log/odo.cfg',
]

for fileitem in filelist:
    try:
        os.remove("/mnt/piusb/{}".format(fileitem))
    except :
        pass
    else:
        print('{}<br>'.format(fileitem))
print ("""
</div>
<hr>

<!-- Pied de page -->
<div class="w3-bar w3-black">
  <a class="w3-bar-item w3-button w3-hover-blue" href="index.py"><i class="w3-xlarge fa fa-home"></i></a>
  <a href="setup.py" class="w3-bar-item w3-button w3-hover-blue">Configurer</a>
  <a href="screen_setup.py" class="w3-bar-item w3-button w3-hover-blue">Personnaliser les affichages</a>
  <a href="clock_setup.py" class="w3-bar-item w3-button w3-hover-blue">Ajuster l'horloge</a>
  <a href="ota.py" class="w3-bar-item w3-button w3-right w3-hover-red">MAJ Firmware</a>
</div>
</body>
</html>""")
