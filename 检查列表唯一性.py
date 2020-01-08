def unique(l):
    if len(l)==len(set(l)):
        print("All elements are unique")
    else:
        print("List has duplicates")
unique([1,2,3,4])
unique([1,1,2,3])