import csv

fin = open("Players.csv")
fout = open("players.txt", "w")
reader = csv.reader(fin, delimiter=',', quotechar='"') 
for fields in reader:
    for i, f in enumerate(fields):
        fields[i] = f.replace("*", "")
    fout.write("{}\n{}\n{}\n{}\n{}\n".format(fields[1], fields[2], fields[3], fields[4], fields[5]))
fout.close()
fin.close()
