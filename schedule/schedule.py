#-*- coding=utf-8 -*-

import calendar


# 假日list: "2,9,10,15,16,23"
# 人員資訊: Table: [人, 院區, 職級, 是否職第四點, 偏好行, 偏好不行]
# 病房資訊: Table: [編號, 院區, 是不是ICU, 是不是教學病房]

#############
# Rule:
# 1.    不能連續2天值班
# 2.    盡量避免隔天
# 3.    PGY, R1, R2不能值ICU
# 4.    輕鬆度：1 > 0 > 2 > 3 > 4 > 5 > 6 = 7
# 5.    輕鬆度: 8 > 10 > 9 > 11 > 12 > 13 = 14
# 6.    固定PGY 8班, R1: 9, R2: 8, R3: 7 （需包含1六1 日）, 上限: R4-R6->6, A1-A2->5, A3-A6->4, S->avg_remain
# 7.    剩下的點由S~R4分, 上級的班不多於下級
# 8.    第四點先排
##############

limit_points = {
    "PGY": 9.5,
    "R1": 10.5,
    "R2": 9.5,
    "R3": 8.5,
    "R4": 6,
    "R5": 6,
    "R6": 6,
    "A1": 5,
    "A2": 5,
    "A3": 4,
    "A4": 4,
    "A5": 4,
    "A6": 4
}

people_info = [
    ["Aki", "A", "PGY", "Y", "5", ""],
    ["Bruce", "A", "S", "N", "10", "1,5"],
    ["Ray", "B", "R6", "N", "14", "23,24"],
    ["HY", "B", "PGY", "N", "8", ""],
    ["HY1", "A", "R3", "N", "9", ""],
    ["HY2", "A", "R4", "N", "10", ""],
    ["HY3", "A", "R1", "N", "22", ""],
    ["HY4", "A", "PGY", "Y", "16,19", ""],
    ["HY5", "B", "S", "N", "18", ""],
    ["HY6", "B", "R6", "N", "28", ""],
    ["HY7", "B", "A1", "N", "29,30", ""],
    ["HY8", "B", "R7", "N", "3", ""]
]

ward_info = [
    ["0", "A", "Y", "N"], \
    ["1", "A", "Y", "N"], \
    ["2", "A", "Y", "N"], \
    ["3", "A", "Y", "N"], \
    ["4", "A", "N", "Y"], \
    ["5", "A", "N", "N"], \
    ["6", "A", "N", "N"], \
    ["7", "A", "N", "N"], \
    ["8", "B", "Y", "N"], \
    ["9", "B", "Y", "N"], \
    ["10", "B", "Y", "N"], \
    ["11", "B", "N", "N"], \
    ["12", "B", "N", "N"], \
    ["13", "B", "N", "N"], \
    ["14", "B", "N", "N"]
]



year = 2016
month = 5
saturday_str = "7,14,21,28"
sunday_str = "1,8,15,22,29"

saturday_list = saturday_str.split(",")
sunday_list = sunday_str.split(",")

(first_weekday, num_of_days) = calendar.monthrange(year, month)
workday_num = num_of_days - len(saturday_list) - len(sunday_list)

# calculate total points
total_points_one_station = len(saturday_list) * 1.5 + len(sunday_list) * 2 + workday_num
total_points = total_points_one_station * len(ward_info)
print(total_points_one_station)

def check_level(level):
    if level == 'R1' or level == 'R2' or level == 'R3' or level == 'PGY':
        return True
    return False

people_fixed_points = \
    sum([  fixed_points[x[2]] for x in people_info if check_level(x[2]) ])
'''
equals to : [ fixed_points[x[2]] for x in people_info if check_level(x[2]) ]
a = []
for x in people_info:
    if check_level(x[2]):
        a.append(fixed_points[x[2]])
'''
print(people_fixed_points)
remain_points = people_fixed_points

#def getTotalPoints()




# For output
#print weekday
#print num_of_days


###
