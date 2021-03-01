"""
Sukurti funkciją, kuri priima
tris parametrus: n - tekstas, a - tekstas, kurio
simboliai yra teigiami, b - tekstas, kuriosimboliai
yra neigiami. Teigiami simboliai yra verti 1, neigiami
verti -1, o simboliai, kurių nėra nei a, nei b teksteyra vertas 0.
Funkcija suskaičiuoja teksto įvertį ir jį grąžina
"""
#Fukcija priimanti 3 kintamuosius
def pirmas(n, a, b):
    try:
        #Tekstasn gauna n kintamojo reiksme
        tekstasn = n
        #teigiamia gauna a kintamojo reiksme
        teigiamia = a
        #neigiamib gauna b kintamojo reiksme
        neigiamib = b
        #priskiriamos 0 reiksmes
        pirmas = 0
        antras = 0
        #for ciklas skirtas pakartotinai eiti per tekstasn
        for i in tekstasn:
            #ieskoti teigiamiems nariams
            for y in teigiamia:
                #Jei teigiamame pridedama po 1
                if(i == y):
                    pirmas = pirmas + 1
            #ieskoti neigiamiems nariam
            for z in neigiamib:
            #jei neigiamam atimama po 1
                if(i==z):
                    antras = antras + 1
        print(pirmas-antras)
    except:
        print("Klaida, naudokite tik teksta")

print("Pagal pvz 1: ")
pirmas("keturiolika", "ktur", "ila")

print("Pagal pvz 2: ")
pirmas("vienas du trys", "vn ", "ayds")

print("Pvz su klaida: ")
pirmas("keturiolika", "ktur", 1)

"""
Sukurti funkciją, kuri priima vieną
parametrą a - vienos dimensijos sąrašas.
Funkcijoje atliekamas sąrašofiltravimas paliekant
reikšmes iš intervalo 10-100. Funkcija grąžina išfiltruotų
reikšmių: vidurkį, didžiausią irmažiausią reikšmes, bei sumą.
Sukurti antrą funkciją, kuri priima vieną parametrą b - sąrašą
sudarytą iš sąrašųir kiekvienam sąrašo elementui
iškviečia pirmą funkciją ir atspausdina gautą rezultatą
"""
data_list= [   [1, 10, 34, 110, 400, 30, 20],   [-5, -10, 55, 120, 30],   [2, 67, 23, 78, 200],]



"""
Sukurti programą, kuri vartotojo paprašo įvesti 
simbolių seką - x, bei vieną skaitmenį - y. Atlikti 
patikrinimus, jogy tikrai skaičius, jog jis yra didesnis už 0, bei x ilgis dalinasi į lygias 
dalis po y simbolių. Jei šios sąlygostenkinamos 
suskaidyti tekstą į lygias dalis po y simbolių ir atspausdinti unikalius simbolius (svarbu išlaikytisimbolių eiliškumą).
"""
def split_str(seq, chunk, skip_tail=False):
    lst = []
    if chunk <= len(seq):
        lst.extend([seq[:chunk]])
        lst.extend(split_str(seq[chunk:], chunk, skip_tail))
    elif not skip_tail and seq:
        lst.extend([seq])
    return lst

def trecias():
    x = input("Ivesti raides")
    y = int(input("Ivesti viena teigiama skaiciu"))


    if(y < 0):
        print("Ivestas skaicius yra mazesnis uz 0")
    elif(len(x)%y != 0):
        print("Nera dalinamas is pasirinkto skaiciaus")
    else:
        print(split_str(x, y))
        print(split_str(x, y, skip_tail=True))


trecias()

"""
Sukurti funkciją, kuri atlieka teksto suspaudimą. Funkcija priima vieną parametrą
x - tekstas ir grąžina tekstąsudarytą iš simbolio ir 
jo iš eilės einančių pasikartojimų skaičiaus t.y. suspaudimas vykdomas grupuojant iš eilėseinančius simbolius
"""

def penktauzduotis():




