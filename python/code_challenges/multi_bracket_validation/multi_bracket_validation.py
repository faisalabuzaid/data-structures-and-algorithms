

open_list = ["[","{","("]
close_list = ["]","}",")"]

def brackets_validation(input_string):
    test = []
    for i in input_string:
        if i in open_list:
            test.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(test) > 0) and
                (open_list[pos] == test[len(test)-1])):
                test.pop()
            else:
                return False
    if len(test) == 0:
        return True
    else:
        return False

    # normal = Queue()
    # square = Queue()
    # curly = Queue()

    # my_list = [char for char in (input_string)]

    # for ele in my_list:

    #     if ele == "{":
    #         print("curlu in")
    #         curly.enqueue('{')
    #     if ele == "(":
    #         print("normal in")
    #         normal.enqueue('(')
    #     if ele == "[":
    #         print("square in")
    #         square.enqueue('[')

    #     if ele == "}":
    #         if not curly.front:
    #             return False
    #         else:
    #             print("curly out")
    #             curly.dequeue()
    #     if ele == ")":
    #         if not normal.front:
    #             return False
    #         else:
    #             print("normal out")
    #             normal.dequeue()
    #     if ele == "]":
    #         if not square.front:
    #             return False
    #         else:
    #             print("square out")
    #             square.dequeue()
    # if not curly.front and not normal.front and not square.front:
    #     return True
    # else:
    #     return False

