def get_list(stri):
    if stri == "":
        return [[]]

    
    ss = get_list(stri[1:])
    fs = get_list(stri[1:])

    for i in fs:
        i.insert(0, stri[0])

    return fs + ss

print(get_list("ab"))
