import yaml
import json

def main():
    """
    Write a Python program that creates a list. One of the elements of the list
    should be a dictionary with at least two keys. Write this list out to a file
    using both YAML and JSON formats. The YAML file should be in the expanded
    form.
    """

    my_dict = {
        'ip_addr': '178.133.10.9',
        'platform': 'cisco_nxos',
        'vendor':   'cisco',
        'model':    '9000'
    }
    my_list = [
        'something',
        'something else',
        99,
        101,
        'another string',
        my_dict,
        'more info'
    ]

    yaml_file = 'my_test.yml'
    json_file = 'my_test.json'

    with open(yaml_file, "w") as f:
        f.write(yaml.dump(my_list, default_flow_style=False))

    with open(json_file, "w") as f:
        json.dump(my_list, f)

if __name__ == "__main__":
    main()
