#sort by keys in a dictionary
dicti={'a':10,'y':2,'b':5}
list=[]
final_list=[]
final_dict_form=dict()
for k,v in dicti.items():
    list.append((k,v))
sorted_list=sorted(list,reverse=True)
print(sorted_list)
for k,v in sorted_list:
    final_dict_form[k]=v

print(final_dict_form)
