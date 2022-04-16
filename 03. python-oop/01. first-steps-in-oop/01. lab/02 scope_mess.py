x = "global"

def outer():
    x = "local"

    def inner():
# The nonlocal statement causes the listed identifiers to refer to 
# previously bound variables in the nearest enclosing scope.
# https://docs.python.org/release/3.1.3/reference/simple_stmts.html#nonlocal
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        global x
        x = "global: changed!"

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()

print(x)
outer()
print(x)