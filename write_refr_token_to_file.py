import json
import os


def write_refr_token_to_file(tokens_dict, path):
    '''
    Saves token to file. If file doesn't exist creates new one, if exists then modifies existing values with new one
    or just updates with new key, value pair
    :param tokens_dict: dict {"email": "refresh_token"}
    :param path: where to save
    '''
    if not os.path.exists(path):
        with open(path, 'w+') as f:
            json.dump(tokens_dict, f, indent=4)
    else:
        with open(path, "r+") as f:
            #if empty file
            if os.stat(path).st_size == 0:
                json.dump(tokens_dict, f, indent=4)
            else:
                try:
                    tokens_dict.update(json.load(f))
                    f.seek(0)
                    json.dump(tokens_dict, f, indent=4)
                    f.truncate()
                except json.JSONDecodeError as e:
                    print(f"Error reading/writing file with refresh keys.\nFailed to save following: {tokens_dict}")