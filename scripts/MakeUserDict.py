#!/usr/bin/python3
import argparse

# Define arguments
parser = argparse.ArgumentParser(description='generate file with names for enumeration(basically for kerberos')
parser.add_argument('-f', '--file',
                    action='store',
                    dest='source_file',
                    required=True,
                    help='specify file with names'
                    )
parser.add_argument('-o', '--output',
                    action='store',
                    dest='dest_file',
                    required=True,
                    help='output to file'
                    )

args = parser.parse_args()


class Names:

    def __init__(self, original_name):
        self.original_name = original_name
        self.dot_name = self.make_dot_name()
        self.long_name = self.make_long_name()
        self.short_name = self.make_short_name()
        self.other_names = [self.original_name, self.dot_name, self.long_name, self.short_name]
        self.other_names_filtered = list(filter(None, self.other_names))

    def make_dot_name(self):
        if ' ' in self.original_name:
            dot_name = self.original_name.replace(' ', '.')
            return dot_name
        return None

    def make_long_name(self):
        long_name = ''
        if ' ' in self.original_name:
            parts_of_name = self.original_name.split(' ')
            for part in parts_of_name:
                long_name += part
            return long_name
        return None

    def make_short_name(self):
        short_name = ''
        if ' ' in self.original_name:
            parts_of_name = self.original_name.split(' ')
            name = parts_of_name[0]
            first_letter = name[0]
            parts_of_name[0] = first_letter
            for part in parts_of_name:
                short_name += part
            return short_name
        return None


def main():
    list_of_names = []
    f = open(args.source_file, 'r')
    for name in f:
        list_of_names.append(Names(name))
    if args.dest_file:
        d = open(args.dest_file, 'w')
        for object in list_of_names:
            for name_variant in object.other_names_filtered:
                d.write(name_variant.lower())


if __name__ == '__main__':
    main()

