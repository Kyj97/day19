

Score = [['선미', 88], ['초아', 99], ['화사', 71], ['영탁', 78], ['영웅', 67], ['민호', 92]]

def SSort(list):
    for i in range(0, len(list)):
        for j in range(i+1, len(list)):
            if list[i][1] > list[j][1]:
                list[i], list[j] = list[j], list[i]
    return list



print(f'정렬 전 : {Score}')
print(f'정렬 후 : {SSort(Score)}')

print('## 성적별 조 편성표 ##')
for i in range(0, 3):
    print(f'{SSort(Score)[i][0]} : {SSort(Score)[-1-i][0]}')



