#!/bin/bash

#1. Use python3 to run the script TC_1.py and redirect stdout (but not stderr!) to the filename 'test1.txt' and stderr (but not stdout!) to the filename 'error1.txt'

python3 TC_1.py > test1.txt 2> error1.txt

#2. Use python3 to run the script TC_2.py and redirect stdout (but not stderr!) to the filename 'test2.txt' and stderr (but not stdout!) to the filename 'error2.txt'
python3 TC_2.py > test2.txt 2> error2.txt

#3. Produce the difference between TC1 and test1.txt and redirect the output to `student.txt`.
diff TC1 test1.txt > student.txt

#4. Produce the difference between TC2 and test2.txt and **append** the output to `student.txt`. Please remember there is a difference between `>` and `>>`. In this step you are *appending* to a pre-existing file that already has data you do not want to over-write.
diff TC2 test2.txt >> student.txt

