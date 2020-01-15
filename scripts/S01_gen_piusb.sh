#!/bin/sh
# We recover the sectors already used and we calculate the size of the two partitions to create
DISK_SIZE=$(fdisk -l /dev/mmcblk0 | grep Disk | awk '{print $7-1}')
LAST_SECTOR=$(fdisk -l /dev/mmcblk0 | grep mmcblk0p2 | awk '{print $5+1}')
echo $DISK_SIZE
echo $LAST_SECTOR
let FREE_SIZE=$DISK_SIZE-$LAST_SECTOR-2
let HALF_SIZE=$FREE_SIZE/2
echo $FREE_SIZE
echo $HALF_SIZE

# we will create partitions with fdisk
sed -e 's/\s*\([\+0-9a-zA-Z]*\).*/\1/' << EOF | fdisk /dev/mmcblk0
  n # new partition
  p # primary partition
  3 # partition number 3, first new one
    # default - start at the beginning of unallocated free space
  +$HALF_SIZE # half the free space
  n # new partition again
  p # primary partition, no number as it is the last one
    # default - start at the end of previously created one
  +$HALF_SIZE # half the free space
  p # print the in-memory partition table
  w # save and quit
EOF

# we copy the rest of the treatment
mount / -o rw,remount
sleep .5
cp /home/rpi/scripts/S02_gen_btrfs.sh /etc/init.d/S02_gen_btrfs.sh
chmod +x /etc/init.d/S02_gen_btrfs.sh

# we delete the current script
rm /etc/init.d/S01_gen_piusb.sh

# we make sure to write the cache on the disc
sync
mount / -o ro,remount
# two securities are better than one
sleep 5
# we restart
reboot


