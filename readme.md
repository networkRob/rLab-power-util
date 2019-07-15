## rLab Power Utilities
This repo will have scripts to help safely power down ESXI vms, ESXI hosts, any fileservers and integrate with Kasa controlled powerstrips to shut power off.

#### Purpose:
The purpose of this to find a way to easily shutdown my lab environment completely when not in use and to power it back on when needed.

#### Requirements:
1. Python3 is required to run this full playbook.  
2. This playbook requires the following PIP packages:
    - `PyVmomi`
    - `pyHS100`

#### Prerequisites:
1. Update the following playbooks to fit the need of your lab: (remove/add roles)
    - `lab_shutdown.yml`
    - `lab_powerup.yml`

#### Usage:
To perform a complete shutdown, run the following command:
```
ansible-playbook -i hosts lab_shutdown.yml
```

To power on the lab:
```
ansible-playbook -i hosts lab_powerup.yml
```
