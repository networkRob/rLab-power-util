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
module: kasa_smartstrip_getplugs

short_description: Module to get plug information of a Kasa Smart Strip

version_added: "2.8"

description:
    - "This module will get plug information of a Kasa Smart Strip."

options:
    ss_plug:
        description:
            - The fqdn or IP address for the smart strip
        required: true
    name:
        description:
            - Return plugs the match the exact name (alias) or partial match.

author:
    - Rob Martin (@networkRob)
'''

from ansible.module_utils.basic import AnsibleModule
from pyHS100 import SmartStrip

def ss_get_powerstate(ss, plug_ind):
    return(ss.state[plug_ind])

def ss_get_plugs(ss, name):
    """
    Gets all information on Smart Strip about each plug.
    """
    tmp_plugs = []
    for plug in ss.get_alias():
        tmp_dict = {}
        if name:
            if name.lower() in ss.get_alias(index=plug).lower():
                tmp_dict['name'] = ss.get_alias(index=plug)
                tmp_dict['index'] = plug
                tmp_dict['powerstate'] = ss_get_powerstate(ss, plug)
        else:
            tmp_dict['name'] = ss.get_alias(index=plug)
            tmp_dict['index'] = plug
            tmp_dict['powerstate'] = ss_get_powerstate(ss, plug)
        if tmp_dict:
            tmp_dict['host'] = ss.host
            tmp_plugs.append(tmp_dict)
    return(tmp_plugs)


def main():
    """ 
    main entry point for module execution
    """
    argument_spec = dict(
        ss_plug=dict(required=True),
        name=dict(required=False)
    )

    module = AnsibleModule(argument_spec=argument_spec,
                           supports_check_mode=False)
    result = dict(changed=False)

    smart = SmartStrip(module.params['ss_plug'])

    result['plugs'] = ss_get_plugs(smart, module.params['name'])
        
    module.exit_json(**result)
    
if __name__ == "__main__":
    main()