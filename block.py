# coding=utf-8
import json
import os
import hashlib


def get_hash(filename):
    blockchain_dir = os.curdir + '/blockchain/'
    file = open(blockchain_dir + filename, 'rb').read()
    return hashlib.md5(file).hexdigest()


def write_block(name, amount, to_whom, prev_hash=''):
    blockchain_dir = os.curdir + '/blockchain/'

    files = os.listdir(blockchain_dir)
    files = sorted([int(i) for i in files])

    last_file = files[-1]  # последний записанный блок

    filename = str(last_file + 1)

    prev_hash = get_hash(str(last_file))

    data = {
        'name': name,
        'amount': amount,
        'to_whom': to_whom,
        'hash': prev_hash
    }

    with open(blockchain_dir + filename, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    write_block('alex titakob', 4, 'kate')


if __name__ == '__main__':
    main()
