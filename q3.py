import random
def vote(t):
    mj = 0
    poss_steps = [-1,1]
    bias = [0.48, 0.52]
    for i in range(100):
        cnt=0
        c_vote = []
        for j in range(t):
            c_vote.append(random.choices(poss_steps, weights=bias)[0])
        for j in range(t):
            if(c_vote[j]==1):
                cnt+=1
        if(cnt>(t/2)):
            mj+=1
    return mj/100
        
if __name__=="__main__":
    t1 = 20
    t2 = 100
    t3 = 400
    print(vote(20))
    print(vote(100))
    print(vote(400))

    t = 400
    while(vote(t)<0.9):
        t+=1
    print(t)

