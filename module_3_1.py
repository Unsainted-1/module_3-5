calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    kortez = (len(string), string.upper(), string.lower())
    print(kortez)
    count_calls()

def is_contains(string, list_to_search):
    if string in list_to_search:
        print(True)
    else:
        print(False)
    count_calls()

string_info('niGGers')
string_info('Omae wo mu, shinderu')
is_contains('Govno', ['govno', 'zadanie'])
is_contains('Yandex', ['Google', 'or', 'Yandex'])

print(calls)