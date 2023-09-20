#encapsultion
# def Outer_func():
#     def inner_func():
#         print('I am inner function')
#     return inner_func

# Outer_func()


#2 reuse
# def increment(num):
#     def inner_incre():
#         return num+1
#     return inner_incre

# print(increment(10)())

def on_click(handler):
    onc_click_handler = handler
    