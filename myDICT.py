# my_dict ={"item":"laptop", "price":500}
# print(my_dict)
# print(my_dict["item"])
# my_dict["quantity"]=5
# my_dict['price']=400
# print(my_dict)
# print("-----------------")
# inventory = {"laptop":(500,10),"phone":(100,15)}
# print(inventory)
# print(inventory["phone"][0])
# print(inventory)
# inventory["tablet"]=(200,5)
# print(inventory)
#======== function in python ===========
# def say_hello():
#         print('hey there, code pilot')
# say_hello()
# --------------------
# def say_hello(name):
#         print('hey there, code pilot', name)
#         print("hey", {name})
# say_hello('ritajosephine')
# say_hello('michel')
def add_number(a,b):
        return a + b
result =add_number(3,4)
print(f"result:  {result}")
def multiply_number(x,y,z):
        return x * y * z
product = multiply_number(2,3,4)
print(f"product {product}")
print("-------------------")
def greet_user(name = 'ritajosephine'):
        print(f"hello, {name}")
greet_user()
greet_user("michel")
print("-------------------")
def get_details():
        return 25, "beirut"
age, city = get_details()
print(f"age: {age}, city {city}")
print("==========================")
def clac_all(num1,num2,operation):
        if operation == '+':
                return num1 + num2
        elif operation == '-':
                return num1 - num2
        elif operation == '*':
                return num1 * num2
        else:
                return "oops, pick+, -, or*"
diff = clac_all(5,3,"-")
print(diff)
sum = clac_all(7,5,'+')
print(sum)
mult = clac_all(5,3,'*')
print(mult)
mult = clac_all(4,3,'%')
print(mult)