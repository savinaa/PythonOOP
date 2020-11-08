def get_info(**kwargs):
    name=kwargs['name']
    age=kwargs['age']
    town=kwargs['town']
    return f'This is {name} from {town} and he is {age} years old'