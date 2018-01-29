# Ansible XML to JSON filter

Custom filter plugin to convert XML outputs to JSON. There is not external 
dependencies. Every node attribute name is prefixed by using a '@'. 
Example:

```
"{{ '<test>this is a test</test>' | from_xml }}"
"{{ '<test>this is a test</test>' | xml_to_json }}"
```

| Filter | Description |
| *from_xml* | Convert XML to python dictionary |
| *xml_to_json | Convert XML to JSON | 

## How to use

Create a `ansible.cfg` file in the root of your playbook path. Add the following
content: 

```
[defaults]
filter_plugins = ./filter_plugins
```

## Run Example

`playbook.yml` defines a simple use case that uses a nmap XML output o test the
plugin. You need to have nmap installed in your system and also make sure you
run the example playbook as root.

```
$ ansible-playbook playbook.yaml --ask-become-pass --become
```

