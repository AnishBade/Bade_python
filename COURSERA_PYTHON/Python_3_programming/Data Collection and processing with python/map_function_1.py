def triple(value):
    return 3*value


def triple_stuff(a_list):
    new_list= map(triple,a_list)
    return new_list


def quadruple(a_list):
    new_list=map(lambda value:4*value,a_list)
    return new_list
lst=[2,5,9]
lst_3=triple_stuff(lst)
print(lst_3)
lst_4=quadruple(lst)
print(lst_4)
