def list_to_string(items):
    if not items:
        return ''
    if len(items) == 1:
        return items[0]
    return ', '.join(items[:-1]) + ', and ' + items[-1]

spam = ['apples', 'bananas', 'tofu', 'cats']
print(list_to_string(spam))