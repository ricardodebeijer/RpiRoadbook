To have the Raspberry Pi, with the 7 inch touchscreen rotated 90/270 degrees:

Update contents of:
`sudo nano /boot/config.txt`

Add the line, for 90 degrees:
`display_rotate=1`

Or add the line, for 270 degrees:
`display_rotate=3`


In your home directory (`/home/pi`), create a file:
`nano update-touchscreen.sh`
And add:
`#!/bin/bash`
`xinput --set-prop 'FT5406 memory based driver' 'Coordinate Transformation Matrix' 0 1 0 -1 0 1 0 0 1`

Chmod this file:
`sudo chmod 777 update-touchscreen.sh` 


Update contents of:
`sudo nano /etc/xdg/lxsession/LXDE-pi/autostart`
Add the following line add the end
`@/home/pi/update-touchscreen.sh`

Now reboot:
`sudo reboot`

If you need a virtual keyboard:


