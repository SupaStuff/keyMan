#!/usr/bin/env python
import os
import sys
import json
from sys import argv

if __name__ == "__main__":
    path2keys = os.environ.setdefault("PATHTOKEYS", os.path.expanduser("~")+"/keys.json")
    if not os.path.exists(path2keys):
        newFile = open(path2keys, 'w+')
        newFile.write("{}")
        newFile.flush()
        newFile.close()
    with open(path2keys) as json_file:    
        keys = json.load(json_file)

    if len(argv) == 1 :
        print("""
            USAGE\n
            keyMAN set KEY \"VALUE\"\tsets a key,value pair\n
            keyMAN remove KEY\t\tremoves a key\n
            keyMAN list CATEGORY\tshow all keys in CATEGORY\n
            keyman get KEY\t\tdisplays the value for KEY
        """)
    else :
        if len(argv) > 1 :
            key = argv[2].split('.')
        if argv[1] == "set" :
            keys[key[0]][key[1]] = argv[3]
            with open(path2keys, 'w') as json_file:
                json_file.write(json.dumps(keys, sort_keys=True, indent=4, separators=(',', ': ')))
        elif argv[1] == "remove" :
            del keys[key[0]][key[1]]
            with open(path2keys, 'w') as json_file:
                json_file.write(json.dumps(keys, sort_keys=True, indent=4, separators=(',', ': ')))
        elif argv[1] == "list" :
            for k in keys[key[0]].keys():
                print(k)
        elif argv[1] == "get":
            print(json.dumps(keys[key[0]][key[1]], sort_keys=True, indent=4, separators=(',', ': ')))
        else :
            print(argv[1] + "is not a valid option")
    #with open(path2keys, 'w') as json_file:
        #json_file.write()
