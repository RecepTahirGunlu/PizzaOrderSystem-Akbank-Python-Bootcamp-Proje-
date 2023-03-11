# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 13:06:55 2023

@author: Recep Tahir Gunlu
"""

# Kütüphaneleri ekle
import csv
from datetime import datetime
from Pizza_and_Sauces import *
import os

# Menu.txt dosyası yoksa oluşturup içine menüyü yazdır
if not os.path.exists('Menu.txt'):
    with open("Menu.txt", "w") as file:
        file.write("* Lütfen Bir Pizza Tabanı Seçiniz:\n1: Klasik\n2: Margarita\n3: TürkPizza\n4: Sade Pizza\n* ve seçeceğiniz sos:\n11: Zeytin\n12: Mantarlar\n13: Keçi Peyniri\n14: Et\n15: Soğan\n16: Mısır\n* Teşekkür ederiz!")

title=['ID','Name Surname','Pizza','Description','Total Cost','CC Number', 'CC Expiration Date', 'CC CVV', 'Order Date']


csv_file_path = 'Orders_Database.csv'

# Orders_Database.csv dosyası yok ise oluşturup sütunların başlıklarını yazdır
if not os.path.exists(csv_file_path):
    # CSV dosyası yoksa oluştur
    with open(csv_file_path, 'w', newline='') as orders_file:
        writer = csv.writer(orders_file)
        writer.writerow(title)

#Main fonksiyonu
def main():
    # Menu.txt dosyasını okuma modunda açıp içindeki metni ekrana yazdırma
    with open('Menu.txt', 'r') as menu_file:
        menu = menu_file.read()
        print(menu)

    # Müşteriden istediği Pizza'yı seçtir ve o pizzanın sınıfından bir nesne oluştur
    while True:

        pizza_choice = int(input('Lütfen pizza seçiminizi yapın (1-4): '))

        if pizza_choice == 1:
            pizza = ClassicPizza()
            break
        elif pizza_choice == 2:
            pizza = MargheritaPizza()
            break
        elif pizza_choice == 3:
            pizza = TurkishPizza()
            break
        elif pizza_choice == 4:
            pizza = PlainPizza()
            break
        else:
            # Geçersiz bir input gelirse birdaha girmesini iste
            print('Hatalı girdi! Geçerli bir pizza seçimi yapın.')


    sauce = None  
    # Müşterinin Pizzasına eklemek istediği sosları kullanıcıdan iste
    while True:
        sauce_choice = int(input("Lütfen sos seçiminizi yapın (11-16)(Ekstra sos istemiyorsanız 0'a basın): "))

        if sauce_choice == 0:
            break
        elif sauce_choice == 11:
            # Eğer sos yoksa (ya da ilk eklenen sos ise) pizza nesnesinin üzerine ekle
            if sauce is None:
                sauce = Olive(pizza)
            # Eğer önceden işlenmiş bir sos var ise onun üzerine ekle
            else:
                sauce = Olive(sauce)
        elif sauce_choice == 12:
            if sauce is None:
                sauce = Mushroom(pizza)
            else:
                sauce = Mushroom(sauce)
        elif sauce_choice == 13:
            if sauce is None:
                sauce = GoatCheese(pizza)
            else:
                sauce = GoatCheese(sauce)
        elif sauce_choice == 14:
            if sauce is None:
                sauce = Meat(pizza)
            else:
                sauce = Meat(sauce)
        elif sauce_choice == 15:
            if sauce is None:
                sauce = Onion(pizza)
            else:
                sauce = Onion(sauce)
        elif sauce_choice == 16:
            if sauce is None:
                sauce = Corn(pizza)
            else:
                sauce = Corn(sauce)
        else:
            # Geçersiz bir input gelirse birdaha girmesini iste
            print('Hatalı girdi! Geçerli bir sos seçimi yapın.')



    # Toplam fiyatı hesaplayın
    total_cost = sauce.get_cost()
    print('Toplam fiyat : ' , total_cost)

    # Kullanıcı bilgilerini alın
    name = input('Adınız: ')
    tc = input('TC Kimlik Numaranız: ')
    cc_number = input('Kredi Kartı Numaranız: ')
    cc_expirationdate = input('Kredi Kartı Son Kullanma Tarihi: ')
    cc_cvv = input('Kredi Kartı CVV: ')

    # Siparis tarihini Yıl-Ay-Gün Saat:Dakika şeklinde al
    current_time = datetime.now()
    current_time.strftime("%Y-%m-%d %H:%M")
    

    # Orders_Database.csv dosyasını append ('a') metodu ile çağırıp kullanıcı ve sipariş bilgilerini csv dosyasına ekle 
    with open(csv_file_path, 'a', newline='') as orders_file:
        writer = csv.writer(orders_file)
        writer.writerow([tc, name, pizza.get_description(), sauce.get_description(), total_cost, cc_number, cc_expirationdate, cc_cvv, current_time])

# Main fonksiyonunu çalıştır
if __name__ == '__main__':
    main()