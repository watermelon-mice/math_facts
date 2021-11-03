import random

how_many_times_do_you_need_to_do=5

f=0
for i in range(1,how_many_times_do_you_need_to_do+1):
    a=random.randint(0,100)
    b=random.randint(0,10)
    c=a+b
    print("question {}: {}+{}=?".format(i,a,b))
    d=input()
    e=int(d)
    if(e==c):
        print("correct")
        f=f+1
    else:
        print("wrong the right answer should be {}".format(c))
print("the score is {}/{}".format(f,how_many_times_do_you_need_to_do))
