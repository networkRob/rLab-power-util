## rLab Power Utilities
This repo will have scripts to help safely power down ESXI vms, ESXI hosts, any fileservers and integrate with Kasa controlled powerstrips to shut power off.

#### Purpose
The purpose of this ti find a way to easily shutdown my lab environment completely when not in use and to power it back on when needed.

#### Requirements
This script requires the `PyVmomi` PIP package.

#### Example
For `poweroff_vms.py` it can shutdown a specified vm name, portion of vm name or all vms.

```
$ ./poweroff_vms.py --help
usage: poweroff_vms.py [-h] -n NODE -u USER [-p PORT] [-s STRING]

optional arguments:
  -h, --help                    show this help message and exit
  -n NODE, --node NODE          IP or hostname to connect to
  -u USER, --user USER          Username for vCenter/ESXI
  -p PORT, --port PORT          Port to connect to host
  -s STRING, --string STRING    Portion of vm Name to filter

$ ./poweroff_vms.py -n vcenter-01 -u username -s L2-

```

