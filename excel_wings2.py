import xlwings as xw

@xw.func
def hello(name):
    return f"Hello, {name}!"
