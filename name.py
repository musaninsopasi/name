filename = "name.txt"


# Dosya açılır ve her satırı lines dizisine okunur.

with open(filename) as f:
    lines = f.readlines()

# İsim, soyisim ve yaş listeleri oluşturulur.
name_list = []
surname_list = []
age_list = []


# Her satır için kelimelere ayrılır ve uygun listelere eklenir.

for line in lines:
    elements = line.split()
    name_list.append(elements[0]) # 0 index  Name olarak geçiyor
    surname_list.append(elements[1]) # 1 index Surname olarak geçiyor
    age_list.append(elements[2]) # 2 index Age olarak geçiyor

# Verileri ekrana yazdırır
print(name_list, surname_list, age_list)