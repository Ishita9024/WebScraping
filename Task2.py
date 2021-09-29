from Task1 import*
import json
def group_by_year(my_function):
    year_list=[]
    for i in my_function:
        year=i['movie_year']
        if year not in year_list:
            year_list.append(year)
        year_list.sort()
    movie_dic={i:[]for i in year_list}
    for i in my_function:
        year=i['movie_year']
        for j in movie_dic:
            if j==year:
                movie_dic[j].append(i)
    with open("Task2_data.json","w") as f:
        json.dump(movie_dic,f,indent=4)   
    return movie_dic
data1=group_by_year(data)


