def convert_to_binary(i):
    res = []
    quot, rem = divmod(i, 2)
    res.append(str(rem))
    while quot != 0:
        quot, rem = divmod(quot, 2)
        res.append(str(rem))
    res.reverse()
    return ''.join(res)


def query_string(S, N):
    for i in range(1, N + 1):
        if convert_to_binary(i) not in S:
            return False
    return True


S_1 = "100011110111101001001111111010111011000101000100011001000000000000001101000001111001000010011111110101100000101000100011100111100101000000010111011001000111011011010101011101010111011000100010001011001011110101010011000101000100101010110111110001101100001110011001110001111010100111000001101101110011"
N_1 = 15
query_string(S_1, N_1)
