#평균을 구하시오

my_score = [79,84,66,93]

def avg(a):
    total =0
    for i in a:
        total += i
    avg = total / len(a)
    print(avg)

avg(my_score)



your_score = {
    'math' : 87,
    'english' : 83,
    'korean' : 76,
    'ethics' : 100
}

your_average = sum(your_score.values())/len(your_score)