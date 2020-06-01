lst=['witch','halloween','pumpkin','cat','candy','wagon','moon']
def filtered(lst):
    new_list=filter(lambda value:'o'in value,lst)
    return list(new_list)
lst_1=filtered(lst)
print(lst_1)