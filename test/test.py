import os
import sys
sys.path.append(os.pardir)

from src.vitothon import Operator
import subprocess

global jails
jails = "/jails"

op = Operator()
op.setupnode("server01")
epaira, epairb = op.createpair()
op.connect("server01", epaira)
op.assignip("server01", epaira, "192.168.100.1", "255.255.255.0")
op.assignip(None, epairb, "192.168.100.254", "255.255.255.0")
op.up("server01", epaira)
op.up(None, epairb)
op.assigngw("server01", "192.168.100.254")