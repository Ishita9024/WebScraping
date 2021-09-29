from Task2 import*
import json
def group_by_decade(my_function):
    list=[]
    for i in my_function:
        dec=i%10
        mod=i-dec
        if mod not in list:
            list.append(mod)
    dic={i:[]for i in list}
    for i in list:
        decade=i+9
        for j in my_function:
            if j<=decade and j>=i:
                for l in my_function[j]:
                    dic[i].append(l)
                with open("Task3_data.json","w") as file:
                    json.dump(dic,file,indent=4)
    return dic
data2=group_by_decade(data1)