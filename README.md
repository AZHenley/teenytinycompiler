_Sponsored by_ 
​<table>
    <tr> 
        <td>  
            <a href="https://www.recall.ai/careers?ashby_jid=7b02811e-bc91-4ef2-925d-f56a5acac13b&utm_source=github&utm_medium=sponsorship&utm_campaign=teenytinycompiler"
                title="recall.ai">
                <img height="60" src="https://recallaidev-public.s3.amazonaws.com/gh/logo-lg.jpg" />
            </a><br>
            <blockquote><i>Processing over 3TB/s of video at peak load, <a
                        href="https://www.recall.ai/careers?ashby_jid=7b02811e-bc91-4ef2-925d-f56a5acac13b&utm_source=github&utm_medium=sponsorship&utm_campaign=teenytinycompiler">now
                        hiring in SF</a></i></blockquote>
        </td>
    </tr>
</table>

# teenytinycompiler

This is a small compiler to demonstrate how compilers work to my students. It compiles our own dialect of BASIC to C, while being written in Python.

Read the tutorial: [Let's make a Teeny Tiny compiler, part 1](https://austinhenley.com/blog/teenytinycompiler1.html) as well as [part 2](https://austinhenley.com/blog/teenytinycompiler2.html) and [part 3](https://austinhenley.com/blog/teenytinycompiler3.html)

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
