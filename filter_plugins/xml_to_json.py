#!/usr/bin/python

import json
import xml.etree.ElementTree as ET
from collections import defaultdict

class FilterModule(object):

    def etree_to_dict(self, t):
        d = {t.tag: {} if t.attrib else None}
        children = list(t)
        if children:
            dd = defaultdict(list)
            for dc in map(self.etree_to_dict, children):
                for k, v in dc.items():
                    dd[k].append(v)
            d = {t.tag: {k: v[0] if len(v) == 1 else v
                         for k, v in dd.items()}}
        if t.attrib:
            d[t.tag].update(('@' + k, v)
                            for k, v in t.attrib.items())
        if t.text:
            text = t.text.strip()
            if children or t.attrib:
                if text:
                  d[t.tag]['#text'] = text
            else:
                d[t.tag] = text
        return d

    def filters(self):
        return {
            'xml_to_json': self.xml_to_json
        }

    def xml_to_json(self, data):
        root = ET.ElementTree(ET.fromstring(data)).getroot()
        return json.dumps(self.etree_to_dict(root))

