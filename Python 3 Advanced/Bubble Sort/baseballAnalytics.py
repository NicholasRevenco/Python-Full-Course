# List of baseball players with random stats
p1 = ["B. Harper", .254, 27, 92]
p2 = ["J. Soler", .256, 36, 91]
p3 = ["C. Yelich", .329, 41, 89]
p4 = ["C. Bellinger", .312, 42, 100]
p5 = ["M. Trout", .299, 41, 99]
p6 = ["F. Lindor", .296, 23, 56]
p7 = ["M. Betts", .285, 21, 67]
p8 = ["A. Rendon", .328, 29, 104]
p9 = ["D. Lemahieu", .331, 22, 87]
p10 = ["R. Acuna", .290, 36, 89]

playerList = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]


def bubbleSort(lst, stat):
  player_lst = []
  for j in range(len(lst)):
    for i in range(len(lst)-1):
      if lst[i][stat] > lst[i+1][stat]:
        old_number = lst[i]
        lst[i] = lst[i+1]
        lst[i+1] = old_number
  for i in range(len(lst)-1, -1, -1):
    print("   " + str(lst[i][0]))

print("Average Leaderboard")
bubbleSort(playerList, 1)


print("\nHome Run Leaderboard")
bubbleSort(playerList, 2)

print("\nRBI Leaderboard")
bubbleSort(playerList, 3)
