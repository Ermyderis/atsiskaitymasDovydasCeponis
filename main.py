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
data_list= [[1, 10, 34, 110, 400, 30, 20],
               [-5, -10, 55, 120, 30],
               [2, 67, 23, 78, 200],
               ]


def antra(filtruoti):

    rezultataiisfiltruoto = []
    #Filtruojama pagal nurodytas reiksme
    isfiltruotiskaiciai = list(filter(lambda x: x >= 10 and x <= 100, filtruoti))
    #gaunamas vidurkis skaiciu
    vidurkis = sum(isfiltruotiskaiciai)/ len(isfiltruotiskaiciai)
    #i lista pridedamas vidurkis
    rezultataiisfiltruoto.append(vidurkis)
    minimali = (min(isfiltruotiskaiciai))
    rezultataiisfiltruoto.append(minimali)
    maksimalireiksme = (max(isfiltruotiskaiciai))
    rezultataiisfiltruoto.append(maksimalireiksme)
    sumavisu = sum(isfiltruotiskaiciai)
    rezultataiisfiltruoto.append(sumavisu)

    return(rezultataiisfiltruoto)


#gaunamos reiksme
print(antra(data_list[0]))
print(antra(data_list[1]))
print(antra(data_list[2]))




"""
Sukurti programą, kuri vartotojo paprašo įvesti 
simbolių seką - x, bei vieną skaitmenį - y. Atlikti 
patikrinimus, jogy tikrai skaičius, jog jis yra didesnis už 0, bei x ilgis dalinasi į lygias 
dalis po y simbolių. Jei šios sąlygostenkinamos 
suskaidyti tekstą į lygias dalis po y simbolių ir atspausdinti unikalius simbolius (svarbu išlaikytisimbolių eiliškumą).
"""

#funkcija kuri isdalina teksta po pasirinktas dalis
def iskaidyti(seq, chunk, skip_tail=False):
    lst = []
    if chunk <= len(seq):
        lst.extend([seq[:chunk]])
        lst.extend(iskaidyti(seq[chunk:], chunk, skip_tail))
    elif not skip_tail and seq:
        lst.extend([seq])
    return lst

def trecias():
    x = input("Ivesti raides")
    kartoti = True
    #tikrina ar ivestas simbolis yra skaicius
    while(kartoti == True):
        try:
            y = int(input("Ivesti viena teigiama skaiciu"))
            kartoti = False
        except:
            print("Veskite tik skaiciu")

    #tikrinama ar ivestas skaicius yra daugiau uz 0
    if(y < 0):
        print("Ivestas skaicius yra mazesnis uz 0")
        #tikrinama ar ivestas tekstas gali buti dalinamas i dalis pasirinkto skaiciaus
    elif(len(x)%y != 0):
        print("Nera dalinamas is pasirinkto skaiciaus")
    else:
        # gaunama po kiek raidziu turi buti isdalintame vienete
        dalina = int(len(x) / y)
        print(dalina)
        print(iskaidyti(x, dalina))


trecias()

"""
Sukurti funkciją, kuri atlieka teksto suspaudimą. Funkcija priima vieną parametrą
x - tekstas ir grąžina tekstąsudarytą iš simbolio ir 
jo iš eilės einančių pasikartojimų skaičiaus t.y. suspaudimas vykdomas grupuojant iš eilėseinančius simbolius
"""
#funkcija iskaido teksta i simbolius
def split(word):
    return list(word)
#gauna kintamaji
def penktauzduotis(tekstas):
    sentence = tekstas
    print(sentence.count('a'))
    print(split(tekstas))

#penktauzduotis("Mano vardas")





