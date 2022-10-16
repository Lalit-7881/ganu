def new_decorators(func):

    def wrap_func():
        print("code here before ececuting func!")
        func()
        print("func() has been called")

    return wrap_func
def func_need_decorators():
    print("this function is in need of a decoration!")


#func_needs_decorators =  new_decorators(func_needs_decorators)
func_needs_decorators()


