#!/bin/sh
chflags -R noschg /jails/$1
ezjail-admin delete -wf $1