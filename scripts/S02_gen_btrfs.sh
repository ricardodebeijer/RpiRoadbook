#!/bin/sh

# insert here the display of the info image
# dd if=/root/update.fb of=/dev/fb0 bs=1536000 count=1 > /dev/null 2>&1
# we create the node udev for the btrfs
mknod /dev/btrfs-control c 10 234
# we create the btrfs filesystem on partition 3
mkfs.btrfs -f /dev/mmcblk0p3
# ditto on partition 4
mkfs.btrfs -f /dev/mmcblk0p4
# We mount the 1st partition
mount /dev/mmcblk0p3 /mnt/piusb
# We add the 2nd partition
btrfs device add -f /dev/mmcblk0p4 /mnt/piusb
# and we define the mirror raid
btrfs balance start -dconvert=raid1 -mconvert=raid1 /mnt/piusb

# now we can decompress the initial archive
mount / -o rw,remount
sleep .5
tar -C / -xvf "/home/rpi/scripts/init.tar.gz"
sleep .5

# we delete the current script
rm /etc/init.d/S02_gen_btrfs.sh
sync
mount / -o ro,remount

# and we restart for the last time
reboot

