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
The variable `self` contains a link to an instance of the class. And we can use not only inner link (`ex1.foo()` or `self.foo()` inside our class) but our own link!

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
