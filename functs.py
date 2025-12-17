# https://youtu.be/PszWLQEHjLI?t=12018
# everything you write between'''........''' will go written in file test_file.py created by the function
def create_test_file():
        with open('test_file.py','w')as file:
                file.write('''#michel
def main():
        print(__file__)
        print(f'__name = (__name__)')
if __name__ == '__main__':
        main()
''')
def main():
        print(__file__)
        print(f'__name = (__name__)')
        create_test_file()
if __name__ == '__main__':
        main()