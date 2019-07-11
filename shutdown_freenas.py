#!/usr/bin/env python3
"""
Module to shutdown a FreeNAS box.
"""

import argparse
import getpass
import requests

API_URL = {
    "shutdown":"/api/v1.0/system/shutdown"
}
PHEADERS = {
    "Content-Type": "application/json"
}

def main(user_args):
    """
    main function.
    """
    node = user_args.node
    pwd = user_args.pwd
    response = requests.request("POST", "http://{0}{1}".format(node, API_URL['shutdown']), \
        headers=PHEADERS, auth=("root", pwd))
    print(response.text)


if __name__ == '__main__':
    U_OPTS = argparse.ArgumentParser()
    U_OPTS.add_argument("-n", "--node", type=str, help="fqdn or IP of FreeNAS", required=True)

    ARGS = U_OPTS.parse_args()
    ARGS.pwd = getpass.getpass("Password for root on {1}: ".format(ARGS.node))

    main(ARGS)
