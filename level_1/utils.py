import json
import re

def parse_string_to_json(new_member):
    new_member = new_member.replace('|', ',').replace('=', ':')
    new_member = re.sub(r'(\w+):', r'"\1":', new_member)
    json_member = json.loads(new_member)
    return json_member
