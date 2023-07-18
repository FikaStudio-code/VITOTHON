import os
import sys
sys.path.append(os.pardir)

from src.vitothon import Operator
import subprocess

global jails
jails = "/jails"

op = Operator()
op.setupnode("server01")
op.setupbridge("bridge01")

# Host - bridge01
epaira, epairb = op.createpair()
op.assignip(None, epaira, "192.168.100.254", "255.255.255.0")
op.connect("bridge01", epairb)
op.up(None, epaira)
op.up("bridge01", epairb)

# server01 - bridge01
epaira, epairb = op.createpair()
op.connect("server01", epaira)
op.connect("bridge01", epairb)
op.assignip("server01", epaira, "192.168.100.1", "255.255.255.0")
op.up("server01", epaira)
op.up("bridge01", epairb)