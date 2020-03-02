#!/usr/bin/python

import getpass, hash.sha3, os

if __name__ == '__main__':

    hash = hash.sha3.Hash('/usr/local/bin/hash/conf.toml')
    password = getpass.getpass('> ')
    os.system("echo '" + hash.exec(password) + "' | xclip -selection clipboard")