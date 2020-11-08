from operator import itemgetter

jobs = list(map(int, input().split(', ')))
indices=[]
for i in range(len(jobs)):
    indices.append(i)
zipped_jobs=zip(jobs,indices)
job_index_needed=int(input())
sorted_list=sorted(zipped_jobs, key=itemgetter(0))
total_clock=0
for i in range(len(sorted_list)):
    value,index=sorted_list[i]
    total_clock+=value
    if index==job_index_needed:
        break

print(total_clock)




