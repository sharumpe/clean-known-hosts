#!/usr/bin/env python3
'''Verify the known_hosts file entries. Output only the good ones.

   `clean-known-hosts -h` for more info.
'''

from pathlib import Path
import os
import subprocess
import sys


def main(argv):
    filepath = str(Path.home()) + '/.ssh/known_hosts'

    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    with open(filepath) as fp:
        for line in fp:
            # Break it into parts, and take the last one.
            addr = line.split(' ')[0].split(',')[-1]
            if (testAddress(addr)):
                print(line.rstrip()) 

def testAddress(address):
    try:
        subprocess.run(["ping","-c1","-W1",address], check=True, stdout=subprocess.DEVNULL)
        return True
    except:
        # Nothing to see here...
        return False

    return False


if __name__ == '__main__':
    main(sys.argv)