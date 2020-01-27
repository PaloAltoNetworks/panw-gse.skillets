#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

__metaclass__ = type

#  Copyright 2019 Palo Alto Networks, Inc
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

ANSIBLE_METADATA = {'metadata_version': '0.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: commit_skillet
short_description: Performs a commit operation on the panos device
description:
    - This module performs a 'commit' on the intended device
    - This module does not provide guards of any sort, so USE AT YOUR OWN RISK.
    - Refer to the Skillet documentation for more details
    - https://docs.paloaltonetworks.com/pan-os.html

author: "Nathan Embery (@nembery)"
version_added: "0.1"

requirements:
    - skilletlib

notes:
    - Check mode is not supported.

options:
    provider:
        description:
            - a dict containing 'ip_address', 'username', 'password'
        required: True
        type: complex

'''

EXAMPLES = '''
- name: Commits config
  commit_skillet:
    provider: '{{ provider }}'

'''

RETURN = '''
stdout:
    description: output (if any) from the given commit operation
    returned: success
    type: string
    sample: "{\"snippets\": {}, \"outputs\": {}, \"result\": \"success\", \"changed\": false}}"
'''

from ansible.module_utils.basic import AnsibleModule

try:
    from skilletlib import Panos
    from skilletlib.exceptions import PanoplyException
    import json

except ImportError:
    pass


def main():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        provider=dict(type='dict', required=True)
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
    )

    # create our context dict. Every skillet requires a context that contains connection information
    # as well as any vars required for that particular skillet

    skillet_context = dict()
    skillet_context.update(module.params['provider'])

    ip_address = module.params['provider'].get('ip_address', None)
    username = module.params['provider'].get('username', None)
    password = module.params['provider'].get('password', None)

    try:
        panos = Panos(hostname=ip_address,
                      api_username=username,
                      api_password=password
                      )

        output = panos.commit()

        output_str = json.dumps(output)
        module.exit_json(changed=True, stdout=output_str)

    except PanoplyException as p:
        module.fail_json(msg='{0}'.format(p))


if __name__ == '__main__':
    main()

