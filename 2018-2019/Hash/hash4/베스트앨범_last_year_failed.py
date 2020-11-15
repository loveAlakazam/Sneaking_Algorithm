def playsOrdered(plays, arr):
    order1= [ plays[x] for x in arr] #plays[x]를 원소로하는 리스트 생성
    order1.sort(reverse=True) #plays (재생수) 내림차순으로 정렬
    return [plays.index(x) for x in order1]
            

def orderedList(arr):
    arr_index=[ arr.index(g) for g in arr]
    tmp=None
    max_sums=arr[0]
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[j]>max_sums:
                tmp=j
                arr_index[j]=i
                arr_index[i]=tmp
                max_sums=arr[j]
    return arr_index
            

def solution(genres, plays):
    genType=list(set(genres)) #genre type: set(집합) ==> list(리스트)

    part_genre=[]
    for i in range(len(genType)):
        part_genre.append([]) #비어있는 리스트 생성(새로운 행 생성)
        for g in range(len(genres)):
            if genres[g]==genType[i]: #genres[g]가 genType[i]와 같다면
                part_genre[i].append(g) #genres[g]의 index번호 g를 part_genre[i]의 열로 추가

    #각행에서 내림차순 순으로 정렬
    for i in range(len(genType)):
        if len(part_genre[i])>1:
            part_genre[i]=playsOrdered(plays, part_genre[i])

    #gen_sums: part_genre 각 행의 모든 원소의 합을 나타냄
    gen_sums=[]
    for i in range(len(genType)):
        gen_sums.append( sum( [plays[g] for g in part_genre[i]] ) )

    #장르 순서 정하기 (gen_sums의 크기가 가장 큰 것으로 우선)
    pick_order=orderedList(gen_sums)
    result=[]
    for p in pick_order:
        if len(part_genre[p])<2:
            result.append(part_genre[p][0])
        else:#len(part_genre[p]>=2
            for i in range(2):
                result.append(part_genre[p][i])

    return result
