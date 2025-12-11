add = lambda x:x+1
print(add(3))
add_numbers = lambda x, y: x+y
print(add_numbers(3,5))
letters = ['yyyy','zzz','aaaa','xxxxx','wwwww']
print(letters)
#output:['yyyy', 'zzz', 'aaaa', 'xxxxx', 'wwwww']

# this sort the list according to word length 
letters.sort(key = lambda x:len(x))
print(letters)
#output:['zzz', 'yyyy', 'aaaa', 'xxxxx', 'wwwww']
def add_one(n):
        return lambda x: x+n
number = add_one(20)
print(number(1))