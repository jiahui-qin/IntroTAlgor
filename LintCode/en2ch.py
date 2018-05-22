nums = str(0)
if nums == '0':
    print('L')
leng = len(nums)
ch = ''
q = ['','S','B','Q','W']
flag = 0
for i in range(leng):
    if nums[leng - i - 1] != '0':
        ch = nums[leng - i - 1] + q[i] +ch
        flag = 0
        print(nums[leng - i - 1],q[i])
    else:
        if flag == 0:
            ch =  'L' + ch
            flag = 1
if ch[len(ch)-1] == 'L':
    ch = ch[0:len(ch)-1]
print(ch)
