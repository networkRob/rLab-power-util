#!/usr/bin/env python3

from time import sleep
import argparse, getpass
import requests

api_url = {
    "shutdown":"/api/v1.0/system/shutdown"
}
pheaders = {
    "Content-Type": "application/json"
}

def main(args):
    node = args.node
    pwd = args.pwd
    response = requests.request("POST","http://{0}{1}".format(node,api_url['shutdown'],headers=pheaders,auth=("root",pwd)))
    print(response.text)


if __name__ == '__main__':
    u_opts = argparse.ArgumentParser()
    u_opts.add_argument("-n","--node",type=str,help="fqdn or IP of FreeNAS",required=True)

    args = u_opts.parse_args()
    args.pwd = getpass.getpass("Password for root on {1}: ".format(args.node))

    main(args)
