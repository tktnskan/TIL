team = [
    'john', 10000,
    'neo', 100,
    'tak', 40500
]

type(team[2:4])  #리스트에서 슬라이싱으로 뽑으면 리스트의 형태로 뽑힘
new_member = ['js', 10]
#team = team + new_member
team += new_member
# len(team) == 8
del(team[2])
# len(team) == 7

del(team[2:4]) #통째로 지울수도있음
# len(team) == 5

