def runlength_encoder(strings):
    encoder = ''
    n = len(strings)
    index = 0
    while index < n:
        alphabet = strings[index]
        count = 0
        for i in range(index + 1, n):
            count += 1
            if strings[i] != alphabet:
                encoder += str(count) + alphabet
                index = i
                break
            elif i >= n - 1:
                count += 1
                encoder += str(count) + alphabet
                index = n
                break
        if index == n - 1:
            encoder += str(1) + strings[index]
            break
            
    return encoder

def runlength_decoder(encoded_strings):
    import re
    n = len(encoded_strings)
    count = 0
    decoder = ''
    while count < n:
        tmp = encoded_strings[count:]
        number = re.findall(r'[1-9]+',tmp)[0]
        count += len(number) + 1
        decoder += tmp[len(number)] * int(number)
    
    return decoder