# 1.จงเขียนตารางสูตรคูณให้ผลลัพท์ที่ออกมาเป็นแบบตัวอย่างด้านล่างโดยใช้คำสั่ง while
# 2.จงเขียนตารางสูตรคูณให้ผลลัพท์ที่ออกมาเป็นแบบตัวอย่างด้านล่างโดยใช้คำสั่ง for

i = 2
a = 1

while i < 13:
    print(i)
    a = 1
    while a < 13:
        print(i, "*", a, "=", i * a)
        a += 1
    i += 1


for i in range(13):
    if i == 0:
        continue
    elif i == 1:
        continue
    print(i)
    a = 1
    for a in range(13):
        print(i, "*", a, "=", i * a)
        a += 1
    i += 1