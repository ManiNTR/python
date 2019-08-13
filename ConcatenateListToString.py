#Python program to concatenate all elements in a list into a string and return it
def Concatenate_list_element(list1):
    result=""
    for elements in list1:
        result=result+str(elements)
    return result
print(Concatenate_list_element([2,5,4,3,6,7]))
