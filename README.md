# Class level

Let's start with what our class can see by default. 
<p>Once declared, class variable already has access to class-level variables and it can see all its methods.</p>

```python
class ClsEx:

  _class_counter = 0
  ...

  @staticmethod
  def static_mthd(*oter_args, **other_kwargs):
    ...

  @classmethod
  def class_mthd(cls, *oter_args, **other_kwargs):
    ...

  def foo(self, *oter_args, **other_kwargs):
    ...

print(ClsEx._class_counter)     #  -> 0              
print(ClsEx.class_mthd)         #  -> ClsEx.class_mthd
print(ClsEx.static_mthd)        #  -> ClsEx.static_mthd
print(ClsEx.foo)                #  -> ClsEx.foo

```

Any changes to class-level at this stage will be applied to all instances.

```python
ex0 = ClsEx()

print(ex0._class_counter)  #  -> 0

ClsEx._class_counter += 1  # it modified in all instances

ex1 = ClsEx()

print(ex0._class_counter)  #  -> 1
print(ex1._class_counter)  #  -> 1

```

# Methods

As already mentioned above, class can see class methods. But if we try to run our method we'll get an `TypeError`.

```python
print(ClsEx.foo)   #  -> ClsEx.foo
ClsEx.foo()        #  -> TypeError: missing 1 required positional argument: 'self'
```
The variable `self` contains a reference to an instance of the class. And we can use not only "inner" reference (`ex1.foo()` or `self.foo()` inside our class) but our own reference!

We could use just that, but it's a boring (BUT CORRECT AND PREFER) way 
```python
ex1 = ClsEx()
ex1.foo()       # -> works! boring! boo!
```
And also you could do this!
```python
ex1 = ClsEx()
ClsEx.foo(ex1)   # -> works! but remember: you can doesn't mean you should
```

# @classmethod

Classmethod can be called directly from the class. But you also can call it from any instance.
```python
class ClsEx:
  ...

  @classmethod
  def class_mthd(cls, *oter_args, **other_kwargs):
    ...

ClsEx.class_mthd()  #  -> works!

ex1 = ClsEx()
ex1.class_mthd()    #  -> also works!
```
Unlike simple methods, which receive a reference to an instance as an `stlf` variable as input, classmethod receive a reference to a whole class as the first parameter. Usually it's called `cls`.

Any class-level variable changed in classmethod will be changed in all instances (and in a class as a whole). Let's look at this with the following example.
In the example we have a class-level variable `_class_counter` in our class. Our `classmerhod` will change the state of this variable. 

```
class ClsEx:
  _class_counter = 0

  @classmethod
  def class_mthd(cls, *oter_args, **other_kwargs):
    cls._class_counter += 1
```

Let's create an instance `ex0`. This instance is created before any classmethod functions calls. Then we call our classmethod function from class. Then we create another instance `ex1` and we call classmethod from it.

```python
ex0 = ClsEx()

ClsEx.class_mthd()  

ex1 = ClsEx() 
ex1.class_mthd()

print(ClsEx._class_counter)  #  -> 2
print(ex0._class_counter)    #  -> 2
print(ex1._class_counter)    #  -> 2
```
 
As you can see, `_class_counter` was modified even in `ex0` instance, which was created before any classmethod called.

<br>

One possible use of a `classmethod`, besides modifying class-level variables, could be an alternative way to initialize a class.

In the next example we have two ways of class initialisation. One with `__init__` and another with `classmethod`

```python
class ClsEx:

  def __init__(self, width, height):
    self.params = (width, height)

  @classmethod
  def init_default(cls):
    return cls(width=200, height=200)


ex1 = ClsEx(100, 100)
ex2 = ClsEx.init_default()

print(ex1.params)          #  -> (100, 100)
print(ex2.params)          #  -> (200, 200)
```

# @staticmethod

`staticmethod` is a method that is not attached to the state of an instance or class. `staticmethod` doesn't receive an implicit first argument representing the instance (`self`) or the class (`cls`).

Let's move on to an example! \
In this example we can see that our staticmethod could be used as a function goes with our class. It can be used both in class and instance.
```python
class ClsEx:

  @staticmethod
  def wery_useful_calculator(a, b):
    print('a + b = ', str(a) + str(b))


ClsEx.wery_useful_calculator(10,  2)   #  -> 102

ex1 = ClsEx()

ex1.wery_useful_calculator(3, 15)      #  -> 315

```
Typically, staticmethods are used as functions that are required by a class, but whose logic can be moved outside the class's work.
