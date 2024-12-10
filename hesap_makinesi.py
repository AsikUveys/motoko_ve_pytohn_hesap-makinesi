def toplama (a, b):
    return a + b

def cikarma (a, b):
    return a - b

def carpma (a, b):
    return a * b

def bolme (a, b):
    if b == 0:
        return "Hata: Sıfıra bölme yapılamaz."
    return a / b

def hesap_makinesi():
    print("Hesap Makinesi")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    
while True:
    secim = input("Bir işlem seçin (1/2/3/4) veya çıkmak için 'q' tuşlayın: ")
    
    if secim == 'q':
        print("Hesap maknesi kapatıldı.") 
        break
    
    if secim in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Birinci sayiyi girin: "))
            num2 = float(input("İkinci sayiyi girin: "))
            
            if secim == '1':
                print(f"Sonuç: {toplama(num1, num2)}")
            elif secim == '2':
                print(f"Sonuç: {cikarma(num1, num2)}")
            elif secim == '3':
                print(f"Sonuç: {carpma(num1, num2)}")
            elif secim == '4':
                print(f"Sonuç: {bolme(num1, num2)}")
        except ValueError:
            print("Hatalı giriş! Lütfen sayıları doğru girin.")
    else:
        print("Geçersiz seçim! Lütfen 1, 2, 3, 4 veya 'q' seçin.")


hesap_makinesi()
            
    


