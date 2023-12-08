import sys
from  collections import deque,defaultdict
from itertools import accumulate, product,permutations,combinations,combinations_with_replacement
import math
from bisect import bisect_left,insort_left,bisect_right,insort_right
import time
#product : bit全探索 product(range(2),repeat=n)
#permutations : 順列全探索
#combinations : 組み合わせ（重複無し）
#combinations_with_replacement : 組み合わせ（重複可）
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**7)
import pprint
around4 = ((-1, 0), (1, 0), (0, -1), (0, 1))
around8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
inf = float('inf')
deq = deque()
dd = defaultdict()

II = lambda : int(input())
MII = lambda : map(int,input().split())
LMII = lambda : list(map(int,input().split()))
Ary2 = lambda w,h,element : [[element] * w for _ in range(h)]
is_not_Index_Er = lambda x,y,h,w : 0 <= x < h and 0 <= y < w    #範囲外参照
import random
from statistics import mean, median,variance,stdev

def Input():
    global n,h,v,d,UDLR,ans,x,y,dirt,dirt_dev1,dirt_dev2,dirt_dev3,weight,weight2,weight3,visited_start,visited_goal,visited_mid,count,visited_coordinate,can_visit_list,score,score_list

    score = 0
    count = 0
    visited_coordinate = set()
    n = II()
    h = [input() for _ in range(n-1)]
    v = [input() for _ in range(n)]
    d = [LMII() for _ in range(n)]
    UDLR = ["U","D","L","R"]
    ans = []
    x,y = 0,0
    #現在の汚れ 
    dirt = [[0] * n for _ in range(n)]

    #重みづけ
    # weight = [[0] * n for _ in range(n)]

    # weight3 = [[] *3 for _ in range(3)]
    #訪れた回数
    visited_start = [[0] * n for _ in range(n)]
    visited_goal = [[0] * n for _ in range(n)]
    visited_mid = [[0] * n for _ in range(n)]
    can_visit_list = [[0] * n for _ in range(n)]

def Input_file():
    global n,h,v,d,UDLR,ans,x,y,dirt,dirt_dev1,dirt_dev2,dirt_dev3,weight,weight2,weight3,visited_start,visited_goal,visited_mid,count,visited_coordinate,can_visit_list,score,score_list

    score = 0
    visited_coordinate = set()
    count = 0
    f = open(f"ahc027\\a\\in\\{Input_file_name:04}.txt", 'r')
    data = f.read()
    f.close()
    
    h = []
    v = []
    data = data.split()
    n = int(data[0])
    d = [[None] * n for _ in range(n)]
    for i,j in enumerate(data):
        if 1 <= i <= n-1:
            h.append(j)
        elif 1 <= i <= 2*n -1:
            v.append(j)
        elif 1 <= i:
            d[(i-2*n)//n][(i-2*n)%n] = int(j)
 

    UDLR = ["U","D","L","R"]
    ans = []
    x,y = 0,0
    #現在の汚れ 
    dirt = [[0] * n for _ in range(n)]

    #重みづけ
    weight = [[0] * n for _ in range(n)]
    weight2 = [[0] * n for _ in range(n)]
    weight3 = [[[] for _ in range(3)] for _ in range(3)]
    #訪れた回数
    visited_start = [[0] * n for _ in range(n)]
    visited_goal = [[0] * n for _ in range(n)]
    visited_mid = [[0] * n for _ in range(n)]
    can_visit_list = [[0] * n for _ in range(n)]

def Output():
    print("".join(ans))
    # print(len(ans))

def Output_file():
    f = open(f"ahc027\\a\\out\\{Output_file_name}.txt", 'w')
    f.write("".join(ans))
    f.close()



def calc_can_visit():
    for x in range(n):
        for y in range(n):
            Up,Down,Left,Right = False,False,False,False
            #上
            if 0 <= x-1 < n-1 and 0 <= y < n:
                if h[x-1][y] == "0":
                    Up = True
            #下
            if 0 <= x < n-1 and 0 <= y < n:
                if h[x][y] == "0":
                    Down = True
            #左
            if 0 <= y-1 < n-1 and 0 <= x < n:
                if v[x][y-1] == "0":
                    Left = True
            #右
            if 0 <= y < n-1 and 0 <= x < n:
                if v[x][y] == "0":
                    Right = True
            
            can_visit_list[x][y] = (Up,Down,Left,Right)








def All_visit():
    global x,y
    visited_num = 0
    while visited_num < n ** 2  and len(visited_coordinate) < n ** 2:
        visited_coordinate.add((x,y))
        for i in range(n):
            for j in range(n):
                dirt[i][j] += d[i][j]
        dirt[x][y] = 0
        if visited_start[x][y] == 0:
            visited_num += 1
        visited_start[x][y] += 1
        Vec = can_visit_list[x][y]
        l = []
        for i,j in enumerate(Vec):
            if j and 0 <= x+around4[i][0] < n and 0 <= y+around4[i][1] < n:
                l.append(visited_start[x+around4[i][0]][y+around4[i][1]])
            else:
                l.append(inf)
        temp = l.index(min(l))
        
        ans.append(UDLR[temp])
        x,y = x+around4[temp][0] , y+around4[temp][1]
        if not submit:
            calc_score()



def run_dev(a):
    global x,y,count,visited_mid
    
    while  count < 2500:
        

        # for i in range(n):
        #     for j in range(n):
        #         dirt[i][j] += d[i][j]
        dirt[x][y] = 0
        count += 1
        visited_mid[x][y] += 1

        xy,route = beem(x,y,a)

        for i in range(n):
            for j in range(n):
                dirt[i][j] += len(xy) * d[i][j]

        temp = 0
    
        for i,j in xy:
            visited_mid[i][j] += 1
            dirt[i][j] = (len(xy) - temp) * d[i][j]
            temp += 1


        x,y = xy[-1]
        count += len(route)-1
        
        calc_score()


def run(a):
    global x,y,count,visited_mid
    
    while  count < 25000 or len(visited_coordinate) < n**2:
        
        if count >= max(5000,n**2 * 5) and x == 0 and y == 0 and len(visited_coordinate) == n**2:
            return
        # for i in range(n):
        #     for j in range(n):
        #         dirt[i][j] += d[i][j]
        visited_coordinate.add((x,y))
        dirt[x][y] = 0
        count += 1
        visited_mid[x][y] += 1



        xy,route = beem(x,y,a)

        for i in range(n):
            for j in range(n):
                dirt[i][j] += len(xy) * d[i][j]

        ans.append(route)
        temp = 0
    
        for i,j in xy:
            visited_mid[i][j] += 1
            visited_coordinate.add((i,j))
            dirt[i][j] = (len(xy) - temp) * d[i][j]
            temp += 1
            if count >= max(5000,n**2 * 5) and i == 0 and j == 0 and len(visited_coordinate) == n**2:

                ans[-1] = ans[-1][:temp]
                return

        x,y = xy[-1]
        count += len(route)-1
        if not submit:
            calc_score()

    All_visit()
    goal()



def standard_d():
    for i in range(n):
        for j in range(n):
            dirt[i][j] = 150*d[i][j]


            

def beem(x,y,a):
    # print(dirt)
    # print(d)
    deq = deque()
    deq.append((None,x,y,[(x,y)],0,"",0))
    # print(dirt)
    while deq:
        v,x,y,visited,deep,route,score = deq.popleft()
        Vec = can_visit_list[x][y]
        # print(v,x,y,visited,deep,score )
        for i,j in enumerate(Vec):
            if j and 0 <= x+around4[i][0] < n and 0 <= y+around4[i][1] < n:
                
                if (x+around4[i][0],y+around4[i][1]) in visited:
                    score_temp = score + (d[x+around4[i][0]][y+around4[i][1]]*(deep+1)//2) * max(0.3,1 -  200*  visited_mid[x+around4[i][0]][y+around4[i][1]] / (count+deep) ) **a
                else:
                    score_temp = score + (dirt[x+around4[i][0]][y+around4[i][1]])* max(0.3,1 -  200*  visited_mid[x+around4[i][0]][y+around4[i][1]] / (count+deep) ) **a
                visited_2 = visited + [(x+around4[i][0],y+around4[i][1])]
                # print(score,dirt[x+around4[i][0]][y+around4[i][1]],d[x+around4[i][0]][y+around4[i][1]])
                if deep == 0:
                    deq.append((i,x+around4[i][0],y+around4[i][1],visited_2,deep+1,route+UDLR[i],score_temp))
                else:
                    deq.append((v,x+around4[i][0],y+around4[i][1],visited_2,deep+1,route+UDLR[i],score_temp))
            # print("bef",deq)
            if i == 3 and deq[0][4] != deep :


                sort_deq = sorted(deq,reverse=True,key=lambda x:x[-1])
                deq = deque()
                for i in range(min(16,len(sort_deq))):
                    deq.append(sort_deq[i])

                #深さの決定

                #まとめて返す長さ
                if dev:
                    return_len = 10
                else:
                    return_len = random.choice([2,3,5,7])
                
                if count >= 7500:
                    return_len = 10
                elif count >= 15000:
                    return_len = 31

                if deep == n*3 or len(set(map(lambda x:x[0],sort_deq)))  == 1:
                    # print(max1,max2)
                    if len(sort_deq[0][3]) >= return_len:
                        # print(sort_deq[0][3][1:return_len+1],sort_deq[0][5][:return_len])
                        return sort_deq[0][3][1:return_len+1],sort_deq[0][5][:return_len]
                        
                    else:
                        # print(sort_deq[0][3][1:len(sort_deq[0][3])+1],sort_deq[0][5][:len(sort_deq[0][3])])
                        return sort_deq[0][3][1:len(sort_deq[0][3])+1],sort_deq[0][5][:len(sort_deq[0][3])]
            
        
    
                
                    


   
    

def goal():
    global x,y
    while x != 0 or y != 0:
        for i in range(n):
            for j in range(n):
                dirt[i][j] += d[i][j]
        dirt[x][y] = 0
        visited_goal[x][y] += 1
        Vec = can_visit_list[x][y]
        l = []
        for i,j in enumerate(Vec):
            if j and 0 <= x+around4[i][0] < n and 0 <= y+around4[i][1] < n:
                l.append(visited_goal[x+around4[i][0]][y+around4[i][1]])
            else:
                l.append(inf)
        temp = l.index(min(l))
        ans.append(UDLR[temp])
        x,y = x+around4[temp][0] , y+around4[temp][1]
        if not submit:
            calc_score()



def calc_score():

    global score,dev_calc_count
    dev_calc_count += 1
    for i in range(n):
        for j in range(n):
            score += dirt[i][j]

def get_score():
    return score // dev_calc_count


def get_last_score():
    global score_list
    score_list.append((score-150*sum(map(sum,d)))  // (len(ans)-1//1000))
    # print(score // (len(ans)-1))
    f = open(f"ahc027\\a\\out\\{Score_file_name}.txt", 'a')
    f.write(f"{Input_file_name:04} : {score // (len(ans)-1)}\n")
    f.close()

def vertification(i,j,k):
    print(score // (len(ans)-1//1000))
    f = open(f"ahc027\\a\\out\\{Score_file_name}.txt", 'a')
    f.write(f"{i,j,k} : {score // (len(ans)-1)}\n")
    f.close()

def end():
    print(*score_list)
    print("sum",sum(score_list)//10)
    # print("".join(ans))
    # print("s",int(stdev(score_list)//1000))
    
# calc_weight()
# Input()
# Output()

#検証1
# def main():
#     global Input_file_name,Output_file_name,Score_file_name,score_list
#     score_list = []
#     for i in range(5):
    #     Input_file_name = i
    #     Output_file_name = f"main9_{Input_file_name:04}"
    #     Score_file_name = "score_main9"
    #     a,b,c = 0.5,0.75,1.25
    #     print(a,b,c)
    #     Input_file()
    #     calc_can_visit()
    #     run(a,b,c)
    #     get_last_score()
    #     Output_file()
    #     print("finish:",i)
    # end()

#検証2
# def main():
#     global Input_file_name,Output_file_name,Score_file_name,score_list,submit,dev
#     submit = False
    dev = True
#     # l = [2]
#     # for i in l:
#     score_list = []
#     for j in range(3,4):
#         print("fin:",j)
#         Input_file_name = j
#         Output_file_name = f"main2_{Input_file_name:04}"
#         Score_file_name = "score_main11"
        
#         Input_file()
#         # calc_weight3()
#         standard_d()
#         calc_can_visit()
#         run()
#         get_last_score()
#         Output_file()
#         # print("finish:",j)
#     end()
        

#提出
def main():
    global submit,dev,score,dev_calc_count,count,x,y,visited_mid
    start_time = time.perf_counter() 

    submit = True
    dev = True
    l = [1.25,1.5,1.75]
    score_list=[0,0,0]
    # a,b,c,d = 0.5,0.75,1,2
    Input()
    standard_d()
    calc_can_visit()
    for i,j in enumerate(l):
        dev_calc_count = 0
        score = 0
        run_dev(j)
        score_list[i] = get_score()
        count = 0
        x,y = 0,0
        standard_d()
        visited_mid = [[0] * n for _ in range(n)]
    
    a = l[score_list.index(min(score_list))]
    print(a)
    print(score_list)
    dev = False
    run(a)
    Output()
    end_time = time.perf_counter() 
    print(end_time-start_time)
if __name__ == '__main__':
    main()














