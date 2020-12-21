def get_magic_triangle(n):
    triangle=[[1],[1, 1]]
    for r in range(2,n):
        current_row=[]
        for c in range(0,r+1):
            if c==0:
                num=triangle[r-1][0]
            elif c==(r):
                num=triangle[r-1][-1]
            else:
                left_n=triangle[r-1][c-1]
                right_n=triangle[r-1][c]
                num=num=left_n+right_n
            current_row.append(num)
        triangle.append(current_row)
    return triangle

print(get_magic_triangle(5))

