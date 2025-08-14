import math

def hesap():
    print("Hesap makinesine hoşgeldiniz")
    print("4 temelk işlem ve özel işlemler olarak iki farklı kısımdan oluşuşacak")

    toplam=0

    sayi=int(input("Sayinizi giriniz"))
    toplam=toplam+sayi

    for x in range(100):
        b=input("Hangi işlemi yapmak istediğinizi giriniz toplama için:+, çıkarma için:-,çarpma için:*, bölme için: /, diğer işlemler icin ozel")
        if b=="+":
            c=int(input("Sayiyi giriniz"))
            toplam=toplam+c
            print("toplam:",toplam)
        elif b=="-":
            c=int(input("Sayiyi giriniz"))
            toplam=toplam-c
            print("Toplam:",toplam)
        elif b=="*":
            c=int(input("Sayiyi giriniz"))
            toplam=toplam*c
            print("Toplam:",toplam)
        elif b=="/":
            c=int(input("Sayiyi giriniz"))
            toplam=toplam/c
            print("Toplam",toplam)
        elif b=="ozel":
            print("Özel işlemler kısmına hoşgeldiniz")
            sec=input("Karesi için:kare  küpü için:kup karekök için:karekok  ")
            if sec=="kare":
                toplam=toplam*toplam
                print("Toplam:",toplam)
            elif sec=="kup":
                toplam=toplam*toplam*toplam
                print("Toplam:",toplam)
            elif sec=="karekok":
                toplam=math.sqrt(toplam)
                print("Toplam:",toplam)
        elif b=="0":
            print("Sayiyi sifirladiniz")
            toplam=0
            print("Toplam:",0)
        elif b=="bitir":
            print("Hesap makinesinden çikis yaptınız")
            print("Toplam:",toplam)
            break



hesap()