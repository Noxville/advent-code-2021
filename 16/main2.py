from functools import reduce


def hex_to_bin(hx):
    return "".join([
        {'0': '0000',
         '1': '0001',
         '2': '0010',
         '3': '0011',
         '4': '0100',
         '5': '0101',
         '6': '0110',
         '7': '0111',
         '8': '1000',
         '9': '1001',
         'A': '1010',
         'B': '1011',
         'C': '1100',
         'D': '1101',
         'E': '1110',
         'F': '1111',
         }[c] for c in hx])


def chomp_int(s, n_bits):
    print(f"chomping {s[:n_bits]}")
    return int(s[:n_bits], 2), s[n_bits:]


def chunks(s, n):
    return [s[(_*n) : (_+1)*n] for _ in range(len(s) // n)]


def calc(op_id, vals):
    if op_id == 0:
        return sum(vals)
    elif op_id == 1:
        return reduce(lambda x, y: x * y, vals, 1)
    elif op_id == 2:
        return min(vals)
    elif op_id == 3:
        return max(vals)
    elif op_id == 5:
        return int(vals[0] > vals[1])
    elif op_id == 6:
        return int(vals[0] < vals[1])
    elif op_id == 7:
        return int(vals[0] == vals[1])


def parse(stream):
    print(f"raw = {stream}")
    if 0 == len(stream):
        return
    if '1' not in stream:
        return
    ver, stream = chomp_int(stream, 3)
    print(f"version = {ver}")
    p_type, stream = chomp_int(stream, 3)
    print(f"Packet type = {p_type}")

    if 4 == p_type:
        pointer_len, num_bin, num = 0, '', None
        for chunk in chunks(stream, 5):
            pointer_len += 5
            num_bin += chunk[1:]
            if '0' == chunk[0]:
                print(f"Number is {int(num_bin, 2)}")
                num = int(num_bin, 2)
                break
        yield num
        yield from parse(stream[pointer_len:])
    else:
        type_len, stream = chomp_int(stream, 1)
        print(f"Length type = {type_len}")
        if 0 == type_len:
            length_packet, stream = chomp_int(stream, 15)
            print(f"Length of packets = {length_packet}")
            vals = list(parse(stream[:length_packet]))
            print(f"VAAALS: {vals}")
            yield calc(p_type, vals)
            yield from parse(stream[length_packet:])
        elif 1 == type_len:
            num_packets, stream = chomp_int(stream, 11)
            print(f"# of packets = {num_packets}")
            vals = list(parse(stream))  # decode entire stream - might be too much
            yield calc(p_type, vals[:num_packets])
            yield from vals[num_packets:]
        else:
            print("Something is fucked")

#     *
#    /  \
#   *    *
#  /  \
# *    *

with open('case1.txt') as fin:
    lines = [hex_to_bin(line.strip()) for line in fin.readlines()]
    for line in lines:
        vers = [_ for _ in parse(line)]
        print(f"-> {vers}")
        print("~~~~~~")
