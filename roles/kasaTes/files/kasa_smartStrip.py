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
        return({"msg":"Unable to connect to {}".format(user_args.plug)})
    return({"msg":"Success {}".format(", ".join([user_args.plug,user_args.device]))})
    # for splug in ss1.sys_info['children']:
    #     L_PLUGS.append(Plugs(splug['alias'], \
    #         ss1.sys_info['children'].index(splug), ss1, splug['state']))
    # for splug in ss2.sys_info['children']:
    #     L_PLUGS.append(Plugs(splug['alias'], \
    #         ss2.sys_info['children'].index(splug), ss2, splug['state']))

if __name__ == "__main__":
    U_OPTS = argparse.ArgumentParser()
    U_OPTS.add_argument("-d", "--device", type=str, help="TurnOff or TurnOn device", required=True)
    U_OPTS.add_argument("-p", "--plug", type=str, help="IP or FQDN of Kasa Plug", required=True)
    U_OPTS.add_argument("-a","--action", type=str, help="TurnOff or TurnOn lab", required=True)
    ARGS = U_OPTS.parse_args()
    main(ARGS)
    