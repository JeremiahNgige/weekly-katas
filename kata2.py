'''
    a function that takes in an input and return an array of its characters 
    then progressively pairs them into tuples through the first character to the last
    If the list length is even then the pairing is achieved  and if its odd then the 
    array is not paired
'''
def main():
    x = str(input("Enter a list of any numbers:"))
    
    seperator = " "
    y = seperator.join(x)
        
    arr =  list(y.split(" "))
    print(arr)
    if (len(arr) % 2) == 0:
        pairs = zip(arr[::2], arr[1::2])
        u = list(pairs)    
        print(u)   
    else:
        print('array lenth is an odd number')
        
        
        
if __name__ == '__main__':
    main()