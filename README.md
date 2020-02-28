# PANW-GSE Skillets

A couple of Ansible modules to execute PAN-OS, Panorama, or Pan-Validation Skillets. For more information, see
https://live.paloaltonetworks.com/t5/Skillets/ct-p/Skillets 


## Project Status

Warning! This project is not-yet released and is under heavy development! 


## Installation

The recommended way to install the modules is (will soon be...) installing the panw-gse.Skillets
Ansible Galaxy role:

```bash

$ ansible-galaxy install panw-gse.skillets

```


---
**NOTE**

This module has not yet been pushed into Ansible galaxy as it is still in heavy development! 

---


## Sample playbooks

```yaml

- name: test my new module
  hosts: localhost

  roles:
  - role: panw-gse.skillets

  tasks:
  - name: Execute Simple Skillet
    execute_skillet:
      skillet_path: '.'
      skillet: 'example_set_skillet'
      provider: '{{ provider }}'
      vars:
        hostname: 'test_hostname'
        firewall_env: 'my_laptop'
    register: skillet_outpput

  - name: dump skillet output
    debug:
      msg: '{{ skillet_output }}'

  - name: Commit config
    commit_skillet:
      provider: '{{ provider }}'

```

## Basic Usage

`execute_skillet` is the primary function to execute a skillet. The arguments are:

* skillet_path: directory in which to recursively search for skillets. This can be the root of a cloned git 
repository for example

* skillet: This is the `name` of the skillet as defined by the `name` attribute in the .meta-cnc skillet definition

* provider: This is a provider dict similar to the standard PAN-OS modules. Expected keys are: 'ip_address', 
'username', 'password'.

* vars: This is where you will customize the skillet variables. Any item present in this list will set the value
of a `variable` defined in the .meta-cnc skillet definition file. Any variable not defined here will use the 
default value from the skillet.

## Support

This template/solution is released under an as-is, best effort, support policy. These scripts should be seen as 
community supported and Palo Alto Networks will contribute our expertise as and when possible. We do not provide 
technical support or help in using or troubleshooting the components of the project through our normal support options 
such as Palo Alto Networks support teams, or ASC (Authorized Support Centers) partners and backline support options.
 The underlying product used (the VM-Series firewall) by the scripts or templates are still supported, but the support 
 is only for the product functionality and not for help in deploying or using the template or script itself.

Unless explicitly tagged, all projects or work posted in our GitHub repository 
(at https://github.com/PaloAltoNetworks) or sites other than our official Downloads page on 
https://support.paloaltonetworks.com are provided under the best effort policy.