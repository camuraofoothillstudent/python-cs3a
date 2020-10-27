"""
    Assignment Five: Reversing a List with Recursion
    Submitted by Christopher Amurao
"""

from string import ascii_lowercase


def reverse_a_list(my_list):
    print(len(my_list))
    length = len(my_list)
    if length == 0:
        return []
    else:
        ret_value = reverse_a_list(my_list[1:]) + [my_list[0]]
    return ret_value


def main():
    alphabet = [char for char in ascii_lowercase]
    print(alphabet)
    print(reverse_a_list(alphabet))
    print(alphabet)


if __name__ == "__main__":
    main()

"""
/Users/camurao/PycharmProjects/CS3A/venv/bin/python /Users/camurao/PycharmProjects/CS3A/Assignment5.py
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
26
25
24
23
22
21
20
19
18
17
16
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
0
['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

Process finished with exit code 0


"""
