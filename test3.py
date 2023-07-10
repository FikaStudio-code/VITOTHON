from vitothon import Operator
import subprocess

global jails
jails = "/jails"

op = Operator()
op.setupnode("server01")
op.setupnode("server02")
op.setuprouter("router01")
op.setuprouter("router02")
op.setupbridge("bridge00")
op.setupbridge("bridge01")
op.setupbridge("bridge02")

# Host - bridge00
epaira, epairb = op.createpair()
op.assignip(None, epaira, "192.168.100.254", "255.255.255.0")
op.connect("bridge00", epairb)
op.up(None, epaira)
op.up("bridge00", epairb)

# bridge00 - router01
epaira, epairb = op.createpair()
op.connect("router01", epaira)
op.connect("bridge00", epairb)
op.assignip("router01", epaira, "192.168.100.1", "255.255.255.0")
op.up("router01", epaira)
op.up("bridge00", epairb)

# bridge00 - router02
epaira, epairb = op.createpair()
op.connect("router02", epaira)
op.connect("bridge00", epairb)
op.assignip("router02", epaira, "192.168.100.2", "255.255.255.0")
op.up("router02", epaira)
op.up("bridge00", epairb)

# router01 - bridge01
epaira, epairb = op.createpair()
op.connect("router01", epaira)
op.connect("bridge01", epairb)
op.assignip("router01", epaira, "10.0.1.254", "255.255.255.0")
op.up("router01", epaira)
op.up("bridge01", epairb)

# router02 - bridge02
epaira, epairb = op.createpair()
op.connect("router02", epaira)
op.connect("bridge02", epairb)
op.assignip("router02", epaira, "10.0.2.254", "255.255.255.0")
op.up("router02", epaira)
op.up("bridge02", epairb)

# bridge01 - server01
epaira, epairb = op.createpair()
op.connect("server01", epaira)
op.connect("bridge01", epairb)
op.assignip("server01", epaira, "10.0.1.1", "255.255.255.0")
op.up("server01", epaira)
op.up("bridge01", epairb)
op.assigngw("server01", "10.0.1.254")

# bridge02 - server02
epaira, epairb = op.createpair()
op.connect("server02", epaira)
op.connect("bridge02", epairb)
op.assignip("server02", epaira, "10.0.2.1", "255.255.255.0")
op.up("server02", epaira)
op.up("bridge02", epairb)
op.assigngw("server02", "10.0.2.254")