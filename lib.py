def try_me(list1):
    sum=0
    for x in list1:
        sum+=x
    return sum

if __name__ == "__main__":
    # Le Wagon location
    list1=[1,2,3,4,5,6,7,8,9,9,5,6,7,8,9,0]
    #Insert your coordinates from google maps here
    #lat2, lon2 = x, y
    sommation = try_me(list1)
    print(sommation)
