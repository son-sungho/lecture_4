class Vector2D:

    def __init__(self, x,y):
        self.x = x
        self.y = y
        
    def __eq__(self, other):
        return self.x ==other.x and self.y ==other.y
    if(data):
        return '같습니다'

    else:
        return '다릅니다'
    def __eq__(self , other):
        return self.x ==other.x and self.y ==other.y
    if(data):
        return '같습니다'

    else:
        return '다릅니다'
    # def __eq__(self , other):
    #     return Vector2D(self.x ==other.x , self.y ==other.y,self.z== other.z )
v1 = Vector2D(103,204)
v2 = Vector2D(10,40)
v3 = v1.eq(v2)
v4 = v1==v2
# print(v3)
print(v4)

# print((1,2)==(1,2))
# class Vector3D:
#     def _init_(self,x,y,z): # 변수 x,y,z
#         self.x=x 
#         self.y=y #생성자 만들기
#         self.z=z
#     def _str_(self): #문자열로 출력하려면 사용, 반환 어떻게 하는 지 만든 것
#         return '({},{},{})'.format(self.x, self.y, self.z)
#     def _eq_(self, other):
#         if self.x == other.x and self.y == other.y and self.z == other.z:
#             return 'Vectors are identical'
#         else :
#             return 'Vectors are different'
# v1=Vector3D(1,2,3)
# v2=Vector3D(1,2,4)
# print(v1==v2)