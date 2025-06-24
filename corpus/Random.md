---
title: Random | VEX AIM - Python API
description: Explore the Python API reference for the random module on a VEX AIM Coding Robot. Find detailed descriptions for functions, usage, and examples.
---

```{highlight} python
:linenothreshold: 5
```
# Random

```{contents}
:local: true
```

<!-- Complete
<div class="completeCallout bg-success">
    <h3 class="text-white"><svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 24 24"
            fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
            class="text-white">
            <polyline points="20 6 9 17 4 12"></polyline>
        </svg>
        Complete</h3>
</div> -->

## Introduction 

Random provides access to Python’s `random` module, which is available by default in VEXcode AIM. These methods let you generate random numbers, floats, and values from lists or ranges—useful for adding unpredictability to games, behaviors, and autonomous decision-making.

Below is a list of available methods:

- [randint](#randint) – Returns a random integer between two values (inclusive).  
- [uniform](#uniform) – Returns a random float between two values.  
- [randrange](#randrange) – Returns a random integer from a range with an optional step.  
- [random](#random) – Returns a random float between 0.0 (inclusive) and 1.0 (exclusive).  
- [getrandbits](#getrandbits) – Returns an integer with a specified number of random bits.  
- [choice](#choice) – Returns a random element from a non-empty list or sequence.  

## Number Generators

### randint

```{vexcode}
id: aim_logic_random
```

`randint` returns a random integer between two values (inclusive), where both values are integers.

**Usage:**<br>
`random.randint(a, b)`

| Parameter | Description |
| --------- | ----------- |
| `a`         | An integer representing the inclusive lower bound of the range. |
| `b`         | An integer representing the inclusive upper bound of the range. |

```python
# Generate a random integer between
# 1 and 10 (inclusive)
random_int = random.randint(1, 10)
robot.screen.print(random_int)

# random_int = (random integer between 1 and 10)
```

### uniform  
`uniform` returns a random float between two values, where both values are floats or integers.

**Usage:**<br>
`random.uniform(start, end)`

| Parameter | Description |
| --------- | ----------- |
| `start`     | A float or integer representing the lower bound of the range. |
| `end`       | A float or integer representing the upper bound of the range. |

```python
# Generate a random float between 5.0 and 10.0
random_uniform = random.uniform(5.0, 10.0)
robot.screen.print(random_uniform)

# random_uniform = (random float between 5.0 and 10.0)
```

### randrange  
`randrange` returns a random integer from a range with an optional step, where both the start and stop values are integers.

**Usage:**<br>
`random.randrange(start, stop, step)`

| Parameter | Description |
| --------- | ----------- |
| `start`     | Optional. An integer representing the inclusive starting value of the range. Default is 0. |
| `stop`      | An integer representing the exclusive ending value of the range. |
| `step`      | Optional. An integer representing the difference between each number in the range. Default is 1. |

```python
# Generate a random integer from
# 0 to 9 (exclusive of 10)
random_range = random.randrange(10)
robot.screen.print(random_range)

# random_range = (random integer from 0 to 9)
```

```python
# Generate a random integer from
# 5 to 15 (exclusive of 15)
random_range = random.randrange(5, 15)
robot.screen.print(random_range)

# random_range = (random integer from 5 to 14)
```

```python
# Generate a random integer from
# 10 to 50, stepping by 5
random_range = random.randrange(10, 50, 5)
robot.screen.print(random_range)

# random_range = (random multiple of 5 between 10 and 45)
```

### random  
`random` returns a random float between 0.0 (inclusive) and 1.0 (exclusive).

**Usage:**<br>
`random.random()`

| Parameter | Description |
| --------- | ----------- |
|         | This method has no parameters. |

```python
# Generate a random float between 0.0 and 1.0
random_float = random.random()
robot.screen.print(random_float)

# random_float = (random float between 0.0 and 1.0)
```

### getrandbits  
`getrandbits` returns an integer with a specified number of random bits, where the number of bits is an integer between 0 and 32.

**Usage:**<br>
`random.getrandbits(n)`

| Parameter | Description |
| --------- | ----------- |
| `n`         | An integer representing the number of random bits `(0 <= n <= 32)`. |

```python
# Generate a random integer with 8 random bits
random_bits = random.getrandbits(8)
robot.screen.print(random_bits)

# random_bits = (random integer between 0 and 255)
```

## Selection

### choice  
`choice` returns a random element from a non-empty list or sequence.

**Usage:**<br>
`random.choice(sequence)`

| Parameter | Description |
| --------- | ----------- |
| `sequence`  | A non-empty sequence (list, tuple, or other indexable object) from which a random element is selected. |

```python
# Choose a random number from a list
random_choice = random.choice([10, 20, 30, 40, 50])
robot.screen.print(random_choice)

# random_choice = (randomly chosen number from the list)
```