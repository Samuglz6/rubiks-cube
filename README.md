# rubiks-cube

## Introduction

_Project for the Intelligent Systems' subject, at Escuela Superior de Informatica in the UCLM University_.

This project consists on solving a rubik's cube applying searching algorithms and strategies.


## System requirements

In order to be able to execute the program you should have installed on your computer _Python3_.

Also some packages are going to be used by the program. Take into account that
some of them have to be installed in order to be able to use them.
The following packages are used by the program:

1. [json](https://docs.python.org/3/library/json.html)
2. [hashlib](https://docs.python.org/3/library/hashlib.html?highlight=hashlib#module-hashlib)
3. [os](https://docs.python.org/3/library/os.html?highlight=os#module-os)
4. [sys](https://docs.python.org/3/library/sys.html?highlight=sys#module-sys)
5. [numpy](https://numpy.org/)
6. [copy](https://docs.python.org/3/library/copy.html?highlight=copy#module-copy)
7. [sortedcontainers](http://www.grantjenks.com/docs/sortedcontainers/)


### How to install _Python3_

Installing _Python3_ in Ubuntu it's an easy task:

`$ sudo apt-get update`

`$ sudo apt-get install python3.6`


### How to install packages

#Sortedcontainers

`$ sudo pip install sortedcontainer `

#### Numpy

`$ sudo pip install numpy `




## Executing the program

Now we are going to execute the program.
To do that we have to be either in the project folder (_rubiks-cube_) or the source code folder (_rubiks-cube/src_).

In both cases we are going to execute the _Main.py_ file that is in the *src* folder.

For the first one the execution will be as follows:

`$ python3 ./src/Main.py`

For the second option, will be like this:

`$ python3 Main.py`

*Any other way of executing the program could lead to problems in the project resources management.*

Now you just have to follow the instructions given by the program:
1. Select the json of the cube to be used in the program
2. Select the searching strategy to find the solution
3. Choose if you want to use pruning or not
4. Wait for the solution
5. You can consult the solution of the cube in the project's folder _output_:
_solution.json_ shows the final result of the cube; solution.txt has the information
of the path to reach the solution.
