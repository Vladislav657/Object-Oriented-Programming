dict = {}
n1 = int(input())
i = 0
while i < n1:
    s1 = input().split(':')
    if len(s1) == 1:
        dict.setdefault(s1[0], [])
        dict[s1[0]].append('None')
    else:
        c = s1[0].split()
        b = s1[1].split()
        dict.setdefault(c[0], [])
        for j in b:
           dict[c[0]].append(j)
    i += 1
n2 = int(input())
u = 0
while u < n2:
    rez = 'No'
    g1 = input().split()
    g2 = g1[1]
    a1 = [g1[0]]
    st = 0
    if g2 == a1[0]:
        rez = 'Yes'
    else:
        while len(a1) != 0 and st == 0:
            b = a1.pop()
            for key, value in dict.items():
                for j in value:
                    if j == b and key != g2:
                        a1.append(key)
                    elif j == b and key == g2:
                        rez = 'Yes'
                        st = 1
                        a1 = []
    u += 1
    print(rez)