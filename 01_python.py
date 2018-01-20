def get_avg(d):
    sum = 0
    for e in d:
        sum += d[e]
    avg = sum/len(d)
    return avg

def get_max(d):
    max = 0
    sbj = None
    for e in d:
        if d[e]>=max:
            max = d[e]
            sbj = e
    return (sbj, max)
    

#main
n_sub = int(input("Enter the number of subjects: "))
i = 0
a = {}
while i<n_sub :
    sub = input("Enter a subject: ")
    scr = int(input("Enter score: "))
    i += 1
    a[sub] = scr


avg_num = get_avg(a)
subject, score = get_max(a)

print("Average score: " + str(avg_num))
print("Higest score: " + subject + ", " + str(score))
