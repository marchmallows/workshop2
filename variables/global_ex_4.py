x = "awesome"


def myfunc():
    global x
    print("Python is" + x)
    # print awesome
    x = "fantastic"
    # x gobal = fantastic


myfunc()
print(" Python is " + x)

# output : Pyton in awesome
# Output : Python is fantastic