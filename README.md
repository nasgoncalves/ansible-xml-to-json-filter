# Ansible XML to JSON filter

Custom filter plugin to convert XML outputs to JSON. There is not external 
dependencies. Every node attribute name is prefixed by using a '@'. 
Example:

```
"{{ '<test>this is a test</test>' | xml_to_jdon }}"
```

## How to use

Create a `ansible.cfg` file in the root of your playbook path. Add the following
content: 

```
[defaults]
filter_plugins = ./filter_plugins
```

## Run

`playbook.yml` defines a simple use case that uses a nmap XML output o test the
plugin. Due the type of network scan you should use the following command to
execute the playbook.

```
$ ansible-playbook playbook.yaml --ask-become-pass --become
```

