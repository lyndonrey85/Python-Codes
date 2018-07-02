import random

random_num = random.randint(0, 1)
coin = round(random_num)

def coin_tosses():
    head = 0
    tail = 0
    for i in range(5000):
        random_num = random.randint(0, 1)
        coin = round(random_num)
        if coin == 1:
            head += 1
            print "Attempt #{}: Throwing a coin... It's a head! ... Got {} head(s) so far and {} tail(s) so far".format(i, head, tail)
        else:
            tail += 1
            print "Attempt #{}: Throwing a coin... It's a tail! ... Got {} head(s) so far and {} tail(s) so far".format(i, head, tail)
    print "Ending the pragram, thank you!"
    
coin_tosses()