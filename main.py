# 1
h = input("Hujjt topshirish: ")
s = input("Suhbatdan otish: ")
t = input("Test sinovdaan otish: ")

if h == "yoq":
    print("Aval hujjat topshiring")
elif h == 'ha' and s == 'yoq':
    print("Suhbatdan otdinggizmi")
elif h == 'ha' and s == 'ha' and t == 'yoq':
    print("Test natijalari yetarli emas")
elif h == 'ha' and s == 'ha' and t == 'ha':
    print("Siz ishga qabul qilindingiz")

else:
    print("Jarayon davom etmoq da")

# 2
gap = input()

natija = ''.join(soz[0] for soz in gap.split())

print(natija)


# 3
roy = [4, 7, 2, 5, 1, 10]

natija = [son * indeks for indeks, son in enumerate(roy)]

print(natija)












