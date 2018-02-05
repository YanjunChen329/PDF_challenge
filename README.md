# PDF_challenge
This repo is the solution for the PDF challenge of Aiden Lab by Yanjun (Anthony) Chen finalized on Febrary 5th. <br />
The solution contains three parts, each of which gives a solution for one of the three challenges.<br />

## 1A Bucket Challenge
### Get started
The solution to 1A bucket challenge is the python file "1A_bucket_challenge.py". It is a command line tool that takes a list of positive integers (bucket sizes) and a positive integer (target value) as inputs, and output 1 or 0 representing whether we could use the specified bucket sizes to reach the target value. Here, the list input should be in the form of "[1, 2, 3]"<br />
Some legal command line examples and results are listed below.

```
$python 1A_bucket_challenge [5, 7] 33
1
$python 1A_bucket_challenge [3, 11, 21] 492
1
$python 1A_bucket_challenge [3, 14, 18] 19
0
```

### Tests
Testing are supported by Python's unittest library. If you want to run the built-in test cases, scorl down in the file to find the last few lines of code like this.

```
# Run
if __name__ == '__main__':
    run()
    # unittest.main()  # Test
```
Comment the third line "run()" and comment out the forth line "unittest.main()  # Test" to run the test cases or add your own test cases

## 1B Number to String
### Get started
The solution to 1B number to string challenge is the python file "1B_number2words.py". It is a command line tool that takes a number string longer than 1 as an input, and output a mix of numbers and words that helps you remember the number. <br />
Some legal command line examples and results are listed below.
```
$python 1B_number2words.py 8432273
vid-card

$python 1B_number2words.py 18002655328
1-u-00-collect

$python 1B_number2words.py 17239699162
1-pad-wow-9-1-ma

$python 1B_number2words.py 776337767
professor
```

### How it works
The project is inspired by [DialABC](http://dialabc.com/about/). It uses the number-letter mapping in phone keypads as the conversion standard and try to substitute as many numbers as possible with meaningful words. <br /><br />
In this project, I define an optimal solution as converting the most numbers in the string into letters. To get the optimal solution, I use dynamic programming to build up a matrix, in which each entry M[i,j] denotes the most numbers converted in a substring[i:] of the input string that includes converting the substring[i:j] into words. To get the largest number of number converted, we only need to find the maximum value in row 0 of the matrix. Then, we use traceback to trace back the optimal path and do the conversion during the meantime. <br /><br />
To determine whether a "word" is meaningful, I use [google-10000-words](https://github.com/first20hours/google-10000-english) github repo by first20hour and made some edition. The file is named "google-10000-english-edited.txt" in my repo. In the implementation, I have a function that generates all combinations of letters represented by a given number string, and filter out the those that are not in the dictionary.<br />


## Two files
The solution to two files challenge is the pdf file "two files". There is no coding assignment to this challenge so I include my answers to all the three questions in a pdf file.
