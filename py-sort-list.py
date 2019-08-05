import pandas as pd

survey = pd.read_csv("survey.csv")
register = pd.read_csv("register.csv")

survey_Col = survey.columns
survey_Val = survey.values

for str in survey_Col:
    if str == 'Username':
        email = str

elistsurvey = survey[email].tolist()
elistregistered = register[email].tolist()

totalreg = len(elistregistered)
totalsur = len(elistsurvey)
print("Total email in list ", totalreg+totalsur)

dup = []
for n1 in elistregistered:
    for n2 in elistsurvey:
        if n1 == n2:
            dup.append(n2)

totaldup = len(dup)
            
for nc in dup:
    for n1 in elistregistered:
        if nc == n1:
            elistregistered.remove(n1)

cleanreg = len(elistregistered)
            
for nc in dup:
    for n2 in elistsurvey:
        if nc == n2:
            elistsurvey.remove(n2)

cleansur = len(elistsurvey)
            
#print(totaldup)
#print(cleanreg)
#print(cleansur)
#print("Total email without dups ", totaldup+cleanreg+cleansur)

for n1 in elistregistered:
    dup.append(n1)

for n2 in elistsurvey:
    dup.append(n2)

finalcount = len(dup)
print("Final email list without dups ", finalcount)

for nc in dup:
    print(nc)

f = open("mail-list.txt","w")
for nc in dup:
    f.write(nc)
    f.write(";\n")

f.close()
    
