#sort by value in a dictionary
dicti={'a':10,'y':2,'b':5}
list=[]
final_list=[]
final_dict_form=dict()
for k,v in dicti.items():

    list.append((v,k))
sorted_list=sorted(list)
print(sorted_list)
for v,k in sorted_list:
    final_list.append((k,v))
    final_dict_form[k]=v
print(final_list)
print(final_dict_form)
