class Parent(object):

    def altered(self):
        print("PARENT altered()")

class Parent2(object):
    
    def altered(self):
        print("second")

class Child(Parent2,Parent):

    def altered(self):
        print("Child, before panrent altered()")
        super(Parent2,self).altered()
        print("child, after")

dad = Parent()
son = Child()

dad.altered()
son.altered()
