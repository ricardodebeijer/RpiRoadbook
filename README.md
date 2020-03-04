# RpiRoadbook
Digital roadbook from a Raspberry Pi

## Starting idea

For motorcycle rallies of the French Road Rally Championship, or for my own rides, I currently use a "paper" dispenser. The electric version allows with a remote control, to advance or move back the boxes of the roadbook to follow its navigation.

A product exists to switch to the electronic unwinder (IzRoadbook, based on e-reader), but the price and the fact that for the moment it is intended only for CFRR rallies do not allow it to be used for its own walks or to reuse the reader to read her novels.

For my needs to create ride roadbooks, I therefore started to code a site to generate the boxes which go well (accessible [here] (http://tqhien.free.fr/)). Then comes the time to develop the "field" part of the roadbook: the unwinder. The criteria are as follows: components accessible to everyone, design different from what exists, and re-use for something other than the unwinder. This results in a screen of sufficient size (7 inches), tactile and visible even in direct sunlight (800cd / m2). Not too expensive (the Rasperry Pi is ideal for that) and can replace the unwinder and the trip I currently have on the handlebars.

## Embedded Linux approach

For a system on board a motorcycle, the problem is the power of the rpi and the security of the memory card. Let me explain. Normally, with the Raspbian distribution, the rpi works like a computer: it reads and writes to the disk (the sdcard) when starting up and must save things when it is shut down. In the event of a repeated power outage, it is common to result in corruption of the SD card and loss of data.

Switching to on-board vehicles meets different needs: quick start-up and security in the event of a power failure. This means in particular a read-only memory card: no corruption of the memory card in the event of untimely extinction. There is just a partition on the card that is in write mode, to save user data from time to time. Creating your own operating system takes a long time, because you have to select the necessary elements and reject the others, then compile from source code. Usually, these files are created on the architecture that will receive the system. For example on PC for PC, on a Mac for Mac, etc. If we do it on the Rpi, it's long. Very long. So it's about using the power of your computer to generate more quickly the code that the Rpi will understand. This is called Cross-compilation. This is the subject of the following chapter: Builroot.

### Tried for Windows, did not work
- Download a version of [Make](https://sourceforge.net/projects/gnuwin32/files/make/3.81/make-3.81.exe/download?use_mirror=netix&download=)
- Add `make` to `PATH`
- Download a version of [BuildRoot](https://buildroot.org/download.html)
- Extract BuildRoot using `tar xvjf buildroot-XXXX`
- Download a version of [Python 3](https://www.python.org/downloads/)
- Add `python` to `PATH`
- Have `Microsoft Visual C++ Build Tools` installed from [Visual Studio](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2017), see [this](https://github.com/benfred/implicit/issues/76#issuecomment-404889398) for help
- Change directory into the `RpiRoadbook` src folder
- run `pip install -r requirements.txt`


## Buildroot and Raspberry Pi
_Use a Linux system, because `make` in combination with Buildroot does not work on Windows as far as I tested_

- `cd` to the /buildroot folder this project
- Using the following guide: https://www.blaess.fr/christophe/articles/creer-un-systeme-complet-avec-buildroot/, do these steps:
- Download Buildroot `wget http://www.buildroot.org/downloads/buildroot-2019.02.tar.bz2`
- Extract with: `tar xf buildroot-2019.02.tar.bz2`
- Go into folder: `cd buildroot-2019.02`
- Create `.config` for Raspberry Pi 3 with: `make raspberrypi3_defconfig`
- Overwrite the `.config` created, with the config provided in `/board/rpi-3/buildroot-2019.02-toolchain.config`
- Create toolchain for the first time: `make toolchain`. _Note: this takes a while (+- 1 hour)_
- When setting up the toolchain is done, we can start on the actual system.
- First remove the buildroot folder with: `rm -rf buildroot-2019.02`
- Extract again with: `tar xf buildroot-2019.02.tar.bz2`
- Create `.config` again with: `make raspberrypi3_defconfig`
- This time overwrite the `.config` created, with the config provided in `/board/rpi-3/buildroot-2019.02-system-01.config`
- No run `make` inside of the `buildroot` folder, again this take a while, but this time only a few minutes.
- List all your current disks with `lsblk`, now plug your SD card in and run `lsblk` again, notice which disk is added (in my case `sdb`)
- Unmount all partitions of that disk with `umount /dev/sdb?`
- Finally install the generated image on the SD card with: `sudo cp output/images/sdcard.img /dev/sdb`
- Plug the SD card in your Pi and hook up a monitor + keyboard
- Modify `.config` to your liking with `make xconfig` (changing MOTD, adding SSH, changing root password etc)
- Run `make` again
- Insert SD card and unmount partitions again with `umount /dev/sdb?`
- Copy new image to SD card again `sudo cp output/images/sdcard.img /dev/sdb`


## Python application / PDF reader / Trip
To come up...

## Remote control
To come up...