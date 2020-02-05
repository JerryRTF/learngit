charlist = input("请输入要计算出24的四个正整数，以空格分隔：").split()
# "".join(charlist)
str_list = [
    '(axb)yczd',
    '(axbyc)zd',
    'ax(byc)zd',
    'ax(byczd)',
    'axby(czd)',
    '(axb)y(czd)',
    '(ax(byc))zd',
    'ax((byc)zd)',
    'ax(by(czd))',
    'axbyczd'
]
operators = '+-*/'
ii = 0
#count = 0
sum = 0
s = set([])

while ii < 10:
    i = 0
    j = 0
    m = 0
    n = 0
    # p = str_list[ii].index('a')
    # q = str_list[ii].index('b')
    # r = str_list[ii].index('c')
    # s = str_list[ii].index('d')
    for c1 in operators:
        a = str_list[ii].replace('x', c1)
        for c2 in operators:
            b = a.replace('y', c2)
            for c3 in operators:
                c = b.replace('z', c3)

                #d = c
                while i < 4:
                    d = c.replace('a', charlist[i])
                    #d = d[:p]+charlist[i]+d[p+1:]
                    while j < 4:
                        if j != i:
                            e = d.replace('b', charlist[j])
                            #d = d[:q]+charlist[j]+d[q+1:]
                            while m < 4:
                                if ((m != j) and (m != i)):
                                    f = e.replace('c', charlist[m])
                                    #d = d[:r]+charlist[m]+d[r+1:]
                                    while n < 4:
                                        if ((n != m) and (n != j) and (n != i)):
                                            g = f.replace('d', charlist[n])
                                            #d = d[:s] + charlist[n] + d[s + 1:]
                                            try:
                                                if (eval(g) == 24):
                                                    s.add(g + '=24')
                                                    sum = sum+1
                                                # print(g)
                                                # count = count+1
                                            except ZeroDivisionError:
                                                pass
                                        n = n + 1
                                m = m + 1
                                n = 0
                        j = j + 1
                        m = 0
                    i = i + 1
                    j = 0

                i = 0
                j = 0
                m = 0
                n = 0

    ii = ii + 1

for element in s:
    print(element)

# print(count)
if sum == 0:
    print("无法生成！")
