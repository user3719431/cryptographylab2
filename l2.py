import l1
from math import isclose
def encrypt(file, key, alphabet):
    file.seek(0)
    fname = file.name[:file.name.index(".")] + "(" + key + ")" + ".txt"
    with open(fname, "w", encoding="utf") as f:
        i=0
        while(True):
            c = file.read(1)
            if not c:
                break
            f.write( alphabet[ (alphabet.index(c) + alphabet.index(key[i%len(key)]) ) % len(alphabet) ] )
            i+=1
    return fname
def c_index(fname,alphabet, notfile):
    c = 0
    counts = 0
    if notfile:
        counts = l1.count_single(fname,alphabet, True)
    else: 
        with open(fname, "r", encoding="utf") as f:
            counts = l1.count_single(f, alphabet, False)
    n = sum(counts[:-1])
    for i in range(len(counts)-1):
        c+=1/(n*(n-1))*counts[i]*(counts[i]-1)
    return c
def split_to_chunks(fname, r):
    chunks=[]
    with open(fname, "r", encoding="utf") as f:
        text = f.read()
    for i in range(r):
        chunk=''
        for k in range(i, len(text), r):
            chunk+=text[k]
        chunks.append(chunk)
    return chunks
    pass
def find_r(fname,alphabet):
    n = len(alphabet)
    ci_list = [0.044864109973961945, 0.0409499892735005,0.03322102057384669]
    given_ci = c_index(fname, alphabet, False)
    possible_r = ci_list.index( min(ci_list, key=lambda x:abs(x-given_ci)) ) 
    if abs((ci_list[possible_r] - given_ci)) < 0.0001:
        return possible_r+2
    else:
        for r in range(5,31):
            text = split_to_chunks(fname, r)
            chunks_ci = []
            for chunk in text:
                chunks_ci.append(c_index(chunk,alphabet,True))
            print(r, chunks_ci, sep="\n")
            if isclose( sum(chunks_ci)/r, 1/n, abs_tol=0.02):
                continue
            else:
                return r
def calc_M(text, pr, alphabet):
    M = []
    N = l1.count_single(text, alphabet, True)[:-1]
    for g in range(len(alphabet)):
        M_g = 0
        for t in range(len(alphabet)):
            M_g += pr[t] * N[(t+g)%len(alphabet)]
        M.append(M_g)
    return M
def find_key(fname, alphabet, r):
    k1 = r*[0]
    k2 = r*[0]
    text = split_to_chunks(fname, r)
    i=0
    distribution = [0.08139674995198061, 0.016868228818078677, 0.0479287237101275, 0.017913321713236532, 0.031437491872493895, 0.0845713985752855, 0.009169616429432965, 0.017696190540954875, 0.07104961447286635, 0.01198039138490318, 0.0339571678936964, 0.046745239518350565, 0.030992492272158414, 0.06539823885144767, 0.1111818974639795, 0.027558956481902354, 0.04598289435852652, 0.0530396574576803, 0.05644575359429637, 0.027280980860245073, 0.001366017539903818, 0.00987231016830052, 0.003383428596652601, 0.014189880017131888, 0.009467873534215458, 0.004020505772468006, 0.00032569675842248236, 0.02009775674866351, 0.01798967553206085, 0.002791686500764135, 0.007377687743899747, 0.02052247486587378]
    for chunk in text:
        counts = l1.count_single(chunk, alphabet, True)[:-1]
        
        most_frequent = counts.index(max(counts))
        k1[i] = alphabet[(most_frequent - 14)%len(alphabet)]
        
        M = calc_M(chunk, distribution, alphabet)
        k2[i] = alphabet[M.index(max(M))]
        i+=1
    key1=''.join(k1)
    key2=''.join(k2)
    print(key1, key2, sep="\n")
    return key2
def decrypt(file, key, alphabet):
    fname = file.name[:file.name.index(".")] + "(decrypted)" + ".txt"
    with open(fname, "w", encoding="utf") as f:
        i=0
        while(True):
            c = file.read(1)
            if not c:
                break
            f.write( alphabet[ (alphabet.index(c) - alphabet.index(key[i%len(key)]) ) % len(alphabet) ] )
            i+=1