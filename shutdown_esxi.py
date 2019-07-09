#!/usr/bin/env python3

from pyVmomi import vim
from pyVim.connect import SmartConnectNoSSL, Disconnect
import argparse, getpass

MAX_DEPTH = 10
vm_list_poweredon = []

def getvminfo(vm, depth=1):
    # if this is a group it will have children. if it does, recurse into them
    # and then return
    if hasattr(vm, 'childEntity'):
        if depth > MAX_DEPTH:
            return
        vmlist = vm.childEntity
        for child in vmlist:
            getvminfo(child, depth+1)
        return

    summary = vm.summary
    if summary.runtime.powerState == 'poweredOn':
        if args.string:
            if args.string.lower() in summary.config.name.lower():
                vm_list_poweredon.append(vm)
        else:
            vm_list_poweredon.append(vm)

def main(args):
    si = SmartConnectNoSSL(host=args.node,user=args.user,pwd=args.pwd,port=args.port)

    content = si.RetrieveContent()

    for child in content.rootFolder.childEntity:
        dc = child
        vmfolder = dc.vmFolder
        vmlist = vmfolder.childEntity
        for vm in vmlist:
            getvminfo(vm)
    if vm_list_poweredon:
        for vm in vm_list_poweredon:
            if vm.summary.guest.toolsRunningStatus == "guestToolsRunning":
                print("Shutting down {}".format(vm.summary.config.name))
                vm.ShutdownGuest()
            else:
                print("Powering Off {}".format(vm.summary.config.name))
                vm.PowerOff()
    else:
        print("No vms to power off")
    
    searcher = si.content.searchIndex
    host = searcher.FindByDnsName(dnsName=args.node,vmSearch=False)
    host.Shutdown(0)

    Disconnect(si)

if __name__ == '__main__':
    u_opts = argparse.ArgumentParser()
    u_opts.add_argument("-n","--node",type=str,help="fqdn to connect to",required=True)
    u_opts.add_argument("-u","--user",type=str,help="Username for vCenter/ESXI",required=True)
    u_opts.add_argument("-p","--port",type=int,help="Port to connect to host",default=443,required=False)
    u_opts.add_argument("-s","--string",type=str,help="Portion of vm Name to filter",required=False)

    args = u_opts.parse_args()
    args.pwd = getpass.getpass("Password for {0} on {1}: ".format(args.user,args.node))

    if args.string:
        main(args)
    else:
        print("Will shutdown all vms!")
        if 'y' == input("Are you sure? [y/n] ").lower():
            main(args)
        else:
            print("Aborting")
