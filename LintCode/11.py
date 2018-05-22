import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        value = int(sys.stdin.readline().strip())
        binv = str(bin(value))[2:]
        count = 0
        while len(binv) > 2:
            if binv(0) != '0':
                binv = binv[1:]
                count = count + 1
            else:
                binv = binv[1:]
        if count % 2 = 0:
            if binv == '00':
                print('don\'t be discourage')
            elif binv == '11':
                print('don\'t be discourage')
            else:
                print('lucky')
        else:
            if binv == '00':
                print('lucky')
            elif binv == '11':
                print('lucky')
            else: 
                print('don\'t be discourage')





        if binv = '00':
            if count % 2 == 0 :
                print('don't be discourage')
            else:
                print('lucky')
         elif binv = '10':
             if count 