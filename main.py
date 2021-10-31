class Stack:

    def __init__(self):
        self.object = []

    def isEmpty(self):
        if self.object.size() == 0:
            return True
        else:
            return False

    def push(self, x):
        self.object.insert(0, x)

    def pop(self):
        return self.object.pop(0)

    def peek(self):
        return self.object[0]

    def size(self):
        return len(self.object)


def balanced_sequence_of_brackets(s: str):
    brackets_dict = {"(": ")", "{": "}", "[": "]"}
    closing_brackets = (")", "}", "]")
    s_tuple = tuple(i for i in s if i in brackets_dict or i in closing_brackets)
    if s_tuple[0] in closing_brackets or len(s_tuple) % 2 != 0:
        return False
    stack = Stack()
    for i in s_tuple:
        if i in brackets_dict:
            stack.push(i)
        elif i in closing_brackets and i != brackets_dict[stack.peek()]:
            return False
        else:
            stack.pop()
    if stack.size() == 0:
        return True
    else:
        return False


def main():
    s = input('Введите строку состоящую из скобок: "(", ")", "{", "}", "[", "]"')
    if balanced_sequence_of_brackets(s):
        print('Cбалансированная последовательность скобок')
    else:
        print('Не сбалансированная последовательность скобок')


if __name__ == '__main__':
    main()
