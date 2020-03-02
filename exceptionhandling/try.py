try:
    print("Hello")
    i = 5/2
    if i!=2:
       raise ValueError("This is Not 2")
except (ValueError,AssertionError,DeprecationWarning,ZeroDivisionError) as e:
    print(e)
finally:
    print("Hello 2")