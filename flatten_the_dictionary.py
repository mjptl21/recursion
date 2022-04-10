def make_it_flat(dicti, key_name, ans):

    for key in dicti.keys():
        if isinstance(dicti[key], dict):
            make_it_flat(dicti[key], key_name + "_" +
                         key if key_name else key, ans)

        else:

            ans.append([key_name + "_" + key, dicti[key]])

            print(key_name)


ini_dict_1 = {'hi': {'hi2': {'hi3': 7}},
              'hello': {'hello2': {'hello3': 3}},
              'bye': {'bye2': {'bye2.1': 1, 'bye2.2': 4}}}

ans = []
make_it_flat(ini_dict_1, "", ans)

final_ans = {}

for i in ans:
    final_ans[i[0]] = i[1]


print(final_ans)
