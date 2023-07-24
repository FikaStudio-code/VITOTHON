#!/bin/sh
# e.g. bash mkrouter.sh router01 ripd
# $1: jail name
# $2: operation daemon (ripd / ospfd / bgpd)
dist="/jails"
ezjail-admin create -f router -r $1 $1 0.0.0.0
chmod 755 ${dist}/$1/var/db/pkg
/usr/sbin/jail -c vnet host.hostname=$1 name=$1 path=${dist}/$1 persist
mount -t devfs devfs ${dist}/$1/dev
mount_nullfs ${dist}/basejail ${dist}/$1/basejail
for pkg in `ls ${dist}/flavours/router/pkg`
do
  pkg -j $1 add /pkg/$pkg
  echo $pkg 'is added.'
done
echo $1 'is created.'
#
jail -r $1
umount ${dist}/$1/dev
umount ${dist}/$1/basejail
echo $1 'unjailed.'
cp /jails/bin/src/zebra.conf /jails/$1/usr/local/etc/quagga/zebra.conf
cp /jails/bin/src/zebra.conf /jails/$1/usr/local/etc/quagga/ripd.conf
cp /jails/bin/src/zebra.conf /jails/$1/usr/local/etc/quagga/ospfd.conf
cp /jails/bin/src/zebra.conf /jails/$1/usr/local/etc/quagga/bgpd.conf
echo 'put config done.'
echo 'quagga_enable="YES"' >> /jails/$1/etc/rc.conf
echo quagga_daemons=\"zebra $2\" >> /jails/$1/etc/rc.conf
echo 'update' $1 'rc.conf'