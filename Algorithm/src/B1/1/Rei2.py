a = [23,53,65,33,24,13,65,4,55,33,85,100,43,56,73,47,23,76,3423]

histo = [0 for i  in range(11)]

for ai in a:
    rank = ai // 10
    if rank >= 0 and rank <= 10:
        histo[rank] += 1

for i in range(11):
    print('{:3d} - : {:3d}'.format(i * 10 , histo[i]))
    