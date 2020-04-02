#!/usr/bin/env python3
import argparse
import base64


parser = argparse.ArgumentParser(description='encode or decode strings into base64')
parser.add_argument('-f', '--file',
                    dest='sourceFile',
                    action='store',
                    help='specify a file to grab data from it')
parser.add_argument('-w', '--word',
                    dest='word',
                    action='store',
                    help='specify a string to encode/decode')
parser.add_argument('-d', '--decode',
                    dest='decode',
                    action='store_true',
                    help='decode from base64')
parser.add_argument('-e', '--encode',
                    dest='encode',
                    action='store_true',
                    help='encode to base64')
args = parser.parse_args()


def main():

    source_list = []  # list of strings to work with
    result_list = []  # list of decoded or enncoded strings
    if args.sourceFile:
        with open(args.sourceFile, 'r') as f:
            for i in f:
                i = i.rstrip()
                source_list.append(i)

    if args.word:
        source_list.append(args.word)

    if args.decode:
        for i in source_list:
            e = base64.b64decode(i)
            result_list.append(e.decode('ASCII'))
        for i in result_list:
            print(i)

    if args.encode:
        for i in source_list:
            e = base64.b64encode(i.encode('UTF-8'))
            e = str(e, 'UTF-8')
            result_list.append(e)
        for i in result_list:
            print(i)


main()
