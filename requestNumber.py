import time
import random
pcNumber = random.randint(1,100)

print("Senden bir sayı girmeni istiyorum.\n Ben de bir sayı tutacağım.\Tahmin edersen sana bir süprizim var :)")
yourNumber = int(input("<<<"))

if yourNumber == pcNumber:
	print("Bakalım doğru mu?")
	time.sleep(2)
	print("Doğru!!!")
	time.sleep(2)

else:
	print("Bilemedin dostum.")
	print(pcNumber , " benim numaramdı.")