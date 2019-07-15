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
2. Update the `hosts` file with the appropriate hosts for inventory use.
3. Update the `group_vars/` files that contain authentication information for each inventory item.  I created my authentication strings using `ansible-vault` with vault ids.  Example creating an ansible-vault string to insert would be:
    ```
    ansible-vault encrypt_string --name 'ansible_sudo_pass' '<pwd_string>' --encrypt-vault-id=<vault_id>
    ```
    
    Then copy and paste the output into the appropriate `group_vars/` file.
4. If using Kasa Power SmartStrips, update the following files for proper powering down and up of plugs.
    - `roles/kasaPowerDOWN/defaults/main.yml`
    - `roles/kasaPowerUP/defaults/main.yml`
    
    The `smart_strips` var needs to include either the FQDN or IP address for each/any power strip to be managed.

    In `roles/kasaPowerUP/defaults/main.yml` specify the start order for each grouping. In my usage, I want to:
    
    1. Power up all switches that contain `7280SE`, `3550`, and a PC with `Code` in the Kasa Smart Strip plug aliases.
    2. Once those plugs have been powered on and 2 of my switches: `rtr-01.rob.lab` and `rtr-02.rob.lab` are accessible via ssh continue.
    3. Power up the plugs with aliases containg `Free`
    4. Wait for my FreeNAS server to be accessible via ssh
    5. Power up the plugs with aliases containing `ESXI`
    

#### Usage:
To perform a complete shutdown, run the following command:
```
ansible-playbook -i hosts lab_shutdown.yml
```

To power on the lab:
```
ansible-playbook -i hosts lab_powerup.yml
```
