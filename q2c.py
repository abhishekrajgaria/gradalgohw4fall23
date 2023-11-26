import random

def brnm(t):
    cnt = 0
    poss_steps = [-1,1]
    curr_p = random.choice(poss_steps)
    last_dir = curr_p
    for i in range(1,t):
        curr_p = curr_p + random.choice(poss_steps)
        if(curr_p*last_dir < 0):
            if(curr_p<0):
                last_dir = -1
               
            else:
                last_dir = 1
            cnt+=1
    return cnt

if __name__=="__main__":
    t1 = 40000
    t2 = 90000
    t3 = 160000
    avg1 = 0
    avg2 = 0
    avg3 = 0
    for i in range(50):
        avg1+=(brnm(t1))
    for i in range(50):
        avg2+=(brnm(t2))
    for i in range(50):
        avg3+=(brnm(t3))
    print(avg1/50)
    print(avg2/50)
    print(avg3/50)
