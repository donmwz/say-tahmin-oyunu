import random
import time
from colorama import Fore, Style

print("Sayı tahmin oyununa hoşgeldiniz.")
time.sleep(2)
print("GEN SOFTWARE SUNAR;")
print("1 SORU= 1 PUAN;"
      "10 SORU= 10 PUAN DEĞERİNDEDİR."
      " Kazanmak için En az 5 tane soruyu doğru cevpla! ")
time.sleep(3)
print("Oyun Yükleniyor Lütfen Bekleyiniz...")

for i in range(3):
    print("LOADİNG" + "." * (i + 1))
    time.sleep(1)

name = input("Adınız: ")
score = 0

for i in range(1, 11):
    print("----------------------------------------")
    min_val = 1
    max_val = 5 * ((i - 1) // 2) + 10 if i < 9 else 100
    print(Fore.BLUE + f"{min_val}-{max_val} arasında sayı tutuluyor. ZORLUK {i}/10")
    random_number = random.randint(min_val, max_val)
    guess = int(input(f"Lütfen {i}. soru tahminini bildir: "))

    if random_number == guess:
        print(Fore.GREEN + f"Doğru cevap Harikasın {name}. +1 puan")
        score += 1
    else:
        print(Fore.RED +f"Yanlış cevap {name}. +0 puan")

print(f"{name}, toplamda {score} puan aldın. Oyun bitti!")
