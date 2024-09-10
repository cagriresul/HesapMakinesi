
from replit import clear

def toplama(n1,n2):
    return n1 + n2

def çıkarma(n1,n2):
    return n1 - n2

def çarpma(n1,n2):
    return n1 * n2

def bölme(n1,n2):
    return n1 / n2

def üs_alma(n1,n2):
    return n1 ** n2

def mod_alma(n1,n2):
    return n1 % n2

operatörler ={
    "+":toplama,
    "-":çıkarma,
    "/":bölme,
    "*":çarpma,
    "**" :üs_alma,
    "%" : mod_alma
}

def işlem():
    sayı1 = float(input("Sayı1'i giriniz : "))
    for sembol in operatörler:
        print(sembol)
    devam_etme = True


    while devam_etme:
        operatör_sembolü = input("Bir operatör seçin : ")
        sayı2 = float(input("Sayı2 giriniz : "))
        hesaplama_fonksiyonu = operatörler[operatör_sembolü]
        cevap = hesaplama_fonksiyonu(sayı1,sayı2)
        print(f"{sayı1}{operatör_sembolü}{sayı2} = {cevap}")

        if input(f"{cevap} ile işlem yapmak istiyorsanız 'evet', istemıyorsanız'hayır'") == "evet":
            sayı1 = cevap

        else :
            devam_etme = False
            clear()




işlem()




