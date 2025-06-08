class ClsEx:

    _class_counter = 0
    _class_mutable = []

    def __init__(self):
        self._instance_counter = 0


    @staticmethod
    def static_mthd(*oter_args, **other_kwargs):
        print("I can't see either the class or the instance")
        print("If follows, I can neither modify class nor instance")
        print('I can be used like a "function in a box"', end="\n\n")

        # print(cls._class_counter)     # can't see 
        # print(self._instance_counter) # can't see


    @classmethod
    def class_mthd(cls, *oter_args, **other_kwargs):
        print(f" I can see my class: {cls}. I got it as the first argument.")

        print("I have access to") 
        cls._class_counter += 1
        print("_class_counter:", cls._class_counter)

        print("Now anyting inside me could see this change")

        print("I can be used as an alternative init method.")

        inner_ex = cls() # creating instance of a ClsEx inside it's class method 
        print(f"inside me was created a new instance {inner_ex}. And it can see all changes at a class level")
        print("let's look at a new instance counter ", inner_ex._class_counter)

        print("and also, for example, I would be helpful to interact with mutable data types")
        # just an example of working mutable data types
        cls._class_mutable.append("a")



    def foo(self, *oter_args, **other_kwargs):
        print( "A am a basic instance method",
             f"I can see my instance: {self}.", 
              " I got it as the fitst argument. I don't work without instance", sep="\n")

        print('I have access to') 
        self._class_counter += 1
        self._instance_counter += 1

        print("_class_counter:", self._class_counter)
        print("_instance_counter:", self._instance_counter)



# let's start with basics and see what and how it can work

print("I can see c_class_couner: ", end="")
print(ClsEx._class_counter)     #  -> 0                | right now class already can see this class-level variable
#print(ClsEx._instance_counter) #  -> AttributeError   | class don't know about this instance-level variable

print()
print("I can see foo: ", end="")
print(ClsEx.foo)                #  -> ClsEx.foo        | class can see this function 
#print(ClsEx.foo())             #  -> TypeError        | class can't execute this function WITHOUT instance   

print("\n\n\n")

# let's do some weird  things 
# we're creating an instance
ex1 = ClsEx()
# and feeding it to our function
ClsEx.foo(ex1)                  #  -> it works!         |  ok, our class could actually execute it's method only with an instance as the first variable

print("\n\n\n")


ClsEx.class_mthd()              #  -> it works!         | we can run classmethod just using a class variable and we can have access to class-level 

# !!! FAN FACT about mutable data types 
# If they are declared at class level,
#  they can change in any instance or call of the class at any time!

# ex1 was created earlier, and we didn't interact with it directly
# BUUUUT(T)
print("ex1 instance has changed!", ex1._class_mutable)

print("\n\n\n")

ClsEx.static_mthd()             #  -> it works          | statimethod works absolutely independently of the class
ex1.static_mthd()               #  -> it works          |  