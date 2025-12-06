# https://youtu.be/ovZsvN67Glc
# in computing a regular expression ,also referred to as "regex" "regexp"
#provide a concise and flexible means for matching strings ot text 
# https://www.rexegg.com/regex-quickstart.php
# you must import the library using "import re"
#you can use "re.search"to see if a string matches an expression similar to using find()
#you can use  "re.find()"to eaxtract portons of a string that matches your expression
# hand = open ('link1.txt')
# for line in hand:
#         line = line.rstrip()
#         if line.find('from: ') >=0:
#                 print(line)
# print("----------------------")
# import re
# hand = open ('link1.txt')
# for line in hand:
#     print(repr(line))

# for line in hand:
#         line = line.rstrip()
#         if re.search('Pharmacy:',line,re.IGNORECASE):
#                 print(line)
"""repr(line) prints the line in raw form, so you can see:

whether "Pharmacy" is uppercase, lowercase, mixed

whether there is a colon :

whether there are extra spaces ('Pharmacy :', ' Pharmacy:')

whether there are tabs ('\tPharmacy:')

invisible characters ('\n', '\r')

any formatting issues"""
# han = open('link1.txt')
# for line in han:
#         line = line.rstrip()
#         wds = line.split()
#         if wds[0] != 'messages'or len(wds)< 3:
#                 continue
#         print(wds[2])
fname = input('enter file name: ')
if len(fname) < 1 : fname = 'link1.txt'
hand = open(fname)
for lin in hand:
        lin = lin.rstrip()
        print(lin)
        wds = lin.split()
        print(wds)
        """ output:enter file name: link1.txt
"Pharmacy text" refers to a service that uses
['"Pharmacy', 'text"', 'refers', 'to', 'a', 'service', 'that', 'uses']
text messages to communicate with patients
['text', 'messages', 'to', 'communicate', 'with', 'patien"""

