# пространство имен система в основе которой уникальные имена
#виды пространства имен
#локальные глобальные и встроенные
#из локального пространства имен я могу обратиться к глобалным, но обратное не работает
# a = 5
# b = 10
#print(c, d)# нет
# def printer():
#     #global a, b #использование глобалых переменых
#     c = 15  #локальное пространство имен, используются только в теле функции\
#     d = 20
#     a = 'str'
#     b = 'str2'
#     print(c,d, 'local')
#     print(a, b, 'global') #да
# print(a,b)
# printer()
# print(a,b)
# printer()



calls = 0
def count_call():
    global calls
    calls += 1
    print(calls)
    return calls

def string_info(word):
    count_call()
    return (len(word), word.upper(), word.lower())


def is_contains(word, list_to_search):
    count_call()
    for i in list_to_search:
        if word.lower() == i.lower():
            return True
    return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)

