#!/usr/bin/env python

from base64 import b64encode
import argparse

def main(auth_str):
    auth_code = "Basic {0}".format(b64encode(auth_str.encode()).decode('ascii'))
    return(auth_code)

if __name__ == '__main__':
    u_opts = argparse.ArgumentParser()
    u_opts.add_argument("-u", "--user", type=str, help="Username:", required=True)
    u_opts.add_argument("-p", "--password", type=str, help="Password:", required=True)

    args = u_opts.parse_args()

    auth_parms = "{0}:{1}".format(args.user,args.password)
    main(auth_parms)
