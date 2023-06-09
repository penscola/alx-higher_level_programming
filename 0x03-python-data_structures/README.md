## Resources
### Read or watch:

* [3.1.3. Lists](https://intranet.alxswe.com/rltoken/VarQbHxfmbnpGnaGp3Nb_A)
* [Data structures](https://intranet.alxswe.com/rltoken/2aa8Mp-V2eSieGeX3OX8yQ)
* [Learn to Program 6 : Lists](https://intranet.alxswe.com/rltoken/BX2_CuHj1sq4eYGiXbCYSg)

### Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### Function Prototypes :floppy_disk:

Prototypes for functions written in this project:

| File                               | Prototype                                      |
| ---------------------------------- | ---------------------------------------------- |
| `0-print_list_integer.py`          | `def print_list_integer(my_list=[]):`          |
| `1-element_at.py`                  | `def element_at(my_list, idx):`                |
| `2-replace_in_list.py`             | `def replace_in_list(my_list, idx, element):`  |
| `3-print_reversed_list_integer.py` | `def print_reversed_list_integer(my_list=[]):` |
| `4-new_in_list.py`                 | `def new_in_list(my_list, idx, element):`      |
| `5-no_c.py`                        | `def no_c(my_string):`                         |
| `6-print_matrix_integer.py`        | `def print_matrix_integer(matrix=[[]]):`       |
| `7-add_tuple.py`                   | `def add_tuple(tuple_a=(), tuple_b=()):`       |
| `8-multiple_returns.py`            | `def multiple_returns(sentence):`              |
| `9-max_integer.py`                 | `def max_integer(my_list=[]):`                 |
| `10-divisible_by_2.py`             | `def divisible_by_2(my_list=[]):`              |
| `11-delete_at.py`                  | `def delete_at(my_list=[], idx=0):`            |
| `100-print_python_list_info.c`     | `void print_python_list_info(PyObject *p);`    |

### General
* Why Python programming is awesome
* What are lists and how to use them
* What are the differences and similarities between strings and lists
* What are the most common methods of lists and how to use them
* How to use lists as stacks and queues
* What are list comprehensions and how to use them
* What are tuples and how to use them
* When to use tuples versus lists
* What is a sequence
* What is tuple packing
* What is sequence unpacking
* What is the `del` statement and how to use it

### Requirements
#### Python Scripts
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly #`!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version `2.8.*`)
* All your files must be executable
* The length of your files will be tested using `wc`

#### C
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* Your code should use the `Betty` style. It will be checked using betty-style.pl and betty-doc.pl
* You are not allowed to use global variables
* No more than 5 functions per file
* In the following examples, the `main.c` files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own `main.c` files at compilation. Our `main.c `files might be different from the one shown in the examples
* The prototypes of all your functions should be included in your header file called `lists.h`
* Don’t forget to push your header file
All your header files should be include guarded