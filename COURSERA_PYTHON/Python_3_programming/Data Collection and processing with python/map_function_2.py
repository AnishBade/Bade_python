abbrevs=['usa','esp','chn','jpn','mex','can','rus','rsa','jam']
def cpt(lst):
    capitalized_list=map(lambda value:value.upper(),lst)
    return capitalized_list
capitalized_list=cpt(abbrevs)
print(capitalized_list)