#!/usr/bin/env python3
# -*- coding: utf-8 -*

# Copyright: (c) 2019, Rob Martin <@networkRob>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    'metadata_version': '1.0',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: kasa_smartstrip_powerstate

short_description: Module to change the powerstate of a Kasa Smart Strip

version_added: "2.8"

description:
    - "This module will change the power state of a Kasa Smart Strip."

options:
    ss_plug:
        description:
            - The fqdn or IP address for the smart strip
        required: true
    powerstate:
        choices: 
            - on
            - off
        description:
            - Set the powerstate of the plug on the smart strip.
        required: true
    plug_index:
        description:
            - The index ID number of the plug on the powerstrip
    


author:
    - Rob Martin (@networkRob)
'''

import argparse
from ansible.module_utils.basic import AnsibleModule
from pyHS100 import SmartStrip

def ss_turn_on(ss, plug_ind):
    """
    function to change the powerstate of a given index on Kasa Smart Strip.
    """
    tmp_dict = {
        'alias': ss.get_alias(index=plug_ind)
    }
    try:
        ss.turn_on(index=plug_ind)
        tmp_dict['powerstate'] = ss.state[plug_ind]
        tmp_dict['status'] = "Success"
    except:
        tmp_dict['powerstate'] = ss.state[plug_ind]
        tmp_dict['status'] = "Error"
    return(tmp_dict)

def ss_turn_off(ss, plug_ind):
    """
    function to change the powerstate of a given index on Kasa Smart Strip.
    """
    tmp_dict = {
        'alias': ss.get_alias(index=plug_ind)
    }
    try:
        ss.turn_off(index=plug_ind)
        tmp_dict['powerstate'] = ss.state[plug_ind]
        tmp_dict['status'] = "Success"
    except:
        tmp_dict['powerstate'] = ss.state[plug_ind]
        tmp_dict['status'] = "Error"
    return(tmp_dict)

def main():
    """ main entry point for module execution
    """
    argument_spec = dict(
        ss_plug=dict(required=True),
        powerstate=dict(required=True),
        plug_index=dict(type=int, required=True),
    )
    
    module = AnsibleModule(argument_spec=argument_spec,
                           supports_check_mode=False)
    result = dict(changed=False)

    smart = SmartStrip(module.params['ss_plug'])
    if smart.state['plug_ind'].lower() == module.params['powerstate'].lower():
        return(False)
    elif module.params['powerstate'].lower() == 'on':
        result['results'] = ss_turn_on(smart, module.params.plug_ind)
    elif module.params['powerstate'].lower() == 'off':
        result['results'] = ss_turn_on(smart, module.params.plug_ind)
    
    module.exit_json(**result)
    
if __name__ == "__main__":
    main()