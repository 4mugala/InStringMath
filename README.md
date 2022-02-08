# About
This program  (algorithm) allows you to bundle basic mathematical computations: addition, subtraction, multiplication, division and exponential. All these being internally inter-converted to get to a possible precise solution.

It is a simple algorithm which is open to any  (if available) enhancements. It is licensed to be permissive for that.

This algorithm is available in both Python and Javascript -- named as main.py and main.js respectively: they are possible direct translation of one another.

CONTRIBUTIONS OF ANY FORMS TO THIS REPOSITORY ARE WELCOME

## Author
Jacob M. Mugala

## License
Copyright 2022 Jacob M. Mugala

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

# API
This is for the InStringMath class -- main class of the program the rest classes just facilitate the computation.

__Note:__ optional arguments are indicated in square brackets. The methods listed below are the only ones to interact with (the other methods are supposed to be private whatsoever).

## InStringMath([args])
class constructor.

args: a string (or list) argument containing a mathematical expression.

## solve(args)
This method takes a string (or list) as arguments containing mathematical computations, it is where after the InStringMath object is instantiated.

## equals()
This method takes no arguments, it return a solution to mathematical expression.

## Usage example
In python:

 ```python
    str_math = InStringMath("5*5")
    print(str_math.equals()) # Outputs 25
    str_math.solve("9^2-80")
    print(str_math.equals()) # Outputs 1
```

In Javascript:

    let strMath = new InStringMath("5*5");
    console.log(strMath.equals()); // Outputs 25
    strMath.solve("9^2-80");
    console.log(strMath.equals()); // Outputs 1
