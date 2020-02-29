def myfun(**my):
    for my,name in my.items():
        my,name=name,my
        print("%s==%s"%(my,name))



myfun(first="Mohamed",middle="kalanthar",last="hussain")


def myFun(arg1, **kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

    # Driver code


myFun("Hi", first='Geeks', mid='for', last='Geeks')  