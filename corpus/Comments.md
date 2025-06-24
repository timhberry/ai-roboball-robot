---
title: Comments | VEX AIM - Python API
description: Explore the Python API reference for using comments on a VEX AIM Coding Robot. Learn how to write comments to document and organize your code.
---


```{highlight} python
:linenothreshold: 5
```

# Comments

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

Comments in Python are used to add explanations or notes within the code. They do not affect how the code runs and are useful for clarifying logic, documenting functionality, or temporarily disabling parts of the code.  

### Comments

A single-line comment starts with `#` (spoken as “hash”) and continues until the end of the line.

```python
# This is a single-line comment
print("Hello!")  # Print a greeting message
```

```python
# Print a greeting and then a farewell
# in the Console
print("Hello!")
print("Goodbye!")
```

### Multiline String Comments

Triple-quoted string comments (`""" """` or `''' '''`) can be used for multiline explanations. Although they are technically string objects, they can function as comments if not assigned to a variable.

```python
"""
This project prints a greeting message,
followed by a farewell message in the
Console.
"""
print("Hello!")
print("Goodbye!")
```