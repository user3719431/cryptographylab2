import csv
from math import log2
def f_filter(file, alphabet):
    file.seek(0)
    fname = ("f(s)_" + file.name) if (" " in alphabet) else ("f_" + file.name)
    ffile = open(fname, "w", encoding="utf")
    c_prev = None
    while True:
        c = file.read(1).lower()
        if c_prev == c == " ":
            continue
        if c in alphabet or c == "ё":
            if c == "ё":
                ffile.write("е")
            else:
                ffile.write(c)
            c_prev = c
        if not c:
            break
    ffile.close()
    ffile = open(fname, "r+", encoding="utf")
    return ffile

def count_single(file, alphabet, notfile):
    single_array=[0]*len(alphabet)
    if notfile:
        for c in file:
            single_array[alphabet.index(c)]+=1
    else:
        file.seek(0)
        while True:
            c = file.read(1)
            if not c:
                break
            single_array[alphabet.index(c)]+=1
    single_array.append(alphabet)
    return single_array

def count_double(file, alphabet):
    file.seek(0)
    double_array1=[0]*(len(alphabet)*len(alphabet))
    while True:
        b = file.read(2)
        if not b or len(b)!=2:
            break
        index = alphabet.index(b[0])*len(alphabet)+alphabet.index(b[1])
        double_array1[index]+=1
    double_array1.append(alphabet)
#####################
    file.seek(2)
    double_array2=list(double_array1)
    while True:
        b = file.read(2)
        if not b or len(b)!=2:
            break
        index = alphabet.index(b[0])*len(alphabet)+alphabet.index(b[1])
        double_array2[index]+=1
    return double_array2, double_array1

def generatecsv(datalist):
    k=0
    for dataset in datalist:
        alphabet = dataset[-1]
        m = len(alphabet)
        with open(str(k)+".csv","w",encoding="utf", newline='') as fp:
            fp.write('\ufeff')
            c_writer = csv.writer(fp, delimiter=";")
            if len(dataset)<100:
                c_writer.writerows(list(zip(alphabet, dataset[:-1])))
            else:
                c_writer.writerow([""] + list(alphabet))
                rows_num = (len(dataset)-1)//m
                for i in range(rows_num):
                    c_writer.writerow(list(alphabet[i]) + dataset[m*i:m*(i+1)])
        k+=1
def printentropy(datalist):
    for dataset in datalist:
        entropy = 0
        m = len(dataset)-1
        n = sum(dataset[:-1])
        for i in range(m):
            if dataset[i]!=0:
                entropy = entropy - (dataset[i]/n)*log2((dataset[i]/n))
        if len(dataset)>100:
            entropy=entropy/2
        print(entropy)