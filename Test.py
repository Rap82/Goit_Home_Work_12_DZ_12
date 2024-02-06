import json

def write_contacts_to_file(filename, contacts):
    with open(filename, "w") as fh:
        json_dict = {"contacts" : contacts}
        json.dump(json_dict, fh)

def read_contacts_from_file(filename):
    with open(filename, "r") as fh:
        json_dict = json.load(fh)
        return json_dict["contacts"]