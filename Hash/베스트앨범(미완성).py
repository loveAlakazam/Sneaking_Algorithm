def solution(genres, plays):
    # 1.
    # genres=["classic", "pop", "pop", "jazz"]
    # genre_dict={"classic":0, "pop":1, "jazz":2}
    genre_dict={}
    hash_table={}
    p_sum={}
    val=0
    for g in genres:
        if not g in genre_dict:
            genre_dict[g]=val
            hash_table[val]={}
            p_sum[val]=0
            val+=1
            
    for g,p in zip(genres, plays):
        gnum=genre_dict[g]
        p_sum[gnum]+=p
        if not p in hash_table[gnum]:
            hash_table[gnum][p]=[]
    
    # 기준1: 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
    genre_order= [ x for x,_  in sorted(p_sum.items(), reverse=True)]
    
    for idx, (g, p) in enumerate(zip(genres, plays)):
        gnum=genre_dict[g]
        hash_table[gnum][p].append(idx)
    
    #print(hash_table)
    #hash_table[gnum]에 대해서 정렬..
    for gnum,_ in enumerate(hash_table.values()):
        hash_table[gnum]=sorted(hash_table[gnum].items(), reverse=True)

    print(hash_table)
    answer = []
    for go in genre_order:
        cnt=2
        for c in hash_table[go]:
            idxs=c[1]
            if cnt>0:
                answer.extend(idxs[:cnt]) 
                if len(idxs)>=2:
                    cnt-=2
                else:
                    cnt-=1                  
    return answer
