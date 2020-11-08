def age_assignment(*args,**kwargs):
    dict={}
    for value in args:
        name=value
        dict[name]=""
    for value in kwargs:
        age=kwargs[value]
        for key in dict.keys():
            if key[0:1]==value:
                dict[key]=age
    return dict
