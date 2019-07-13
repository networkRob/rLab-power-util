#!/usr/bin/env python
import os
import argparse
import json

U_OPTS = argparse.ArgumentParser()
U_OPTS.add_argument("-d", "--device", type=str, help="TurnOff or TurnOn device", required=True)
U_OPTS.add_argument("-p", "--plug", type=str, help="IP or FQDN of Kasa Plug", required=True)
U_OPTS.add_argument("-a","--action", type=str, help="TurnOff or TurnOn lab", required=True)
ARGS = U_OPTS.parse_args()
print(ARGS.action,ARGS.plug,ARGS.device)
