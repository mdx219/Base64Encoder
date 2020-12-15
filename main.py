import getopt
import sys
from encode.file import readfile, writefile, readstring
from vars.vars import SHORT_OPTIONS, LONG_OPTIONS, HELPTEXT


def cli(args):
    try:
        opts, args = getopt.getopt(args, SHORT_OPTIONS, LONG_OPTIONS)
        for option, value in opts:
            if option in ('-h', '--help', '-?'):
                print(HELPTEXT)
            if option in ('-f', '--filename'):
                encoded = readfile(value)
            if option in ('-s', '--string'):
                encoded = readstring(value)
            if option in ('-o', '--output'):
                writefile(encoded, value)
            else:
                writefile(encoded)
    except getopt.error as err:
        print(err)


if __name__ == '__main__':
    cli(sys.argv[1:])

