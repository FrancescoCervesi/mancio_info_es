import math

for raggio in range(1, 21):
    circonferenza = 2 * math.pi * raggio
    area = math.pi * raggio ** 2
    print(f"Per il raggio {raggio}:")
    print(f"Circonferenza: {circonferenza}")
    print(f"Area: {area}")
    print()