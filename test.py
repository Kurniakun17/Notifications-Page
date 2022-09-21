def maxCost(cost, labels, dailyCount):
    num = len(labels)
    i = 0
    total = 0
    while(i < num):
        temp = 0
        count = 0
        while(count < dailyCount and i < num):
            if(labels[i] == "legal"):
                count += 1
                temp  += cost[i]
            i+=1
        total += temp if count<dailyCount else 0
    return total

a = int(input())
harga = []
label = []
for i in range(a):
    temp = int(input())
    harga.append(temp)

b = int(input())
for i in range(b):
    temp = input()
    label.append(temp)

dailycost = int(input())

print(maxCost(harga,label,dailycost))


# nomor 2
# hitung distinct subarray
# contoh a = [1,1,1,3,3,3,2]
# jawaban 4