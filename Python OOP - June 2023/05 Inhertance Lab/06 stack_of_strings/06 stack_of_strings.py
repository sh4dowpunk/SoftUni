from typing import List


class Stack:
    def __init__(self):
        self.data: List[str] = []

    def push(self, element):
        """
        Adds an element to the end of the stack.
        :param element:
        :return: This method returns nothing.
        """
        self.data.append(element)

    def pop(self) -> str:
        """
        Removes and returns the last element of the stack.
        :return: The last element from the stack.
        """
        last_element = self.data.pop()
        return last_element

    def top(self) -> str:
        """
        Returns a reference to the topmost element of the stack.
        :return: The topmost element of the stack.
        """
        topmost_element = self.data[-1]
        return topmost_element

    def is_empty(self):
        """
        This method returns True or False.
        :return: Boolean
        """
        if not self.data:
            return True
        return False

    def __str__(self):
        return f"[{', '.join([el for el in self.data[::-1]])}]"


# my_stack = Stack()
# my_stack.push("Ivan")
# my_stack.push("Bogomil")
# my_stack.push("Radoslav")
#
# print(my_stack.pop())
# # print(my_stack.top())
# # print(my_stack.pop())
# # print(my_stack.pop())
# print(my_stack.is_empty())
#
# print(my_stack.__str__())

# Variant 2
# class Stack:
#     def __init__(self):
#         self.data = []
#
#     def push(self, value):
#         if not isinstance(value, str):
#             raise TypeError("Only strings can be appended to our stack!")
#         self.data.append(value)
#
#     def pop(self):
#         return self.data.pop()
#
#     def top(self):
#         return self.data[-1]
#
#     def is_empty(self):
#         return len(self.data) == 0
#
#     def __str__(self):
#         return f"[{', '.join([el for el in self.data[::-1]])}]"