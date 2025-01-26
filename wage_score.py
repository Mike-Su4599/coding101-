income_excel = input()
result = input()
income_excel = open(income_excel, "r", encoding="utf8")
result = open(result, "w", encoding="utf8")
list_income = []
for line in income_excel:
    line = line.strip("\n")
    list_line = line.split(",")
    if list_line[0] == "臺中市":
        dist = str(list_line[1])+str(list_line[2])
        income = float(list_line[5])
        combine = (dist, income)
        list_income.append(combine)
list_income = sorted(list_income, key=lambda x: (x[1], x[0]), reverse=True)
result.writelines("台中市各區平均月收入分數(按比例給分)"+"\n")
result.writelines("\n")
# 開始計算分數，以十分為滿分
lowest = float(list_income[624][1])
highest = float(list_income[0][1])
list_income_ad = []
list_titles = []
for comb in list_income:
    list_income_ad.append(float(comb[1])-lowest)
    list_titles.append(comb[0])
changer = float(10/(highest-lowest))
list_combine = []
average = float()
for i in range(625):
    if i == 0:
        combine = [list_titles[i], 10]
        average += 10
    if i == 624:
        combine = [list_titles[i], 0]
    else:
        score = float(list_income_ad[i])
        combine = [list_titles[i], round(score*changer, 2)]
        average += score*changer
    list_combine.append(combine)
average = round(average/625, 2)
for comb in list_combine:
    score = comb[1]
    title = comb[0]
    result.writelines("{:6s} :{}分\n".format(title, score))
result.writelines("平均分數 :{}分\n".format(average))
