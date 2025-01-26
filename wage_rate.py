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
result.writelines("台中市各區平均月收入"+"\n")
result.writelines("    "+"\n")
for com in list_income:
    result.writelines("{:6s} :{}元\n".format(
        str(com[0]), round(com[1], 2)))
