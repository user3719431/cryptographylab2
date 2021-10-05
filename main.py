import l1
import l2
alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
ffile = None
###### 1,2
with open("stihi.txt", "r", encoding="utf") as f:
    ffile = l1.f_filter(f, alphabet)
    print(
        "2\t"+ str(l2.c_index(l2.encrypt(ffile,"оп",alphabet), alphabet, False)), 
        "3\t"+ str(l2.c_index(l2.encrypt(ffile,"сим",alphabet), alphabet, False)),
        "4\t"+ str(l2.c_index(l2.encrypt(ffile,"хлеб",alphabet), alphabet, False)),
        "5\t"+ str(l2.c_index(l2.encrypt(ffile,"крупа",alphabet),alphabet, False)),
        "10\t"+str(l2.c_index(l2.encrypt(ffile,"сухофрукты",alphabet),alphabet, False)),    #10
        "20\t"+str(l2.c_index(l2.encrypt(ffile,"сухофруктыкрупасимоп",alphabet),alphabet, False)),              #20
        sep = "\n"
        )
with open("doktor-zhivago.txt", "r", encoding="utf") as f:
    ffile = l1.f_filter(f, alphabet)
print(l2.c_index("f_doktor-zhivago.txt", alphabet, False))
###### 3
r = l2.find_r("1.txt", alphabet)
print(r)
key = l2.find_key("1.txt", alphabet, r)
with open("1.txt", "r", encoding="utf") as f:
    l2.decrypt(f, key, alphabet)
