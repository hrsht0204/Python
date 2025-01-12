list = [5, 10,6 , 2, 1, 7, 8,0,9]

search = int(input("Search for : "))
index = 0

while index < len(list):
    
    if list[index] == search:
        print("Founded" , search ,"on index no" , index)
        break 
    elif search not in  list:
        print("Not founded")
        break
    else:
        index += 1
        
    