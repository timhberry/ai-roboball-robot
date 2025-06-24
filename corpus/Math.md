---
title: Math | VEX AIM - Python API
description: Explore the Python API reference for the math module on a VEX AIM Coding Robot. Find detailed descriptions for functions, usage, and examples.
---

```{highlight} python
:linenothreshold: 5
```
# Math

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

Math includes both built-in Python functions and the full `math` module, which is automatically available in VEXcode AIM. These tools allow you to perform everything from basic arithmetic to advanced trigonometry, rounding, and logarithmic operations.

Use these functions and constants to calculate positions, angles, distances, and other numeric values for your robot. You can also convert between degrees and radians, evaluate expressions, and work with special values like infinity and NaN.

Below is a list of available math functions, constants, and utilities:

**Built-in Functions – Common math tools included with Python.**  
- [abs](#abs) – Returns the absolute value of a number.  
- [round](#round) – Rounds a number to a specified number of decimal places.  
- [min](#min) – Returns the smallest of the input values.  
- [max](#max) – Returns the largest of the input values.  
- [sum](#sum) – Adds up all values in an iterable.  
- [divmod](#divmod) – Returns the quotient and remainder as a tuple.  
- [pow](#pow) – Raises a number to a power, optionally with a modulus.  
- [int](#int) – Converts a value to an integer.  
- [float](#float) – Converts a value to a floating-point number.  

**Constants – Predefined values from the `math` module.**  
- [math.pi](#pi) – The constant π (pi).  
- [math.tau](#tau) – The constant tau (2π).  
- [math.e](#e) – Euler’s number, base of the natural log.  
- [math.inf](#inf) – Positive infinity.  
- [math.nan](#nan) – Not a Number (NaN).  

**Trigonometry – Calculate angles and relationships between sides.**  
- [math.sin](#sin) – Sine of an angle in radians.  
- [math.cos](#cos) – Cosine of an angle in radians.  
- [math.tan](#tan) – Tangent of an angle in radians.  
- [math.atan](#atan) – Arctangent of a value in radians.  
- [math.atan2](#atan2) – Arctangent of y/x in radians, considering the quadrant.  
- [math.asin](#asin) – Arcsine of a value in radians.  
- [math.acos](#acos) – Arccosine of a value in radians.  
- [math.degrees](#degrees) – Converts radians to degrees.  
- [math.radians](#radians) – Converts degrees to radians.  

**Hyperbolics – Advanced trig-related functions.**  
- [math.sinh](#sinh) – Hyperbolic sine of a value.  
- [math.cosh](#cosh) – Hyperbolic cosine of a value.  
- [math.tanh](#tanh) – Hyperbolic tangent of a value.  
- [math.asinh](#asinh) – Inverse hyperbolic sine.  
- [math.acosh](#acosh) – Inverse hyperbolic cosine.  
- [math.atanh](#atanh) – Inverse hyperbolic tangent.  

**Rounding & Absolute Value – Adjust precision or direction.**  
- [math.ceil](#ceil) – Rounds up to the nearest integer.  
- [math.floor](#floor) – Rounds down to the nearest integer.  
- [math.trunc](#trunc) – Removes the decimal portion.  
- [math.fabs](#fabs) – Returns the absolute value as a float.  

**Exponents & Logarithms – Power, root, and log calculations.**  
- [math.pow](#pow) – Raises a number to a power.  
- [math.sqrt](#sqrt) – Returns the square root.  
- [math.exp](#exp) – Calculates e to the power of x.  
- [math.log](#log) – Natural logarithm (base e).  
- [math.log10](#log10) – Base-10 logarithm.  
- [math.log2](#log2) – Base-2 logarithm.  
- [math.factorial](#factorial) – Factorial of an integer.  
- [math.expm1](#expm1) – More accurate result for `e^x - 1`.  

**Floating Point Operations – Inspect or decompose float values.**  
- [math.modf](#modf) – Returns the fractional and integer parts of a float.  
- [math.frexp](#frexp) – Decomposes a number into mantissa and exponent.  
- [math.fmod](#fmod) – Remainder with sign of the dividend.  
- [math.copysign](#copysign) – Returns a value with the sign of another.  
- [math.ldexp](#ldexp) – Computes `x * (2 ** exp)`.  

**Comparison & Approximation – Check values with tolerances or categories.**  
- [math.isclose](#isclose) – Tests if two values are approximately equal.  
- [math.isfinite](#isfinite) – Checks if a number is finite.  
- [math.isinf](#isinf) – Checks if a number is infinite.  
- [math.isnan](#isnan) – Checks if a value is NaN.  

**Error & Gamma – Special mathematical functions.**  
- [math.gamma](#gamma) – Gamma function (generalized factorial).  
- [math.lgamma](#lgamma) – Logarithmic gamma.  
- [math.erf](#erf) – Error function.  
- [math.erfc](#erfc) – Complementary error function.  

## Built-In Functions

Python provides several built-in functions that allow you to perform mathematical operations inside your project.

### abs

`abs` returns the absolute value of a number, removing any negative sign.


**Usage:**<br>
`abs(x)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | An integer or float. |

```python
# Get the absolute value of -10
abs_result = abs(-10)
robot.screen.print(abs_result)

# abs_result = 10
```

### round

```{vexcode}
id: aim_logic_round
```

`round` rounds a number to a specified number of decimal places.

**Usage:**<br>
`round(x, ndigits)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | An integer or float. |
| `ndigits`         | Optional. The number of decimal places to round to. The default is 0. |

```python
# Round 5.7 to the nearest integer
round_int_result = round(5.7)
robot.screen.print(round_int_result)

# round_int_result = 6
```

```python
# Round 3.14159 to 2 decimal places
round_result = round(3.14159, 2)
robot.screen.print(round_result)

# round_result = 3.14
```

### min

`min` returns the smallest value from multiple arguments or an iterable.

**Usage:**<br>
`min(arg1, arg2, ...)` or `min(sequence)`

| Parameter | Description |
| --------- | ----------- |
| `arg1`, `arg2`, ...         | The numbers to compare. |
| `sequence`         | A list, tuple, or other sequence containing numbers. |

```python
# Get the smallest number from 3, 7, and 1
min_result = min(3, 7, 1)
robot.screen.print(min_result)

# min_result = 1
```

```python
# Get the smallest value from a list
min_list_result = min([10, 4, 25, 1])
robot.screen.print(min_list_result)

# min_list_result = 1
```

### max

`max` returns the largest value from multiple arguments or an iterable.

**Usage:**<br>
`max(arg1, arg2, ...)` or `max(sequence)`

| Parameter | Description |
| --------- | ----------- |
| `arg1`, `arg2`, ...         | The numbers to compare. |
| `sequence`         | A list, tuple, or other sequence containing numbers. |

```python
# Get the largest number from 3, 7, and 1
max_result = max(3, 7, 1)
robot.screen.print(max_result)

# max_result = 7
```

```python
# Get the largest value from a list
max_list_result = max([10, 4, 25, 1])
robot.screen.print(max_list_result)

# max_list_result = 25
```

### sum

`sum` adds up all values in an iterable, with an optional starting value.

**Usage:**<br>
`sum(sequence, start)`

| Parameter | Description |
| --------- | ----------- |
| `sequence`         | A list, tuple, or other sequence containing numbers. |
| `start`         | Optional. A value to add to the sum. Default is 0. |

```python
# Calculate the sum of a list of numbers
sum_result = sum([1, 2, 3, 4, 5])
robot.screen.print(sum_result)

# sum_result = 15
```

```python
# Calculate the sum of a list with a starting value of 10
sum_with_start = sum([1, 2, 3], 10)
robot.screen.print(sum_with_start)

# sum_with_start = 16
```

### divmod

`divmod` returns a tuple containing the quotient and remainder of a division operation.

**Usage:**<br>
`divmod(a, b)`

| Parameter | Description |
| --------- | ----------- |
| `a`         | The dividend. |
| `b`         | The divisor. |

```python
# Perform integer division and remainder of 10 / 3
divmod_result = divmod(10, 3)
robot.screen.print(divmod_result)

# divmod_result = (3, 1)
```

### pow

```{vexcode}
id: aim_logic_power
```

`pow` raises a number to a power and optionally performs a modulus operation.

**Usage:**<br>
`pow(x, y, mod)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | The base number. |
| `y`         | 	The exponent. |
| `mod`         | Optional. A modulus value. If provided, returns `(x ** y) % mod`. |

```python
# Calculate 2 raised to the power of 3
pow_result = pow(2, 3)
robot.screen.print(pow_result)

# pow_result = 8
```

```python
# Calculate (5 ** 3) % 7
pow_mod_result = pow(5, 3, 7)
robot.screen.print(pow_mod_result)

# pow_mod_result = 6
```

### int

`int` converts a number or string into an integer. It also supports base conversion when converting from a string.

**Usage:**<br>
`int(x, base)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | A number, string, or other object to convert. |
| `base`         | Optional. The number base to use for conversion. Default is 10. |

```python
# Convert a float to an integer to get rid of decimals
price = 19.99
price_int = int(price)
robot.screen.print(f"{price_int} coins")

# Output: 19 coins
```

```python
# Convert a string into an integer to use in calculations
user_input = "55"
user_number = int(user_input)
robot.screen.print(user_number * 2)

# Output: 110
```

### float

`float` converts a number or string into a floating-point number.

**Usage:**<br>
`float(x)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | A number, string, or other object to convert. |

```python
# Convert division result to a float
num_apples = 6
num_people = 2
apples_per_person = float(num_apples) / num_people
robot.screen.print(apples_per_person)

# Output: 3.00
```

```python
# Convert a string into a float to use in calculations
user_input = "23.4"
user_number = float(user_input)
robot.screen.print(user_number * 3)

# Output: 70.20
```

## Math Module

The `math` module in MicroPython provides additional methods for performing common mathematical calculations. These methods include trigonometric, logarithmic, and other numerical operations.

The `math` module is imported by default in VEXcode.

### Constants

Constants are predefined values that remain fixed during a project. They can be used in calculations without requiring any definition or assignment.

#### pi

`pi` gives the mathematical constant π, the ratio of a circle’s circumference to its diameter.

**Usage:**<br>
`math.pi`

```python
# Calculate the area of a circle with radius 5 using pi
circle_area = math.pi * 5 * 5
robot.screen.print(circle_area)

# circle_area = 78.54
```

#### tau

`tau` gives the value of 2π.

**Usage:**<br>
`math.tau`

```python
# Calculate the circumference of a circle with radius
circumference = math.tau * 5
robot.screen.print(circumference)

# circumference = 31.42
```

#### e

`e` gives the base of the natural logarithm.

**Usage:**<br>
`math.e`

```python
# Calculate e raised to the power of 2
e_power = math.pow(math.e, 2)
robot.screen.print(e_power)

# e_power = 7.39
```

#### inf

`inf` gives positive infinity as a float.

**Usage:**<br>
`math.inf`

```python
# Check if infinity is infinite
inf_value = math.inf

if math.isinf(inf_value):
    robot.screen.print("Infinity")

# Prints "Infinity"
```

#### nan

`nan` represents a special float for "Not a Number" (NaN).

**Usage:**<br>
`math.nan`

```python
# Check if nan is Not a Number
nan_value = math.nan

if math.isnan(nan_value):
    robot.screen.print("Not a Number")

# Prints "Not a Number"
```

### Trigonometry 

#### sin

```{vexcode}
id: aim_logic_sin
```

`sin` calculates the sine of an angle in radians and returns a float.

**Usage:**<br>
`math.sin(x)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | A float or integer representing an angle in radians. |

```python
# Calculate the sine of 30 degrees in radians
sine_result = math.sin(math.radians(30))
robot.screen.print(sine_result)

# sine_result = 0.50
```

#### cos

```{vexcode}
id: aim_logic_cos
```

`cos` calculates the cosine of an angle in radians and returns a float.

**Usage:**<br>
`math.cos(x)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | A float or integer representing an angle in radians. |

```python
# Calculate the cosine of 60 degrees in radians
cosine_result = math.cos(math.radians(60))
robot.screen.print(cosine_result)

# cosine_result = 0.50
```

#### tan

```{vexcode}
id: aim_logic_tan
```

`tan` calculates the tangent of an angle in radians and returns a float.

**Usage:**<br>
`math.tan(x)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | A float or integer representing an angle in radians. |

```python
# Calculate the tangent of 45 degrees in radians
tangent_result = math.tan(math.radians(45))
robot.screen.print(tangent_result)

# tangent_result = 1.00
```

#### atan

```{vexcode}
id: aim_logic_atan
```

`atan` calculates the inverse tangent (arc tangent) of a number and returns a float representing the angle in radians.

**Usage:**<br>
`math.atan(x)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | A float or integer. |

```python
# Calculate the arc tangent of 1 in degrees
arc_tangent_result = math.degrees(math.atan(1.0))
robot.screen.print(arc_tangent_result)

# arc_tangent_result = 45.00
```

#### atan2

```{vexcode}
id: aim_logic_atan2
```

`atan2` calculates the principal value of the inverse tangent of y/x and returns a float representing the angle in radians.

**Usage:**<br>
`math.atan2(y, x)`

| Parameter | Description |
| --------- | ----------- |
| `y`         | A float or integer representing the y-coordinate. |
| `x`         | A float or integer representing the x-coordinate. |

```python
# Calculate the inverse tangent of 1/1 in degrees
atan2_result = math.degrees(math.atan2(1.0, 1.0))
robot.screen.print(atan2_result)

# atan2_result = 45.00
```

#### asin

```{vexcode}
id: aim_logic_asin
```

`asin` calculates the inverse sine (arc sine) of a number and returns a float representing the angle in radians.

**Usage:**<br>
`math.asin(x)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | A float or integer between -1 and 1. |

```python
# Calculate the arc sine of 0.5 in degrees
arc_sine_result = math.degrees(math.asin(0.5))
robot.screen.print(arc_sine_result)

# arc_sine_result = 30.00
```

#### acos

```{vexcode}
id: aim_logic_acos
```

`acos` calculates the inverse cosine (arc cosine) of a number and returns a float representing the angle in radians.

**Usage:**<br>
`math.acos(x)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | A float or integer between -1 and 1. |

```python
# Calculate the arc cosine of 0.5 in degrees
arc_cosine_result = math.degrees(math.acos(0.5))
robot.screen.print(arc_cosine_result)

# arc_cosine_result = 60.00
```

#### degrees

`degrees` converts an angle from radians to degrees.

**Usage:**<br>
`math.degrees(x)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | A float or integer representing an angle in radians. |

```python
# Convert pi radians to degrees
degrees_result = math.degrees(math.pi)
robot.screen.print(degrees_result)

# degrees_result = 180.00
```

#### radians

`radians` converts an angle from degrees to radians.

**Usage:**<br>
`math.radians(x)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | A float or integer representing an angle in degrees. |

```python
# Convert 180 degrees to radians
radians_result = math.radians(180)
robot.screen.print(radians_result)

# radians_result = 3.14
```

### Hyperbolics 

#### sinh

`sinh` calculates the hyperbolic sine of `x`.

**Usage:**<br>
`math.sinh(x)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | A float or integer representing the input value. |

```python
# Calculate the hyperbolic sine of 1
sinh_result = math.sinh(1)
robot.screen.print(sinh_result)

# sinh_result = 1.18
```

#### cosh

`cosh` calculates the hyperbolic cosine of `x`.

**Usage:**<br>
`math.cosh(x)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | A float or integer representing the input value. |

```python
# Calculate the hyperbolic cosine of 1
cosh_result = math.cosh(1)
robot.screen.print(cosh_result)

# cosh_result = 1.54
```

#### tanh

`tanh` calculates the hyperbolic tangent of `x`.

**Usage:**<br>
`math.tanh(x)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | A float or integer representing the input value. |

```python
# Calculate the hyperbolic tangent of 1
tanh_result = math.tanh(1)
robot.screen.print(tanh_result)

# tanh_result = 0.76
```

#### asinh

`asinh` calculates the inverse hyperbolic sine of `x`.

**Usage:**<br>
`math.asinh(x)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | A float or integer representing the input value. |

```python
# Calculate the inverse hyperbolic sine of 1
asinh_result = math.asinh(1)
robot.screen.print(asinh_result)

# asinh_result = 0.88
```

#### acosh

`acosh` calculates the inverse hyperbolic cosine of `x`.

**Usage:**<br>
`math.acosh(x)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | A float or integer greater than or equal to 1. |

```python
# Calculate the inverse hyperbolic cosine of 2
acosh_result = math.acosh(2)
robot.screen.print(acosh_result)

# acosh_result = 1.32
```

#### atanh

`atanh` calculates the inverse hyperbolic tangent of `x`.

**Usage:**<br>
`math.atanh(x)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | A float between -1 and 1 (exclusive). |

```python
# Calculate the inverse hyperbolic tangent of 0.5
atanh_result = math.atanh(0.5)
robot.screen.print(atanh_result)

# atanh_result = 0.55
```

### Rounding & Absolute Values

#### ceil

```{vexcode}
id: aim_logic_ceil
```

`ceil` rounds a number up to the nearest integer.

**Usage:**<br>
`math.ceil(x)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | A float or integer to be rounded up. |

```python
# Round 3.7 up to the nearest integer
ceil_result = math.ceil(3.7)
robot.screen.print(ceil_result)

# ceil_result = 4
```

#### floor

```{vexcode}
id: aim_logic_floor
```

`floor` rounds a number down to the nearest integer.

**Usage:**<br>
`math.floor(x)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | A float or integer to be rounded down. |

```python
# Round 3.7 down to the nearest integer
floor_result = math.floor(3.7)
robot.screen.print(floor_result)

# floor_result = 3
```

#### trunc

`trunc` removes the decimal part of a number without rounding.

**Usage:**<br>
`math.trunc(x)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | A float to be truncated. |

```python
# Remove the decimal part of 3.7
trunc_result = math.trunc(3.7)
robot.screen.print(trunc_result)

# trunc_result = 3
```

#### fabs

```{vexcode}
id: aim_logic_abs
```

`fabs` returns the absolute value of a number as a float.

**Usage:**<br>
`math.fabs(x)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | A float or integer. |

```python
# Get the absolute value of -3.7
fabs_result = math.fabs(-3.7)
robot.screen.print(fabs_result)

# fabs_result = 3.70
```

### Exponents & Logarithms

#### pow  
`pow` raises x to the power of y and returns a float, even if both inputs are integers.

**Usage:**<br>
`math.pow(x, y)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | A float or integer base. |
| `y`         | A float or integer exponent. |

```python
# Calculate 2 raised to the power of 3
power_result = math.pow(2, 3)
robot.screen.print(power_result)

# power_result = 8.00
```

#### sqrt

```{vexcode}
id: aim_logic_sqrt
```

`sqrt` calculates the square root of a number and returns a float, even for perfect squares.

**Usage:**<br>
`math.sqrt(x)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | A non-negative float or integer. |

```python
# Calculate the square root of 16
sqrt_result = math.sqrt(16)
robot.screen.print(sqrt_result)

# sqrt_result = 4.00
```

#### exp

```{vexcode}
id: aim_logic_exponent
```

`exp` calculates the exponential of a number and returns a float.

**Usage:**<br>
`math.exp(x)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | A float or integer. |

```python
# Calculate e raised to the power of 1
exp_result = math.exp(1)
robot.screen.print(exp_result)

# exp_result = 2.72
```

#### log

```{vexcode}
id: aim_logic_log
```

`log` calculates the natural logarithm of a number and returns a float.

**Usage:**<br>
`math.log(x)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | A positive float or integer. |

```python
# Calculate the natural logarithm (base e) of 7.389056
log_result = math.log(7.389056)
robot.screen.print(log_result)

# log_result = 2.00
```

#### log10

```{vexcode}
id: aim_logic_log10
```

`log10` calculates the base-10 logarithm of a number and returns a float.

**Usage:**<br>
`math.log10(x)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | A positive float or integer. |

```python
# Calculate the base-10 logarithm of 1000
log10_result = math.log10(1000)
robot.screen.print(log10_result)

# log10_result = 3.00
```

#### log2  
`log2` calculates the base-2 logarithm of a number and returns a float, even when `x` is a power of 2.

**Usage:**<br>
`math.log2(x)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | A positive float or integer. |

```python
# Calculate the base-2 logarithm of 8
log2_result = math.log2(8)
robot.screen.print(log2_result)

# log2_result = 3.00
```

#### factorial

`factorial` returns the factorial of an integer `x`, which is the product of all positive integers up to `x`.

**Usage:**<br>
`math.factorial(x)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | A non-negative integer. |

```python
# Calculate 5 factorial (5!)
factorial_result = math.factorial(5)
robot.screen.print(factorial_result)

# factorial_result = 120
```

#### expm1  

`expm1` calculates `e<sup>x</sup> - 1`, which is more accurate for small `x`.

**Usage:**<br>
`math.expm1(x)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | The exponent value. |

```python
# Compute expm1(1) (e^1 - 1)
expm1_result = math.expm1(1)
robot.screen.print(expm1_result)

# expm1_result = 1.72
```

### Floating Point Operations

#### modf  
`modf` decomposes a number into its fractional and integer parts and returns a tuple `(fractional part, integer part)`, both as floats.

**Usage:**<br>
`math.modf(x)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | A float or integer to decompose. |

```python
# Decompose 3.14159 into fractional and integer parts
fractional_part, integer_part = math.modf(3.14159)
robot.screen.print(fractional_part)
robot.screen.next_row()
robot.screen.print(integer_part)

# fractional_part = 0.14
# integer_part = 3.00
```

#### frexp  
`frexp` decomposes a number into its mantissa and exponent and returns a tuple `(mantissa, exponent)`, where the mantissa is a float and the exponent is an integer.

**Usage:**<br>
`math.frexp(x)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | A float or integer to decompose. |

```python
# Decompose 16 into its mantissa and exponent
mantissa, exponent = math.frexp(16)
robot.screen.print(mantissa)
robot.screen.next_row()
robot.screen.print(exponent)

# mantissa = 0.50
# exponent = 5
```

#### fmod

`fmod` returns the remainder of division while keeping the sign of the dividend (`x`).

**Usage:**<br>
`math.fmod(x, y)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | The dividend. |
| `y`         | The divisor. |

```python
# Calculate remainder of 10 / 3
# that preserves the sign of 10
fmod_result = math.fmod(10, 3)
robot.screen.print(fmod_result)

# fmod_result = 1.00
```

#### copysign

`copysign` returns x with the sign of `y`.

**Usage:**<br>
`math.copysign(x, y)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | The value to modify. |
| `y`         | The value whose sign will be copied. |

```python
# Return -10 with the sign of 3 (positive)
copysign_result = math.copysign(-10, 3)
robot.screen.print(copysign_result)

# copysign_result = 10.00
```

#### ldexp

`ldexp` computes `x * (2 ** exp)`, which is equivalent to `x * 2<sup>exp</sup>`.

**Usage:**<br>
`math.ldexp(x, exp)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | The base value. |
| `exp`         | The exponent. |

```python
# Compute 3 * (2 ** 4)
ldexp_result = math.ldexp(3, 4)
robot.screen.print(ldexp_result)

# ldexp_result = 48.00
```

### Comparison & Approximation 

#### isclose  

`isclose` checks if two numbers are approximately equal within a tolerance.

**Usage:**<br>
`math.isclose(a, b, rel_tol, abs_tol)`

| Parameter | Description |
| --------- | ----------- |
| `a`         | The first number to compare. |
| `b`         | The second number to compare. |
| `rel_tol`         | Optional. The maximum allowed difference between a and b, relative to their size. Default is 1e-09 (very small). |
| `abs_tol`         | Optional. A fixed margin of error, useful when comparing numbers close to zero. Default is 0.0. |

**Note:** If both `rel_tol` and `abs_tol` are provided, whichever condition is met first determines the result.

```python
# Check if 1.000000001 and 1.0 are close
# within the default tolerance
isclose_result = math.isclose(1.000000001, 1.0)
robot.screen.print(isclose_result)

# isclose_result = True
```
```python
# Check if 0.0000001 and 0.0 are close
# using absolute tolerance
isclose_result = math.isclose(0.0000001, 0.0, abs_tol=1e-07)
robot.screen.print(isclose_result)

# isclose_result = True
```
```python
# Check if 1000000.0 and 1000000.1 are close
# with a stricter tolerance
isclose_result = math.isclose(1000000.0, 1000000.1, rel_tol=1e-10)
robot.screen.print(isclose_result)

# isclose_result = False
```

#### isfinite  
`isfinite` checks if a number is finite. This method returns a Boolean value:

- `True` - The number is finite.
- `False` - The number is infinite.

**Usage:**<br>
`math.isfinite(x)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | A float or integer to check. |

```python
# Check if 42 is a finite number (returns True)
is_finite_true = math.isfinite(42)
robot.screen.print(is_finite_true)

# is_finite_true = True
```

```python
# Check if infinity is a finite number (returns False)
is_finite_false = math.isfinite(math.inf)
robot.screen.print(is_finite_false)

# is_finite_false = False
```

#### isinf  
`isinf` checks if a number is infinite. This method returns a Boolean value:

- `True` - The number is infinite.
- `False` - The number is finite.

**Usage:**<br>
`math.isinf(x)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | A float or integer to check. |

```python
# Check if infinity is an infinite number (returns True)
is_inf_true = math.isinf(math.inf)
robot.screen.print(is_inf_true)

# is_inf_true = True
```

```python
# Check if 42 is an infinite number (returns False)
is_inf_false = math.isinf(42)
robot.screen.print(is_inf_false)

# is_inf_false = False
```

#### isnan  
`isnan` checks if a number is NaN (Not a Number). This method returns a Boolean value:

- `True` - The number is NaN.
- `False` - The number is a valid number.

**Usage:**<br>
`math.isnan(x)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | A float or integer to check. |

```python
# Check if NaN (Not a Number) is NaN (returns True)
is_nan_true = math.isnan(math.nan)
robot.screen.print(is_nan_true)

# is_nan_true = True
```

```python
# Check if 42 is NaN (returns False)
is_nan_false = math.isnan(42)
robot.screen.print(is_nan_false)

# is_nan_false = False
```

### Error and Gamma Calculations

#### gamma  

`gamma` computes the gamma function of `x`, which generalizes the factorial function for real and complex numbers. For an integer `n`, `gamma(n) = (n-1)!`.

**Usage:**<br>
`math.gamma(x)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | A positive float or integer. |

```python
# Calculate the gamma function of 5 (equivalent to 4!)
gamma_result = math.gamma(5)
robot.screen.print(gamma_result)

# gamma_result = 24.00
```

#### lgamma  

`lgamma` computes the natural logarithm of the `gamma` function.

**Usage:**<br>
`math.lgamma(x)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | A positive float or integer. |

```python
# Calculate the natural logarithm of the
# gamma function of 5
lgamma_result = math.lgamma(5)
robot.screen.print(lgamma_result)

# lgamma_result = 3.18
```

#### erf  

`erf` computes the error function of `x`.

**Usage:**<br>
`math.erf(x)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | A float or integer representing the input value. |

```python
# Calculate the error function of 1
erf_result = math.erf(1)
robot.screen.print(erf_result)

# erf_result = 0.84
```

#### erfc  

`erfc` computes the complementary error function of `x`, which is defined as `1 - erf(x)`.

**Usage:**<br>
`math.erfc(x)`

| Parameter | Description |
| --------- | ----------- |
| `x`         | A float or integer representing the input value. |

```python
# Calculate the complementary error function of 1
erfc_result = math.erfc(1)
robot.screen.print(erfc_result)

# erfc_result = 0.16
```