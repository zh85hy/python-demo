def trim(s):
    if s == '':
        return ''
    if s[0] == ' ':
        return trim(s[1:])
    elif s[-1] == ' ':
        return trim(s[:-1])
    else:
        return s


print(trim('    Hello !  '))
