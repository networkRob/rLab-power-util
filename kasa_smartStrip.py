#!/usr/bin/env python3

import argparse
from time import sleep
from pyHS100 import SmartStrip

PO_G1 = ['7280SE', '3550']
PO_G2 = ['Free-02', 'PC-Code']
PO_G3 = ['ESXI']
DEMO = ['Monitor']
L_PLUGS = []

class Plugs():
    def __init__(self, name, index, sstrip, pstate):
        self.name = name
        self.index = index
        self.strip = sstrip
        self.state = pstate
    @property
    def getState(self):
        self.state = self.strip.state[self.index]
        return(self.state)
    def turnOn(self):
        self.strip.turn_on(index=self.index)
        self.getState
        return((self.name, self.state))
    def turnOff(self):
        self.strip.turn_off(index=self.index)
        self.getState
        return((self.name, self.state))

def main(user_args):
    # Creating SmartStrip objects
    ss1 = SmartStrip("kasa-ss-1")
    ss2 = SmartStrip("kasa-ss-2")
    for splug in ss1.sys_info['children']:
        L_PLUGS.append(Plugs(splug['alias'], \
            ss1.sys_info['children'].index(splug), ss1, splug['state']))
    for splug in ss2.sys_info['children']:
        L_PLUGS.append(Plugs(splug['alias'], \
            ss2.sys_info['children'].index(splug), ss2, splug['state']))

if __name__ == "__main__":
    U_OPTS = argparse.ArgumentParser()
    U_OPTS.add_argument("-a", "--action", \
        type=str, help="TurnOff or TurnOn lab", required=True)
    ARGS = U_OPTS.parse_args()
    main(ARGS)
    