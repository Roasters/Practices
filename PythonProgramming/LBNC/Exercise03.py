# Exercise 1
import re

p = re.compile('(\d{6})-?(\d{7})')
print(p.search('123456-1234567').group(1)+'-xxxxxxx')


p = re.compile('(\d{6})-?\d{7}')
print(p.sub('\g<1>-xxxxxxx','123456-1234567'))


# Exercise 2

List = ['123456-1234567', 1234561234567]

p = re.compile('(\d{6})-?(\d{7})')
for number in List:
    print(p.search(str(number)).group(1)+'-xxxxxxx')

for number in List:
    m = p.match(str(number)).groups()
    print(m[0]+'-'+re.sub('\d', 'X', m[1]))


# Exercise 3

s = '''
회원 명단입니다.
anonymous@daum.net 홍길동
anonymous@naver.com 홍순자
이상입니다.
'''  

p = re.compile('\\b\w+[@]\w+[.]\w+\\b')    # '\\b\w+@[\w.]+\\b'
for address in p.findall(s):
    print(address)