#!/usr/bin/env python3

import argparse
from pyHS100 import SmartStrip

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

    try:
        ss = SmartStrip(user_args.plug)
    except:
        return("False")

    for splug in ss.sys_info['children']:
        if user_args.device.lower() in splug['alias'].lower():
            p_ind = ss.sys_info['children'].index(splug)
            if user_args.action.upper() == ss.state[p_ind]:
                print("Noting to do")
            elif user_args.action.upper() == 'ON':
                print("Current State: {0}".format(ss.state[p_ind]))
                ss.turn_on(index=p_ind)
                print("New State: {0}".format(ss.state[p_ind]))
            elif user_args.action.upper() == 'OFF':
                print("Current State: {0}".format(ss.state[p_ind]))
                ss.turn_off(index=p_ind)
                print("New State: {0}".format(ss.state[p_ind]))

if __name__ == "__main__":
    U_OPTS = argparse.ArgumentParser()
    U_OPTS.add_argument("-d", "--device", type=str, help="TurnOff or TurnOn device", required=True)
    U_OPTS.add_argument("-p", "--plug", type=str, help="IP or FQDN of Kasa Plug", required=True)
    U_OPTS.add_argument("-a","--action", type=str, help="TurnOff or TurnOn lab", required=True)
    ARGS = U_OPTS.parse_args()
    main(ARGS)
    