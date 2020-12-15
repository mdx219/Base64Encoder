SHORT_OPTIONS = 'hUs:f:o:'
LONG_OPTIONS = ['help', 'URLSAFE', 'string=', 'filename=', 'outputname=']

HELPTEXT = """
A Basic Base64 Encoder in python.

USAGE:
-h, --help, -?        :  List this help
-s, --string          :  Accepts a string to encode
-f, --filename        :  Accepts the name of the file to encode
-o, --output          :  Accepts the name of the output file. Default is 'output'

-U, --urlsafe         :  encode in a URL safe format

EXAMPLE:
python encode.py -f ./sample.txt -o ./output.txt  

"""