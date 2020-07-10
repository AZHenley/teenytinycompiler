# teenytinycompiler

This is a small compiler to demonstrate how compilers work to my students. It compiles our own dialect of BASIC to C, while being written in Python.

Read the tutorial: [Let's make a Teeny Tiny compiler, part 1](http://web.eecs.utk.edu/~azh/blog/teenytinycompiler1.html) as well as [part 2](http://web.eecs.utk.edu/~azh/blog/teenytinycompiler2.html) and [part 3](http://web.eecs.utk.edu/~azh/blog/teenytinycompiler3.html)

The code is split into folders (part1, part2, part3) that correspond with the complete code from the parts of the tutorial. See part3 for the finished compiler.

It supports:
  - Numerical variables
  - Basic arithmetic
  - If statements
  - While loops
  - Print text and numbers
  - Input numbers
  - Labels and goto
  - Comments

Example code:
```
PRINT "How many fibonacci numbers do you want?"
INPUT nums
PRINT ""

LET a = 0
LET b = 1
WHILE nums > 0 REPEAT
    PRINT a
    LET c = a + b
    LET a = b
    LET b = c
    LET nums = nums - 1
ENDWHILE
```
