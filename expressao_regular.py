import re

'''
4
4.0O0
-1.00
+4.54
SomeRandomStuff
'''
n=int(input())
for i in range(0,n):
    expressao = input()
    resultado = re.compile('\A[+-]*[0-9]\.[0-9]+[^A-Z]')
    if resultado.match(expressao) == None:
        print("False")
    else:
            print("True")
