def blackhole(a):
    
    import inflect
    x=inflect.engine()
    y = a
    b = len(y)
    print()
    while b!=4:
        c = x.number_to_words(b)
        b = len(c)
        print("In",y,"number of character : ",c)
        y = c
        print()

    print("In",c,"number of character : FOUR")
    print()
    print("Blackhole 4 [ FOUR ] is come again.")



a = str(input("Enter a word : "))
blackhole(a)