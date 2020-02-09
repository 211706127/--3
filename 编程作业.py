def change1(s1):
    for s in s1:
        if s=="一":
            return(1)
        elif s=="二":
            return(2)
        elif s=="三":
            return(3)
        elif s=="四":
            return(4)
        elif s=="五":
            return(5)
        elif s=="六":
            return(6)
        elif s=="七":
            return(7)
        elif s=="八":
            return(8)
        elif s=="九":
            return(9)
        elif s=="零":
            return(0)
        else:
            return("输入错误，只能为零-九。")

# 中文数字 —> 阿拉伯数字
def change_alb(s1):
    m = 0
    t = 1
    if s1[0]=="负":
        s1 = s1[1:]
        t*=-1
    # [ : : -1]将字符串逆序
    s1_nixu = s1[ : : -1]
    for s in s1_nixu:
        m = change1(s)*t + m
        t*=10
    return m

def change2(s1):
    for s in s1:
        if s=="1":
            return("一")
        elif s=="2":
            return("二")
        elif s=="3":
            return("三")
        elif s=="4":
            return("四")
        elif s=="5":
            return("五")
        elif s=="6":
            return("六")
        elif s=="7":
            return("七")
        elif s=="8":
            return("八")
        elif s=="9":
            return("九")
        elif s=="0":
            return("零")
        elif s=="-":
            return("负")
        else:
            return("输入错误，只能为0-9。")

# 阿拉伯数字 —> 中文数字  
def change_zw(s):
    s_zhongwen = ""       
    for c in s:
        s_zhongwen += change2(c)
    return s_zhongwen


#进行处理的方法
def chuli(s):
    s_list = s.split(" ")
##     定义语句
    if s_list[0] == "整数" and len(s_list) == 4:
#         print(s_list[3])
        dict1[s_list[1]] = change_alb(s_list[3])

##     查看语句
    elif (s_list[0] == "看看") and len(s_list) == 2:
        # 取出key为s_list[1]的值
        s_value = dict1.get(s_list[1], None)
        if s_value:
            print(change_zw(str(s_value)))
        # 将阿拉伯数字的值转换成中文数字，并输出
        else:
            print(s_list[1][1:-1])
            
##     如果...则...否则 语句
    elif (s_list[0] == "如果") and len(s_list) == 2:
        fouze(s)
        
##     运算语句
    else: 
        if s_list[1] == "减少" and len(s_list) == 3:
            dict1[s_list[0]] = dict1[ s_list[0] ] - change_alb(s_list[2])
        elif s_list[1] == "增加" and len(s_list) == 3:
            dict1[s_list[0]] = dict1[ s_list[0] ] + change_alb(s_list[2])


#判断
def panduan(s):
    if "大于" in s:
        # 此处的 s_list 存放的是：所要判断的 变量名 和 判断的值。
        s_list = s.split(" 大于 ")
        if dict1[ s_list[0] ] > change_alb(s_list[1]):
            return True
        else:
            return False

# 创建一个用来存放变量名跟值的空字典
dict1 = {}


#主函数，先判断是否有如果，有的话先把三个语句切分出来，再调用chuli方法进行处理
def main(s):
    s_list = []
    if "如果" in s:
        s_list = []
        for c in [" 否则 ", " 则 ", "如果 "]:
            if c in s:
                s_list1 = s.split(c)
                s_list.append(s_list1[-1])
                s = s_list1[0]
#         for ls in s_list:
#             if "如果" in s:
#                 main1(ls)
        if len(s_list)>1:
            if panduan(s_list[-1]):
                main(s_list[-2])
            else:
                if s_list[0]=="无":
                    return 0
                else:
                    main(s_list[0])
    else:
        main(s)
