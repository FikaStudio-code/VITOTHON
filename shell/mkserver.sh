#!/bin/sh
dist="/jails"
ezjail-admin create -f server -r $1 $1 0.0.0.0
chmod 755 ${dist}/$1/var/db/pkg
/usr/sbin/jail -c vnet host.hostname=$1 name=$1 path=${dist}/$1 persist
mount -t devfs devfs ${dist}/$1/dev
mount_nullfs ${dist}/basejail ${dist}/$1/basejail
for pkg in `ls ${dist}/flavours/server/pkg`
do
  pkg -j $1 add /pkg/$pkg
  echo $pkg 'is added.'
done
echo $1 'is created.'
#
jail -r $1
umount ${dist}/$1/dev
umount ${dist}/$1/basejail
echo $1 ' unjailed.'