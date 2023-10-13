#!/usr/bin/python3

"""This module has a function that that prints a text with 2
    new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """That prints a text with 2 new
    lines after each of these characters: .,:

    Arguments:
        text (str) -- text

    Raises:
        TypeError: text must be a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    aux = "."
    for i in text.strip():
        if i == " " and aux in ".:?":
            continue
        print(i, end="")
        aux = i
        if i in ".:?":
            print("\n")
