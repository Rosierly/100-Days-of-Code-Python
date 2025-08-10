## DAY 14 - NOTES
***

### Setting a Default Parameter
###### Setting a default parameter means giving a function argument a value to use if no value is provided when the function is called.
```python
def greet(name=None):
    if name is None:
        print("Hello, stranger!")
    else:
        print(f"Hello, {name}!")
        
greet()           # Output: 'Hello, stranger!'
greet("Alice")    # Output: 'Hello, Alice!'
```
***
