# จงเขียนโปรแกรมเพื่อทำการคำนวณเกรดโดยมีเงื่อนไขดังนี้

# คะแนน 80 - 100 ได้ A
# คะแนน 75 - 79 ได้ B+
# คะแนน 70 - 74 ได้ B
# คะแนน 65 - 69 ได้ C+
# คะแนน 60 - 64 ได้ C
# คะแนน 55 - 59 ได้ D+
# คะแนน 50 - 54 ได้ D
# คะแนน 0 - 49 ได้ F

# และให้แสดงผลตามตัวอย่างด้านล่าง

# Enter your score: 49
# grade:  F

score = 49

if score >= 80 and score < 101:
    print("grade:  A")
elif score >= 75 and score < 80:
    print("grade:  B+")
elif score >= 70 and score <= 74:
    print("grade:  B")
elif score >= 65 and score <= 69:
    print("grade:  C+")
elif score >= 60 and score <= 74:
    print("grade:  C")
elif score >= 55 and score <= 59:
    print("grade:  D+")
elif score >= 50 and score <= 54:
    print("grade:  D")
else:
    print("grade:  F")
