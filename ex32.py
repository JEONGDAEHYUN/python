# 4-1 36p
# f = open("C:\python\새파일.txt",'w')
# for i in range(1,11):
#     data = "%d번째 줄입니다.\n"%i
#     f.write(data)
# f.close()


# 4-1 37p
# f = open("C:\python\새파일.txt",'r')
# line = f.readline()
# print(line)
# f.close()

# 4-1 38p
# f = open("C:\python\새파일.txt",'r')
# line = f.readline()
# print(line)
# f.close()

f = open("C:\python\새파일.txt", 'a')
for i in range(11,20):
    data = "%d번째 줄입니다.\n"%i
    f.write(data)
f.close()