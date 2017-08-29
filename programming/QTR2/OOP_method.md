## OOP: Methods
```
class MyClass:
    def method(self):
        return
        
    @classmethod
    def classmethod(cls):
        return
        
    @staticmethod
    def staticmethod():
        return
        
        
# instantialization
obj = MyClass()
```
### instance method
The first method `method(self)` is called a `method` (or `instance method`).

`self` parameter points to `obj`, an instance of `MyClass`.

`self` parameter allows instance method to access attributes and other methods on the same object.

Hence, instance methods can modify an object's state.

Also, through `self.__class__` attribute, instance methods can modify class state.

How to call:  
1. `obj.method()`  
2. `MyClass.method(obj)`

### @classmethod
`@classmethod` decorator marks the below `classmethod(cls)` as a `class method`.

`cls` parameter points to `MyClass`, a class - not instance or object.

Because of the lack of `self` parameter, class methods cannot modify object instance state.

However, because `cls` parameter allows modifying class state, the modification can be applied to all instances of the class.

How to call:  
1. `obj.classmethod()`  
2. `MyClass.classmethod()`
### @staticmethod
`@staticmethod` decorator marks the below `staticmethod()` as a `static method`.

Because it takes neither `self` nor `cls` parameter, it cannot modify object state or class state.

How to call:  
1. `obj.staticmethod()`  
2. `MyClass.staticmethod()`