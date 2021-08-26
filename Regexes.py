import re
PhoneNumRegex=re.compile(r'\d{3}-\d{3}-\d{4}')
mo = PhoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found:',mo.group())