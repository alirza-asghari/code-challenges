The Collatz sequence is as follows:

Start with some given integer n.
If it is even, the next number will be n divided by 2.
If it is odd, multiply it by 3 and add 1 to make the next number.
The sequence stops when it reaches 1.

According to the Collatz conjecture, it will always reach 1. If that's true, you can construct a finite sequence following the aforementioned method for any given integer.

Write a function that takes in an integer n and returns the highest integer in the corresponding Collatz sequence.
