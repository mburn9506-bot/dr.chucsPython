# eee = dict()
# eee['rita'] = 1
# eee['josephine']=1
# print(eee)
# # {'rita': 1, 'josephine': 1}
# eee['rita'] = eee['rita'] + 1
# print(eee)
# # {'rita': 2, 'josephine': 1}
#===============================
# counts = dict()
# names = ['rita','josephine','michel','rita','josephine']
# for name in names:
#         if name not in counts:
#                 counts[name]=1
#         else:
#                 counts[name]=counts[name]+1
# print(counts)
#output: {'rita': 2, 'josephine': 2, 'michel': 1}
# ============= get method for dictionary ==========================
#===== simplified counting method get() ======
# https://youtu.be/8DvywoWv6fI?t=16990
# counts = dict()
# names = ['rita','josephine','michel','rita','josephine']
# for name in names:
#         counts[name] = counts.get(name,0)+1

# print(counts)
#output:{'rita': 2, 'josephine': 2, 'michel': 1}
# ======= counting words in text ========
# counts = dict()
# print('enter a line of text: ')
# line =input('')
# words = line.split()
# ========words = line.split() means:=======

# ✔️ Take a line of text and split it
# into separate words

# split() (with no arguments) breaks the string 
# wherever 
# it finds whitespace (spaces, tabs, newlines).
#here is an example of split:
# line = "hello world this is python"
# words = line.split()
# print(words)
#output:
# ['hello', 'world', 'this', 'is', 'python']


#============================================
# print('Words: ', words)
# print('counting ....')
# for word in words :
#         counts[word] = counts.get(word, 0)+1
# print('Counts: ',counts)
"""enter a line of text: 
the quick brown fox jumps over the lazy dog 
quick fox brown
Words:  ['the', 'quick', 'brown', 
'fox', 'jumps', 'over', 'the', 'lazy', 'dog', 
'quick', 'fox', 'brown']
counting ....
Counts:  {'the': 2, 'quick': 2, 'brown': 2, 
'fox': 2, 'jumps': 1, 'over': 1, 'lazy': 1,
 'dog': 1}"""
"""dict.get() is a dictionary method in Python that
 lets you safely retrieve a value for a given key. 
 If the key does not exist, it returns a default 
 value instead of giving an error.

When counting words, it's used to initialize 
missing words to 0."""
# counts = {}

# word = "hello", "ritajosephine"
# counts[word] = counts.get(word, 0) + 1
"""dict.get(key, default)

Returns value for key

If key missing → returns default 
(usually 0 when counting)

Perfect for word counting loops!"""
# print(counts)
# https://youtu.be/8DvywoWv6fI?t=17597
name = input('enter file; ')
handle = open(name)

counts = dict()
for line in handle:
        words = line.split()
        for word in words:
                counts[word]= counts.get(word,0)+1

bigcount = None
bigword =None
for word,count in counts.items():
        if bigcount is None or count > bigcount:
                bigword = word
                bigcount = count
print(bigword,bigcount)
#This task of searching and extracting is 
# so common that Python has a very 
# powerful module called regular expressions 
# that handles many of these tasks
