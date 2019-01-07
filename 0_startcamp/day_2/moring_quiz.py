#평균을 구하시오

my_score = [79,84,66,93]

average_score = sum(my_score)/len(my_score)



def get_avg(numbers):
    total = 0
    for number in numbers:
        total += number
    avg = total / len(numbers)
    return avg

print(get_avg(my_score))



your_score = {
    'math' : 87,
    'english' : 83,
    'korean' : 76,
    'ethics' : 100
}


your_average = sum(your_score.values())/len(your_score)



3: 도시별 온도 평균, 
출력값 -> 서울 :? 대전:? 광주: ? 구미: ?

cities = list(cities_temp.keys())
temp = list(cities_temp.values())

count =0
for i in cities:
        print(cities[count],'의 평균 온도는',sum(temp[count])/len(temp[count]))
        count = count + 1


for city, temperatures in cities_temp.items():
    avg_temperature = round(sum(temperatures) / len(temperatures),2)
    print(city + ': ',(round(sum(temperatures) / len(temperatures),2)), "'c")
    print(city + ': ' + str((round(sum(temperatures) / len(temperatures),2))) + "'c")
    print('{}: {}'.format(city, avg_temperature))


# 4: 도시중에 최근 3일간 가장 추웠던 곳과 가장 더웠던 곳
# Hottest : ??, coldest : ?? 

# cities_temp = {
#     'Seoul' : [-6,-10,5],
#     'Daejeon' : [-3,-5,2],
#     'Gwangju' : [0,-5,10],
#     'Gumi' : [2,-2,9]
# }

# temp = list(cities_temp.values())
# count=0
# max_temp=[]
# for i in temp:
#     max_temp.append(min(temp[count]))
#     count = count + 1
# print(max_temp)

# count1=0
# for city, temperatures in cities_temp.items():
#      if max_temp[count1] == min(max_temp):
#         print('Hottest city :' + city +' and ' + str(min(max_temp)))
#         break
#      else:    
#         count1 = count1 + 1     





cities_temp = {
    'Seoul' : [-6,-10,5],
    'Daejeon' : [-3,-5,2],
    'Gwangju' : [0,-5,10],
    'Gumi' : [2,-2,9]
}

# all_temp에 모든 기온을 모은다.
all_temp =[]
for key, value in cities_temp.items():
    all_temp +=value

print(all_temp)

# all_temp에서 최대/최소를 찾는다
max_temp = max(all_temp)
min_temp = min(all_temp)

print(max_temp, min_temp)

hottest = []
coldest = []

# cities_temp 에서 최댓값/최솟값을 가지고 있는 도시를 찾는다.
for key, value in cities_temp.items():
    if max_temp in value:
        hottest.append(key)
        #print('최고 온도는', key ,'로' , max(value),'도 이다')
    if min_temp in value:
        coldest.append(key)
        #print('최저 온도는', key ,'로' , min(value),'도 이다')

print(hottest,coldest)


  


