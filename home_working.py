# import json

b = b'r\xc3\xa9sum\xc3\xa9'.decode('Latin1')
s = b.encode('UTF-8')
c = b'r\xc3\xa9sum\xc3\xa9'.decode('UTf-8')

# if __name__ == '__main__':
print(s, c, sep='\n')
