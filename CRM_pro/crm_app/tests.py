class see():
    def fun(self, a):
        x = list(a)
        for i in x:
            a = ord(i)
            if a >= 97 and a <= 122:
                k = 219 - a
                print(chr(k), end='')
            elif a >= 65 and a <= 90:
                k = 155 - a
                print(chr(k), end='')
            else:
                print('This is not an alphabate')


#     def fun(self,a, b):
#         print(a, b)
# # see().fun(10)
# see().fun(10,20)
see().fun('ashok')