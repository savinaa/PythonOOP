from collections import deque
customer_times=deque(map(int,input().split(', ')))
taxis=list(map(int,input().split(', ')))
total_time=0
while(customer_times):
    if len(taxis)==0:
        print(f'Not all customers were driven to their destinations\nCustomers left: {", ".join(map(str,customer_times))}')
        break
    customer=int(customer_times.popleft())
    taxi=taxis.pop()
    if taxi>=customer:
        total_time+=customer
    else:
        customer_times.appendleft(customer)
else:
    print(f'All customers were driven to their destinations\nTotal time: {total_time} minutes')