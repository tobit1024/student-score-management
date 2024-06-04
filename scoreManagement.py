scoreDict = {}
ascScoreDict = {}
descScoreDict = {}
asc2020 = {}
asc2021 = {}
asc2022 = {}
asc2023 = {}
asc2024 = {}
A = {}
B = {}
C = {}
D = {}


def avg(file, num):
    file = dict(file)
    sum = 0
    for i in list(file.values()):
        sum += int(i[num])
    return str(sum / len(file))

def writeinfo(year, file):
    file = dict(file)
    
    bestScoreNum = -1
    worstScoreNum = 0
    bestScore = file[list(file)[bestScoreNum]][4]
    bestScoreNum -= 1
    while True:
        if bestScore == file[list(file)[bestScoreNum]][4]:
            bestScoreNum -= 1
        else:
            bestScoreNum += 1
            bestScoreNum = -bestScoreNum
            break
    worstScore = file[list(file)[worstScoreNum]][4]
    worstScoreNum += 1
    while True:
        if worstScore == file[list(file)[worstScoreNum]][4]:
            worstScoreNum += 1
        else:
            break
    with open("txt/"+str(year)+".txt","w",encoding="utf-8") as f:
        f.write("1등 : ")
        for i in range(bestScoreNum):
            f.write(file[list(file)[-i-1]][0])
            if i < bestScoreNum - 1:
                f.write(",")
            f.write(" ")
        f.write("("+str(bestScore)+"점)\n")
        f.write("꼴등 : ")
        for i in range(worstScoreNum):
            f.write(file[list(file)[i]][0])
            if i < worstScoreNum - 1:
                f.write(",")
            f.write(" ")
        f.write("("+str(worstScore)+"점) \n")
        f.write("웹 프로그래밍 평균 : " +avg(file,1)+"\n")
        f.write("파이썬 프로그래밍 평균 : "+avg(file,2)+"\n")
        f.write("알고리즘 평균 : " + avg(file,3)+"\n")
        
def writeData(files,data):
    data = dict(data)
    data = data.items()
    with open("txt/"+files+".txt","w",encoding="utf-8") as file:
        for id,value in data:
            file.write(id+"\t")
            for i in value:
                file.write(str(i)+"\t")
            file.write("\n")




with open("txt/data.txt","r",encoding="utf-8") as file:
    data = file.read().split("\n")
    k = 0
    for i in data:
        if i != "":
            j = i.split(" ")
            j.append(int(j[2])+int(j[3])+int(j[4]))
            scoreDict.update({j[0] : j[1:]})
            k += 1

ascScore = sorted(scoreDict.items(), key=lambda x : (x[1][4], x[0]))

stuNum = len(scoreDict)
i = 1
for stuScore in ascScore:
    if i <= (stuNum * 3/10):
        stuScore[1].append("D")
        D.update({stuScore[0] : stuScore[1]})
    elif i <= (stuNum * 5/10):
        stuScore[1].append("C")
        C.update({stuScore[0] : stuScore[1]})
    elif i <= (stuNum * 8/10):
        stuScore[1].append("B")
        B.update({stuScore[0] : stuScore[1]})
    else:
        stuScore[1].append("A")
        A.update({stuScore[0] : stuScore[1]})
    i += 1

for key, value in ascScore:
    ascScoreDict.update({key : value})
    if key[:4] == "2020":
        asc2020.update({key : value})
    elif key[:4] == "2021":
        asc2021.update({key : value})
    elif key[:4] == "2022":
        asc2022.update({key : value})
    elif key[:4] == "2023":
        asc2023.update({key : value})
    elif key[:4] == "2024":
        asc2024.update({key : value})

writeinfo(2020,asc2020)
writeinfo(2021,asc2021)
writeinfo(2022,asc2022)
writeinfo(2023,asc2023)
writeinfo(2024,asc2024)

descScore = sorted(scoreDict.items(), key=lambda x : (-int(x[1][4]), x[0]))
for key, value in descScore:
    descScoreDict.update({key : value})

writeData("asc",ascScoreDict)
writeData("desc",descScoreDict)
writeData("A", A)
writeData("B", B)
writeData("C", C)
writeData("D", D)


#====================================================================================================================#
#조회 기능#
#====================================================================================================================#
