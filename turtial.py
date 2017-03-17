# # def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
# #   while True:
# #     ok = input(prompt)
# #     if ok in ('y', 'yes'):
# #       return True
# #     if ok in ('n', 'no'):
# #       return False
# #     retries = retries - 1
# #     if retries < 0:
# #       raise IOError('refused user')
# #     print(complaint)
#
# # ask_ok('Do you really want to quit?')
#
# # def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
# #     while True:
# #         ok = input(prompt)
# #         if ok in ('y', 'ye', 'yes'):
# #             return True
# #         if ok in ('n', 'no', 'nop', 'nope'):
# #             return False
# #         retries = retries - 1
# #         if retries < 0:
# #             raise IOError('refusenik user')
# #         print(complaint)
#
# # ask_ok('Do you really want to quit?', 2)
#
# def scope_test():
#     def do_local():
#         spam = "local spam"
#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlocal spam"
#     def do_global():
#         global spam
#         spam = "global spam"
#     spam = "test spam"
#     do_local()
#     print("after local", spam)
#     do_nonlocal()
#     print("after nonlocal", spam)
#     do_global()
#     print("after global", spam)
#
# scope_test()
# print("In global scope", spam)