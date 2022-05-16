def log_on_exception(*args, **kwargs):
    print("Inside decorator")
     
    def inner(func):
        try:
            func()
        except:
            print("Exception", ", ".join(list(args)))
    return inner
 
@log_on_exception('tag1', 'tag2')
def fn():
    raise Exception("Inside actual function")