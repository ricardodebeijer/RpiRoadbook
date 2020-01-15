# RpiRoadbook
Digital roadbook from a Raspberry Pi

## Starting idea

For motorcycle rallies of the French Road Rally Championship, or for my own rides, I currently use a "paper" dispenser. The electric version allows with a remote control, to advance or move back the boxes of the roadbook to follow its navigation.

A product exists to switch to the electronic unwinder (IzRoadbook, based on e-reader), but the price and the fact that for the moment it is intended only for CFRR rallies do not allow it to be used for its own walks or to reuse the reader to read her novels.

For my needs to create ride roadbooks, I therefore started to code a site to generate the boxes which go well (accessible [here] (http://tqhien.free.fr/)). Then comes the time to develop the "field" part of the roadbook: the unwinder. The criteria are as follows: components accessible to everyone, design different from what exists, and re-use for something other than the unwinder. This results in a screen of sufficient size (7 inches), tactile and visible even in direct sunlight (800cd / m2). Not too expensive (the Rasperry Pi is ideal for that) and can replace the unwinder and the trip I currently have on the handlebars.

## Embedded Linux approach

For a system on board a motorcycle, the problem is the power of the rpi and the security of the memory card. Let me explain. Normally, with the Raspbian distribution, the rpi works like a computer: it reads and writes to the disk (the sdcard) when starting up and must save things when it is shut down. In the event of a repeated power outage, it is common to result in corruption of the SD card and loss of data.

Switching to on-board vehicles meets different needs: quick start-up and security in the event of a power failure. This means in particular a read-only memory card: no corruption of the memory card in the event of untimely extinction. There is just a partition on the card that is in write mode, to save user data from time to time. Creating your own operating system takes a long time, because you have to select the necessary elements and reject the others, then compile from source code. Usually, these files are created on the architecture that will receive the system. For example on PC for PC, on a Mac for Mac, etc. If we do it on the Rpi, it's long. Very long. So it's about using the power of your computer to generate more quickly the code that the Rpi will understand. This is called Cross-compilation. This is the subject of the following chapter: Builroot.

## Setup
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
To come up...


## Python application / PDF reader / Trip
To come up...

## Remote control
To come up...