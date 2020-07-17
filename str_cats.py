class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color
                                      # Cat 객체의 문자열 표현방식
    def __str__(self):
        print('Cat(name='+self.name+', color='+self.color+')')
        return 'Cat(name='+self.name+', color='+self.color+')'
nabi = Cat('나비', '검정색')                 # nabi 인스턴스 생성
nero = Cat('네로', '흰색')                   # nero 인스턴스 생성
# nabi()
print(nabi)
print(nero)