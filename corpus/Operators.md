---
title: Operators | VEX AIM - Python API
description: Explore the Python API reference for operators used in VEXcode on a VEX AIM Coding Robot. Find detailed descriptions for operators, usage, and examples.
---


```{highlight} python
:linenothreshold: 5
```
# Operators

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

<!-- In Progress
<div class="inProgressCallout bg-warning">
    <h3 class="text-black"><svg class="inline me-2 mb-1 text-lg text-black" width="2em" height="2em" viewBox="0 0 72 72"
            fill="none" xmlns="http://www.w3.org/2000/svg">
            <g clip-path="url(#clip0_40_48064)">
                <path
                    d="M24 27C24 25.3431 25.3431 24 27 24H45C46.6569 24 48 25.3431 48 27C48 28.6569 46.6569 30 45 30H27C25.3431 30 24 28.6569 24 27Z"
                    fill="currentColor"></path>
                <path
                    d="M24 39C24 37.3431 25.3431 36 27 36H39C40.6569 36 42 37.3431 42 39C42 40.6569 40.6569 42 39 42H27C25.3431 42 24 40.6569 24 39Z"
                    fill="currentColor"></path>
                <path fill-rule="evenodd" clip-rule="evenodd"
                    d="M12 18C12 13.0294 16.0294 9 21 9H51C55.9706 9 60 13.0294 60 18V54C60 58.9706 55.9706 63 51 63H21C16.0294 63 12 58.9706 12 54V18ZM21 15H51C52.6569 15 54 16.3431 54 18V54C54 55.6569 52.6569 57 51 57H21C19.3431 57 18 55.6569 18 54V18C18 16.3431 19.3431 15 21 15Z"
                    fill="currentColor"></path>
            </g>
            <defs>
                <clipPath id="clip0_40_48064">
                    <rect width="72" height="72" fill="white"></rect>
                </clipPath>
            </defs>
        </svg>In Progress</h3>
</div> -->

## Introduction

Operators in Python are special symbols and keywords that allow you to perform operations on values and variables. They encompass a wide range of functionalities—from arithmetic and comparison to logical, bitwise, and assignment operations. Mastering these operators is essential for constructing expressive and efficient Python code, as they form the foundation of nearly every computation or decision-making process in your programs. Below, you’ll find concise examples for each operator to help you understand their usage and expected outcomes.	

### Arithmetic 

| Name | Symbol | Operator | Example |
| --- | :--: | :--: | --- |
| Addition | `+` | `a + b` | `5 + 3 # 8` |
| Division | `/` | `a / b` | `10 / 4 # 2.5  (always returns a float)` |
| Exponentiation | `**` | `a ** b` | `2 ** 3 # 8` |
| Floor Division | `//` | `a // b` | `10 // 4 # 2    (always returns an integer)` |
| Modulo | `%` | `a % b` | `10 % 4 # 2` |
| Multiplication | `*` | `a * b` | `5 * 3 # 15` |
| Negation | `-` | `- a` | `- 5 # -5` |
| Subtraction | `-` | `a - b` | `10 - 3 # 7` |

### Augmented Arithmetic

| Name | Symbol | Operator | Example |
| --- | :--: | :--: | --- |
| Addition | `+=` | `a += b` | `a = 5`<br>`b = 3`<br>`a += b # a = 8` |
| Division | `/=` | `a /= b` | `a = 10`<br>`b = 4`<br>`a /= b # a = 2.5` |
| Exponentiation | `**=` | `a **= b` | `a = 2`<br>`b = 3`<br>`a **= b # a = 8` |
| Floor Division | `//=` | `a //= b` | `a = 10`<br>`b = 4`<br>`a //= b # a = 2` |
| Modulus | `%=` | `a %= b` | `a = 10`<br>`b = 3`<br>`a %= b # a = 1` |
| Multiplication | `*=` | `a *= b` | `a = 2`<br>`b = 3`<br>`a *= b # a = 6` |
| Subtraction | `-=` | `a -= b` | `a = 10`<br>`b = 4`<br>`a -= b # a = 6` |

### Comparison

| Name | Symbol | Operator | Example |
| --- | :--: | :--: | --- |
| Equality | `==` | `a == b` | `5 == 5 # True` |
| Inequality | `!=` | `a != b` | `5 != 10 # True` |
| Greater Than | `>` | `a > b` | `10 > 5 # True` |
| Greater Than or Equal | `>=` | `a >= b` | `10 >= 5 # True` |
| Less Than | `<` | `a < b` | `5 < 10 # True` |
| Less Than or Equal | `<=` | `a <= b` | `5 <= 5 # True` |
| Chained Comparison | `varies` | `a < b < c` | `1 < 2 < 3 # True (1 < 2) and (2 < 3)` |

### Logical

| Name                   | Symbol     | Example   |
|------------------------|:----------:|:-----------------------|
| False                  | `False`    | Certain values are defined to be `False`, including:<ul><li>`None`</li><li>`False`</li><li>Numeric zero of any type: `0`, `0.0`, `0j`</li><li>Empty sequences and collections: `''` (empty string), `[]` (empty list), `()` (empty tuple), `{}` (empty dictionary), `set()`, etc.</li></ul> |
| True                   | `True`     | Any object that is not explicitly `False` is considered `True`. For instance, non-empty strings, non-zero numbers, non-empty lists, and even custom objects (unless they override the truth value methods to return `False`) are treated as `True`. |
---
| Name                   | Symbol     | Operator     |     Example        |
|------------------------|:----------:|:------------:|--------------------|
| Identity               | `is`       | `a is b` |  `[1] is [1] # False` |
| Not Identity           | `is not`   | `a is not b` | `5 is not 10 # True` |
| Logical AND            | `and`      | `a and b` | `True and False # False`|
| Logical Negation       | `not`      | `not a` | `not False # True` |
| Logical OR             | `or`       | `a or b` | `False or True # True` |
| Conditional Expression | `if else`  | `x if condition else y` | `"Yes" if 5 > 3 else "No" # "Yes"` |

### Sequences (Lists, Tuples, Strings)

| Name | Symbol | Operator | Example |
| --- | :--: | :--: | --- |
| Concatenation | `+` | `seq1 + seq2` | `[1, 2] + [3, 4] # [1, 2, 3, 4]` |
| Slice Assignment |  | `seq[i:j] = values` | `lst = [1, 2, 3, 4]`<br>`lst[1:3] = [20, 30] # lst = [1, 20, 30, 4]` |
| Slice Deletion |  | `del seq[i:j]` | `lst = [1, 2, 3, 4]`<br>`del lst[1:3] # lst = [1, 4]` |
| Slicing |  | `seq[i:j]` | `lst = [1, 2, 3, 4]`<br>`lst[1:3] # [2, 3]` |

### Dictionaries (Mappings)

| Name | Symbol | Operator | Example |
| --- | :--: | :--: | --- |
| Indexed Assignment |  | `obj[k] = v` | `d = {}`<br>`d['a'] = 1 # d = {'a': 1}` |
| Indexed Deletion |  | `del obj[k]` | `d = {'a': 1}`<br>`del d['a'] # d =  {}` |
| Indexing |  | `obj[k]` | `d = {'a': 1}`<br>`d['a'] # 1` |

### String Formatting

| Name | Symbol | Operator | Example |
| --- | :--: | :--: | --- |
String Formatting|	%	| `s % obj`	| `str = "Hello, %(name)s" % {"name": "Alice"}    # str = 'Hello, Alice'` |

### Membership

| Name | Symbol | Operator | Example |
| --- | :--: | :--: | --- |
| Containment Test | `in` | `obj in seq` | `'a' in 'cat' # True` |
| Membership Negation (Not In) | `not in` | `a not in b` | `'x' not in 'hello' # True` |

### Bitwise

| Name | Symbol | Operator | Example |
| --- | :--: | :--: | --- |
| Bitwise And | `&` | `a & b` | `6 & 3 # 2 (0b110 & 0b011 = 0b010)` |
| Bitwise Exclusive Or (XOR) | `^` | `a ^ b` | `6 ^ 3 # 5 (0b110 ^ 0b011 = 0b101)` |
| Bitwise Inversion (NOT) | `~` | `~ a` | `~5 # -6 (~0b101 yields -6 in two's complement)` |
| Bitwise Or | `\|` | `a \| b` | `6 \| 3 # 7 (0b110 \| 0b011 = 0b111)` |
| Left Shift | `<<` | `a << b` | `2 << 3 # 16 (0b10 << 3 becomes 0b10000)` |
| Right Shift | `>>` | `a >> b` | `16 >> 2 # 4 (0b10000 >> 2 becomes 0b100)` |

### Augmented Bitwise

| Name | Symbol | Operator | Example |
| --- | :--: | :--: | --- |
| Augmented Bitwise And | `&=` | `a &= b` | `a = 6`<br>`b = 3`<br>`a &= b # a = 2 (0b110 & 0b011 = 0b010)` |
| Augmented Bitwise Exclusive Or (XOR) | `^=` | `a ^= b` | `a = 6`<br>`b = 3`<br>`a ^= b # a = 5 (0b110 ^ 0b011 = 0b101)` |
| Augmented Bitwise Or | `\|=` | `a \|= b` | `a = 6`<br>`b = 3`<br>`a \|= b # a = 7 (0b110 \| 0b011 = 0b111)` |
| Augmented Left Shift | `<<=` | `a <<= b` | `a = 5`<br>`b = 2`<br>`a <<= b # a = 20 (5 << 2 equals 5 * 2²)` |
| Augmented Right Shift | `>>=` | `a >>= b` | `a = 20`<br>`b = 2`<br>`a >>= b # a = 5 (20 >> 2 equals 20 // 2²)` |