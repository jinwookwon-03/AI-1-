#lab 9-10 / 1

class Rect:
    def __init__(self, width, height):
        self.width = width
        self. height = height
        
r1= Rect(100, 200)
print(r1.__dict__)
print(r1.__dict__['width'])
# 위 코드 수행 결과
#{'width': 100, 'height': 200}
#100

#lab 9-10 / 2

class Rect:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        
r1= Rect(100, 200)
print(r1.__dict__)
print(r1.__dict__['_Rect__width'])
# 위 코드 수행 결과
#{'_Rect__width': 100, '_Rect__height': 200}
#100
