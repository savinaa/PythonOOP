import operator as o,functools
def operate(operator,*args):
    return  {
        "+":functools.reduce(lambda a,b:o.add(a,b),args),
        "-":functools.reduce(lambda a,b:o.sub(a,b),args),
        "*":functools.reduce(lambda a,b:o.mul(a,b),args),
        "/":functools.reduce(lambda a,b:o.truediv(a,b),args),
    }[operator]