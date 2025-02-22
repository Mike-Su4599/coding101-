def ex_combiner(list_rank):
    # list_rank則表示排名的list,順序為人口組成、薪資、社會增加率
    # 輸出為dict
    dict_edu = {"中正里": 10.0, "中和里": 4.32, "下寮里": 3.59, "安仁里": 3.27, "大庄里": 3.01, "文化里": 2.81, "頂寮里": 2.47,
                "大村里": 2.32, "福德里": 1.82, "南簡里": 1.69, "草湳里": 1.08, "興農里": 0.8, "永安里": 0.77, "永寧里": 0.64}
    dict_mage = {"中正里": 10.0, "中和里": 0, "下寮里": 4.12, "安仁里": 1.32, "大庄里": 9.49, "文化里": 5.12, "頂寮里": 2.16,
                 "大村里": 6.48, "福德里": 3.66, "南簡里": 4.86, "草湳里": 0.55, "興農里": 0.97, "永安里": 1.02, "永寧里": 1.89}
    dict_fage = {"中正里": 10.0, "中和里": 0, "下寮里": 3.93, "安仁里": 1.28, "大庄里": 9.49, "文化里": 5.12, "頂寮里": 2.28,
                 "大村里": 6.72, "福德里": 3.68, "南簡里": 4.92, "草湳里": 0.57, "興農里": 0.9, "永安里": 0.96, "永寧里": 1.81}
    dict_wage = {"中正里": 4.55, "中和里": 4.88, "下寮里": 4.12, "安仁里": 0, "大庄里": 8.52, "文化里": 3.81, "頂寮里": 0.48,
                 "大村里": 9.3, "福德里": 4.64, "南簡里": 7.59, "草湳里": 4.29, "興農里": 10, "永安里": 1.02, "永寧里": 8.17}
    list_dist = ["下寮里", "大村里", "大庄里", "中正里", "中和里", "文化里",
                 "永安里", "永寧里", "安仁里", "南簡里", "草湳里", "頂寮里", "福德里", "興農里"]
    dict_final = {"下寮里": 0, "大村里": 0, "大庄里": 0, "中正里": 0, "中和里": 0, "文化里": 0,
                  "永安里": 0, "永寧里": 0, "安仁里": 0, "南簡里": 0, "草湳里": 0, "頂寮里": 0, "福德里": 0, "興農里": 0}
    dict_socinc = {"下寮里": 10, "大村里": 5.65, "大庄里": 5.52, "中正里": 0, "中和里": 9.33, "文化里": 8.37,
                   "永安里": 3.58, "永寧里": 4.81, "安仁里": 5.36, "南簡里": 0, "草湳里": 0, "頂寮里": 8.94, "福德里": 0, "興農里": 0}
    for i in range(3):
        list_rank[i] = (4-int(list_rank[i]))*2

    h_rate = float(list_rank[0])
    w_rate = float(list_rank[1])
    s_rate = float(list_rank[2])

    for i in range(14):
        dist = list_dist[i]
        mage = float(dict_mage[dist])
        fage = float(dict_fage[dist])
        edu = float(dict_edu[dist])
        socnic = float(dict_socinc[dist])
        wage = float(dict_wage[dist])
        age = 0.35*mage + 0.65*fage
        human = age/2+edu/2
        com = (human*(1.7+h_rate)+wage*(1.314+w_rate)+socnic*s_rate)/16.014
        dict_final[dist] = round(com, 2)
    
    dict_final = sorted(list(dict_final.items()), key=lambda y: y[1], reverse=True)
    return dict_final


def human_express(type, list_rank):
    # type 輸入human,socinc或wage。個別代表人口組成、社會增加率、平均薪資。
    # list_rank則表示排名的list,順序為人口組成、薪資、社會增加率
    # 輸出為dict
    dict_edu = {"中正里": 10.0, "中和里": 4.32, "下寮里": 3.59, "安仁里": 3.27, "大庄里": 3.01, "文化里": 2.81, "頂寮里": 2.47,
                "大村里": 2.32, "福德里": 1.82, "南簡里": 1.69, "草湳里": 1.08, "興農里": 0.8, "永安里": 0.77, "永寧里": 0.64}
    dict_mage = {"中正里": 10.0, "中和里": 0, "下寮里": 4.12, "安仁里": 1.32, "大庄里": 9.49, "文化里": 5.12, "頂寮里": 2.16,
                 "大村里": 6.48, "福德里": 3.66, "南簡里": 4.86, "草湳里": 0.55, "興農里": 0.97, "永安里": 1.02, "永寧里": 1.89}
    dict_fage = {"中正里": 10.0, "中和里": 0, "下寮里": 3.93, "安仁里": 1.28, "大庄里": 9.49, "文化里": 5.12, "頂寮里": 2.28,
                 "大村里": 6.72, "福德里": 3.68, "南簡里": 4.92, "草湳里": 0.57, "興農里": 0.9, "永安里": 0.96, "永寧里": 1.81}
    dict_wage = {"中正里": 4.55, "中和里": 4.88, "下寮里": 4.12, "安仁里": 0, "大庄里": 8.52, "文化里": 3.81, "頂寮里": 0.48,
                 "大村里": 9.3, "福德里": 4.64, "南簡里": 7.59, "草湳里": 4.29, "興農里": 10, "永安里": 1.02, "永寧里": 8.17}
    list_dist = ["下寮里", "大村里", "大庄里", "中正里", "中和里", "文化里",
                 "永安里", "永寧里", "安仁里", "南簡里", "草湳里", "頂寮里", "福德里", "興農里"]
    dict_final = {"下寮里": 0, "大村里": 0, "大庄里": 0, "中正里": 0, "中和里": 0, "文化里": 0,
                  "永安里": 0, "永寧里": 0, "安仁里": 0, "南簡里": 0, "草湳里": 0, "頂寮里": 0, "福德里": 0, "興農里": 0}
    dict_socinc = {"下寮里": 10, "大村里": 5.65, "大庄里": 5.52, "中正里": 0, "中和里": 9.33, "文化里": 8.37,
                   "永安里": 3.58, "永寧里": 4.81, "安仁里": 5.36, "南簡里": 0, "草湳里": 0, "頂寮里": 8.94, "福德里": 0, "興農里": 0}
    for i in range(3):
        list_rank[i] = (4-int(list_rank[i]))*2

    h_rate = float(list_rank[0])
    w_rate = float(list_rank[1])
    s_rate = float(list_rank[2])

    if type == "human":
        for i in range(14):
            dist = list_dist[i]
            mage = float(dict_mage[dist])
            fage = float(dict_fage[dist])
            edu = float(dict_edu[dist])
            age = 0.35*mage + 0.65*fage
            human = age/2 + edu/2
            dict_final[dist] = round(human*(1.7+h_rate)/16.14, 2)
    elif type == "wage":
        for i in range(14):
            dist = list_dist[i]
            wage = float(dict_wage[dist])
            dict_final[dist] = round(wage*(1.314+w_rate)/16.14, 2)
    elif type == "socinc":
        for i in range(14):
            dist = list_dist[i]
            socinc = float(dict_socinc[dist])
            dict_final[dist] = round(socinc*s_rate/16.14, 2)
    
    return dict_final


def final_rank(list_rank):
    
    a = str(list_rank[0])
    b = str(list_rank[1])
    c = str(list_rank[2])
    
    #remain = [list_rank[0], list_rank[1], list_rank[]]
    
    
    
    first = ex_combiner(list_rank)[0][0]
    list_rank = [int(a),int(b),int(c)]
    second = ex_combiner(list_rank)[1][0]
    list_rank = [int(a),int(b),int(c)]
    third = ex_combiner(list_rank)[2][0]
    list_rank = [int(a),int(b),int(c)]
    
    human_type = human_express('human', list_rank)
    list_rank = [int(a),int(b),int(c)]
    wage_type = human_express('wage', list_rank)
    list_rank = [int(a),int(b),int(c)]
    socinc_type = human_express('socinc', list_rank)
    list_rank = [int(a),int(b),int(c)]
    
    set1 = [first, human_type[first], wage_type[first], socinc_type[first]]
    set2 = [second, human_type[second], wage_type[second], socinc_type[second]]
    set3 = [third, human_type[third], wage_type[third], socinc_type[third]]
    rank_list = [set1, set2, set3]
    return rank_list

    
