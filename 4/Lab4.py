import pandas as pd
from colorama import init, Fore, Back, Style

pd.options.display.max_columns = 9
pd.set_option('display.width', 1400)
init(autoreset=True) 

with open('refrigerators.txt') as fileobject:
    refrigerators = []
    refrigerators = fileobject.readlines()
    refrigerators = [line.rstrip('\n') for line in refrigerators]

print("\n")
print(Style.BRIGHT + Fore.BLUE + "Холодильники:",*refrigerators,sep="\n")
print("\n")

with open('parameters.txt') as fileparameters:
    parameters = []
    parameters = fileparameters.readlines()
    parameters = [line.rstrip('\n') for line in parameters]

print(Style.BRIGHT + Fore.BLUE + "Параметри:",*parameters,sep="\n")
print("\n")

with open('importance.txt') as fileimportance:
    importance = []
    importance = fileimportance.readlines()
    importance = [line.rstrip('\n') for line in importance]

file1 = open ('1.txt' , 'r')
exp1 = []
exp1 = [ line.split() for line in file1]

file2 = open ('2.txt' , 'r')
exp2 = []
exp2 = [ line.split() for line in file2]

file3 = open ('3.txt' , 'r')
exp3 = []
exp3 = [ line.split() for line in file3]

file4 = open ('4.txt' , 'r')
exp4 = []
exp4 = [ line.split() for line in file4]

def Price (refrigerator):
    price = float(importance[0]) * (float(exp1[refrigerator][0])+float(exp2[refrigerator][0])+float(exp3[refrigerator][0])+float(exp4[refrigerator][0]))
    return price

def Rosseti (refrigerator):
    rosseti = float(importance[1]) * (float(exp1[refrigerator][1])+float(exp2[refrigerator][1])+float(exp3[refrigerator][1])+float(exp4[refrigerator][1]))
    return rosseti

def Design (refrigerator):
    design = float(importance[2]) * (float(exp1[refrigerator][2])+float(exp2[refrigerator][2])+float(exp3[refrigerator][2])+float(exp4[refrigerator][2]))
    return design

def Energy (refrigerator):
    energy = float(importance[3]) * (float(exp1[refrigerator][3])+float(exp2[refrigerator][3])+float(exp3[refrigerator][3])+float(exp4[refrigerator][3]))
    return energy

def Noise (refrigerator):
    noise = float(importance[4]) * (float(exp1[refrigerator][4])+float(exp2[refrigerator][4])+float(exp3[refrigerator][4])+float(exp4[refrigerator][4]))
    return noise

def Value (refrigerator):
    value = float(importance[5]) * (float(exp1[refrigerator][5])+float(exp2[refrigerator][5])+float(exp3[refrigerator][5])+float(exp4[refrigerator][5]))
    return value

def Light (refrigerator):
    light = float(importance[6]) * (float(exp1[refrigerator][6])+float(exp2[refrigerator][6])+float(exp3[refrigerator][6])+float(exp4[refrigerator][6]))
    return light

#DELFA TTH-85
price1 = Price(0)
rosseti1 = Rosseti(0)
design1 = Design(0)
energy1 = Energy(0)
noise1 = Noise(0)
value1 = Value(0)
light1 = Light(0)

#HISENSE RB224D4BDF
price2 = Price(1)
rosseti2 = Rosseti(1)
design2 = Design(1)
energy2 = Energy(1)
noise2 = Noise(1)
value2 = Value(1)
light2 = Light(1)

#WHIRLPOOL W7 921O K AQUA
price3 = Price(2)
rosseti3 = Rosseti(2)
design3 = Design(2)
energy3 = Energy(2)
noise3 = Noise(2)
value3 = Value(2)
light3 = Light(2)

#INDESIT LI8S1ES
price4 = Price(3)
rosseti4 = Rosseti(3)
design4 = Design(3)
energy4 = Energy(3)
noise4 = Noise(3)
value4 = Value(3)
light4 = Light(3)

#GORENJE NRS 9181 MX
price5 = Price(4)
rosseti5 = Rosseti(4)
design5 = Design(4)
energy5 = Energy(4)
noise5 = Noise(4)
value5 = Value(4)
light5 = Light(4)

#Sum

sum1 = price1 + design1 + rosseti1 + value1 + noise1 + light1 + energy1
sum2 = price2 + design2 + rosseti2 + value2 + noise2 + light2 + energy2
sum3 = price3 + design3 + rosseti3 + value3 + noise3 + light3 + energy3
sum4 = price4 + design4 + rosseti4 + value4 + noise4 + light4 + energy4
sum5= price5 + design5 + rosseti5 + value5 + noise5 + light5 + energy5

parameters.append('')
importance.append('')

df = pd.DataFrame({'№': ['1', '2', '3', '4', '5', '6', '7', 'Сума'],
                   'Параметри': parameters,
                   'Вага': importance,
                   refrigerators[0]: [price1, rosseti1, design1, energy1, noise1, value1, light1, sum1],
                   refrigerators[1]: [price2, rosseti2, design2, energy2, noise2, value2, light2, sum2],
                   refrigerators[2]: [price3, rosseti3, design3, energy3, noise3, value3, light3, sum3],
                   refrigerators[3]: [price4, rosseti4, design4, energy4, noise4, value4, light4, sum4],
                   refrigerators[4]: [price5, rosseti5, design5, energy5, noise5, value5, light5, sum5]})

print(Style.BRIGHT + Fore.GREEN + "Результат:")
print(df)
print('\n')

winer = ''
points = ''

if sum1 > sum5 and sum1 > sum3 and sum1 > sum2 and sum1 > sum4:
    winer = refrigerators[0]
    points = sum1
elif sum2 > sum5 and sum2 > sum3 and sum2 > sum1 and sum2 > sum4:
    winer = refrigerators[1]
    points = sum2
elif sum3 > sum5 and sum3 > sum2 and sum3 > sum1 and sum3 > sum4:
    winer = refrigerators[2]
    points = sum3
elif sum4 > sum5 and sum4 > sum2 and sum4 > sum1 and sum4 > sum3:
    winer = refrigerators[3]
    points = sum4
elif sum5 > sum4 and sum5 > sum2 and sum5 > sum1 and sum5 > sum3:
    winer = refrigerators[4]
    points = sum5
else:
    print("Щось пішло не так при обличсленнях переможця, або переможець не один!")

print(Fore.YELLOW + "Найкращим варіантом вийшов -",winer, '-', points)
print('\n')