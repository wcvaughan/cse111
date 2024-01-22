import re

s = "foo123bar"

print(re.search('123', s))

print(re.search('[0-9][0-9][0-9]', s))

print(re.search('1.3', s))

s = 'foo13bar'

print(re.search('1.3', s))