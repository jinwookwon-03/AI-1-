#lab 8-1 / 1

a = [10, 20, 30]
a[3]
print(a)

n = int('20%')
print(n)

a = 100 + '200'
print(a)

#lab 8-1 / 2
try :
    a = [10, 20, 30]
    a[3]
except Exception as e:
    print(e)

try :
    n = int('20%')
    print(n)
except Exception as e:
    print(e)

try :
    a = 100 + '200'
    print(a)
except Exception as e:
    print(e)
