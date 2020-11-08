def func_executor(*args):
    results=[]
    for function in args:
        func,arguments=function
        results.append(func(*arguments))
    return results
