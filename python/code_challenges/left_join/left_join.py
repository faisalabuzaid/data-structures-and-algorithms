# from code_challenges.hashtable.hashtable import HashMap, LinkedList

# def left_join(d1, d2):
#     result = []
#     for i in range(d1.size):
#         if d1.contains(d2.buckets[i]):
#             result.append(d1.buckets[i]+d2.buckets[i][1])

def left_join(d1,d2):

    output = []
    for key in d1.keys():
        if key in d2.keys():
            output.append([key,d1[key],d2[key]])
        else:
            output.append([key,d1[key],'NULL'])
    return output

if __name__ == "__main__":
    # table1 = HashMap
    # table1.add("faisal", 1)
    # table1.add('lara','ahmad')
    # table1.add('sara','ahmad')
    # table2 = HashMap
    # table1.add('faisal','abuzaid')
    # table1.add('lara','abuzaid')
    # table1.add('sara','abuzaid')
    # left_join(table1, table2)
    d1 = {'fond':'enamored','wrath':'anger','diligent':'employed','outfit':'garb','guide':'usher','hello':'everyone'}
    d2 = {'fond':'averse','wrath':'delight','diligent':'idle','guide':'follow','flow':'jam'}
    print(left_join(d1,d2))