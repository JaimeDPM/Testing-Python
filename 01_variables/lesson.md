# Topic 1: Variables and data types

## What is a variable?

A variable is a name you give to a value so you can use it later. In Python you don't need to declare the type, you just assign:

```python
name = "Jaime"
age = 30
```

## Basic data types

```python
text = "Hello"          # str (string)
whole_number = 10       # int
decimal_number = 3.14   # float
is_true = True          # bool (True or False)
```

You can check the type of any variable with `type()`:

```python
print(type(whole_number))   # <class 'int'>
```

## Basic operations

```python
addition = 5 + 3        # 8
subtraction = 5 - 3     # 2
multiplication = 5 * 3  # 15
division = 5 / 3        # 1.666...
```

## Combining text and variables (f-strings)

```python
name = "Jaime"
age = 30
print(f"My name is {name} and I'm {age} years old")
```

## input() — asking the user for data

```python
name = input("What's your name? ")
print(f"Hello, {name}")
```

Careful: `input()` always returns text (str), even if the user types a number. If you need it as a number, you have to convert it:

```python
age = int(input("How old are you? "))
```

## Now go to `exercise.py` and complete the tasks marked with `# TODO`
