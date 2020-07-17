try:
    a,b = input('두수를 넣으세요').split()
    result = (int(a)/int(b))

except Exception as e:
    print ('에러 형태는{}'.format(a))


print('test')