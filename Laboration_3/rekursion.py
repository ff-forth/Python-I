def pascal(num):
    """Funtionen returnera en lista på nivån av n
    parameter : int
    returvärde : list
    """
    if num == 0:
        return [1]

    return_list = [1]
    last_list = pascal(num-1)
    num_index = len(last_list)-1
    for index in range(num_index):
        return_list.append(last_list[index]+last_list[index+1])
    return_list += [1]
    return(return_list)

print(pascal(2))