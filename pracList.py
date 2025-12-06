# counts = dict()
# names = ['csev','cwen','csev','sqian','cwen']
# for name in names :
#         if name not in counts:
#                 counts[name]=1
#         else:
#                 counts[name]=counts[name]+1
# print(counts)
# print("------------------")
# if name in counts:
#         x=counts[name]
# else:
#         x = 0
# x = counts.get(name,0)
# print(x)

# counts = dict()
# names = ['csev','cwen','csev','sqian','cwen']
# for name in names:
#         counts[name]= counts.get(name, 0)+1
# print(counts)
# ======== counting words in text =======
# https://youtu.be/8DvywoWv6fI?t=17167
# counts = dict()
# print('enter a line of text: ')
# line = input()
# words = line.split(' ')
# print('words',words)
# print('counting ....')
# for word in words:
#         counts[word]= counts.get(word, 0)+ 1
# print('counts',counts)
# print("==========================")
# counts = {'rita':27,'josephine':26,'michel':65}
# for key in counts:
#         print(key,counts[key])
# print("==========================")
# jjj = {'rita':27,'josephine':26,'michel':65}
# print(list(jjj))
# print(jjj.keys())
# print(jjj.values())
# print(jjj.items())
# ==== two iteration / variable! =======
# https://youtu.be/8DvywoWv6fI?t=17485



# jjj = {'rita':27,'josephine':26,'michel':65}
# # the first variable is the key and the second is the value
# for aaa,bbb in jjj.items():
#         print(aaa,bbb)
#output:
#rita 27
#josephine 26
# michel 65
#===== using two nested loop ========
# https://youtu.be/8DvywoWv6fI?t=17592
# name = input('enter file; ')
# handle = open(name)

# counts = dict()
# for line in handle:
#         words = line.split()
#         for word in words:
#                 counts[word]= counts.get(word,0)+1

# bigcount = None
# bigword =None
# for word,count in counts.items():
#         if bigcount is None or count > bigcount:
#                 bigword = word
#                 bigcount = count
# print(bigword,bigcount)
        
#=======================================
name = input('enter file: ')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None

for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
