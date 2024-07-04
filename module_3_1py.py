calls = 0
def count_calls():
    global calls
    calls += 1


def string_info(string=''):
    count_calls()
    return ((len(string), string.upper(), string.lower()))


def is_contains(string='', list_to_search=[]):
    count_calls()
    for s in list_to_search:
        if string.casefold() == s.casefold():
            return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(string_info('Abra-Cadabra'))
print(string_info('Велосипед и костыли'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(is_contains('Mannelig', ['Herr', 'mAnNeLiG', 'Herr Mannelig']))
print(calls)