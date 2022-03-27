class Person:
    def __init__(self,param_name) -> None: # 생성자
        # print('hihi',self)
        #self 는 자기자신 가르키는 포인터라 생각하면 된다.
        self.name=param_name

    def talk(self):
        print(f"hi, my name is {self.name}!")

person_1 = Person("유재석")
print(person_1.name)
person_1.talk()
person_2 = Person("박명수")
print(person_2.name)