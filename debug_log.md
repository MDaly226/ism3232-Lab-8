# debug_log.md
# Author: Michael Daly

## Bug 1
Error type: Keyerror: 'amount'
File + line: "/home/MDaly/ism3232/module05_functions/week8_buggy.py", and 12
What the error means: The directory key 'amount' is being caled but atleast one of the directories in records doesnt have that key.
What I told the duck: The purpose of get_total() is to return the total value of an order amount paid or due.
What I tried: I added "print(f'DEBUG: rec = {rec}')" to the records code to find any errors and I found that 'amount' was spelt like 'amout'
How I fixed it: I corrected the spelling of 'amount', that correction seems to have fixed it, but now there are new errors.

## Bug 2
Error type: TypeError: '>' not supported between instances of 'int' and 'str'
File + line: "/home/MDaly/ism3232/module05_functions/week8_buggy.py", line 23 and 16
What the error means: This error is saying that python is trying to compare a string and an integer and its not able to do that.
How I fixed it: I removed ' ' from amount to change it from a string to and integer.

## After Fixing Both Bugs
Final output: the final output says "Total: $5150.00 across 3 records
True"
Did pytest pass? Yes

## AI Literacy Reflection
Did I use AI? Yes
If yes -- exact prompt I used: "dont fix the code, just explain the error:
Total: $5150.00 across 3 records
Traceback (most recent call last):
  File "/home/MDaly/ism3232/module05_functions/week8_buggy.py", line 23, in <module>
    print(is_over_limit(total))
          ~~~~~~~~~~~~~^^^^^^^
  File "/home/MDaly/ism3232/module05_functions/week8_buggy.py", line 16, in is_over_limit
    return amount > '1000'
           ^^^^^^^^^^^^^^^
TypeError: '>' not supported between instances of 'int' and 'str'"

What AI explained: "This error means Python is trying to compare two different data types using >
ere:
- amount is an integer (int), such as 5150
- '1000' is a string (str) because it has quotation marks around it
Python does not know how to determine whether a number like 5150 is greater than text like '1000'."
What I changed myself: I fixed the spelling error in the first bug and changed the 1000 from a str to an int in bug 2
Can I explain every fixed line? Yes

## What I learned
I learned that coding bugs can occur very easily, that even a single typo, or even indent can prevent your code from working properly. I feel like moving forward I'm going to be testing my code all the time to try to catch these errors early. Debugging can be a huge headache and I can only imagine what its like trying to find and fix bugs in thousands of lines of code.