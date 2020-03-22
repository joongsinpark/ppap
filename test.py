import re
d = re.compile('\d+')
e = re.compile('[a-zA-Z]+')

hashTag = ["수블리", "미네랄워터", "2L", "X", "6개"]

hash_string = ""

for string in hashTag:
    if not d.match(string) and not e.match(string): hash_string += "#"+string+" "


print (hash_string)
