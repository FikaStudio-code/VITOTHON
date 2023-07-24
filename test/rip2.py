import os
import sys
sys.path.append(os.pardir)

from src.vitothon import Operator
import subprocess

global jails
jails = "/jails"

op = Operator()
op.setupnode("server01")
op.setupnode("server02")
op.setupnode("server03")
op.setuprouter("rip01")
op.setuprouter("rip02")
op.setuprouter("rip03")
op.setuprouter("rip04")
op.setuprouter("rip05")
op.setupbridge("bridge00")

# Host - bridge00
epaira, epairb = op.createpair()
op.assignip(None, epaira, "192.168.100.254", "255.255.255.0")
op.connect("bridge00", epairb)
op.up(None, epaira)
op.up("bridge00", epairb)

# bridge00 - rip01
epaira, epairb = op.createpair()
op.connect("rip01", epaira)
op.connect("bridge00", epairb)
op.assignip("rip01", epaira, "192.168.100.1", "255.255.255.0")
op.up("rip01", epaira)
op.up("bridge00", epairb)

# rip01 - rip02
epaira, epairb = op.createpair()
op.connect("rip01", epaira)
op.connect("rip02", epairb)
op.assignip("rip01", epaira, "10.0.1.1", "255.255.255.0")
op.assignip("rip02", epairb, "10.0.1.2", "255.255.255.0")
op.up("rip01", epaira)
op.up("rip02", epairb)

# rip02 - rip03
epaira, epairb = op.createpair()
op.connect("rip02", epaira)
op.connect("rip03", epairb)
op.assignip("rip02", epaira, "10.0.2.1", "255.255.255.0")
op.assignip("rip03", epairb, "10.0.2.2", "255.255.255.0")
op.up("rip02", epaira)
op.up("rip03", epairb)

# rip03 - rip01
epaira, epairb = op.createpair()
op.connect("rip03", epaira)
op.connect("rip01", epairb)
op.assignip("rip03", epaira, "10.0.3.1", "255.255.255.0")
op.assignip("rip01", epairb, "10.0.3.2", "255.255.255.0")
op.up("rip03", epaira)
op.up("rip01", epairb)

# rip03 - rip04
epaira, epairb = op.createpair()
op.connect("rip03", epaira)
op.connect("rip04", epairb)
op.assignip("rip03", epaira, "10.0.4.1", "255.255.255.0")
op.assignip("rip04", epairb, "10.0.4.2", "255.255.255.0")
op.up("rip03", epaira)
op.up("rip04", epairb)

# rip04 - rip05
epaira, epairb = op.createpair()
op.connect("rip04", epaira)
op.connect("rip05", epairb)
op.assignip("rip04", epaira, "10.0.5.1", "255.255.255.0")
op.assignip("rip05", epairb, "10.0.5.2", "255.255.255.0")
op.up("rip04", epaira)
op.up("rip05", epairb)

# rip01 - server01
epaira, epairb = op.createpair()
op.connect("server01", epaira)
op.connect("rip01", epairb)
op.assignip("server01", epaira, "1.0.0.1", "255.255.255.0")
op.assignip("rip01", epairb, "1.0.0.254", "255.255.255.0")
op.up("server01", epaira)
op.up("rip01", epairb)
op.assigngw("server01", "1.0.0.254")

# rip02 - server02
epaira, epairb = op.createpair()
op.connect("server02", epaira)
op.connect("rip02", epairb)
op.assignip("server02", epaira, "2.0.0.1", "255.255.255.0")
op.assignip("rip02", epairb, "2.0.0.254", "255.255.255.0")
op.up("server02", epaira)
op.up("rip02", epairb)
op.assigngw("server02", "2.0.0.254")

# rip03 - server03
epaira, epairb = op.createpair()
op.connect("server03", epaira)
op.connect("rip03", epairb)
op.assignip("server03", epaira, "3.0.0.1", "255.255.255.0")
op.assignip("rip03", epairb, "3.0.0.254", "255.255.255.0")
op.up("server03", epaira)
op.up("rip03", epairb)
op.assigngw("server03", "3.0.0.254")

# quagga start
op.start("rip01", "quagga")
op.start("rip02", "quagga")
op.start("rip03", "quagga")
op.start("rip04", "quagga")
op.start("rip05", "quagga")