def flip_your_hat(caplist):
    keep_hat = caplist[0]
    tmp = caplist + [keep_hat]
    n = len(tmp)
    counter = 1
    while counter < n:
        if tmp[counter] != keep_hat:
            for index in range(counter+1, n):
                if tmp[index] == keep_hat:
                    end = index - 1
                    print('People in position', counter, 'through', end,'flip your hat')
                    break
                    
            if end <= counter:
                end = counter
                print('People in position',counter, 'flip your hat')

            counter = end + 1
        else:
            counter += 1 

def flip_your_hat_skip_empty(caplist, skip_hat = 'H'):
    keep_hat = caplist[0]
    tmp = caplist + [keep_hat]
    n = len(tmp)
    counter = 1
    while counter < n:
        if tmp[counter] != keep_hat and tmp[counter] != skip_hat:
            for index in range(counter+1, n):
                if tmp[index] == keep_hat or tmp[index] == skip_hat:
                    begin = counter
                    end = index - 1
                    break
                    
            if end <= counter:
                end = counter
                print('People in position',begin, 'flip your hat')
            else:
                print('People in position', begin, 'through', end,'flip your hat')

            counter = end + 1
        else:
            counter += 1


if __name__ == "__main__":
    cap1 = ['F', 'F', 'B', 'B', 'B', 'F', 'B',
            'B', 'B', 'F', 'F', 'B', 'F']
    cap2 = ['F', 'F', 'B', 'B', 'H', 'B', 'F', 'B',
            'B', 'B', 'F', 'F', 'F', 'F']
    
    flip_your_hat(cap1)
    flip_your_hat_skip_empty(cap2)

    