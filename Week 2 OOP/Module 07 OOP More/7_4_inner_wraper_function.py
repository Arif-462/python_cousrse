
#function is first class object
def Double_decker():

    print('starting the double decker')
    def inner_func():
        print('inside the inner function')
        return 300
    return inner_func   


# print(Double_decker())
print(Double_decker()())

def do_something(work):
    print('work started')
    # print(work)
    work()
    print('work ende')

# do_something(2)
# do_something('ami busy')

def coding():
    print('codin in python')

# do_something(coding)
def sleeping():
    print('sleeping and dreaming in python')

do_something(sleeping)



