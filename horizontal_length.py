import math

def yatay_mesafe_hesapla(nokta1, nokta2):
   
    x1, y1 = nokta1
    x2, y2 = nokta2
    
    mesafe = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return mesafe

p1 = (100.0, 100.0)
p2 = (130.0, 140.0)
p3 = (160.0, 100.0)
p4 = (130.0, 60.0)

mesafe_p1_p2 = yatay_mesafe_hesapla(p1, p2)
mesafe_p1_p3 = yatay_mesafe_hesapla(p1, p3)
mesafe_p1_p4 = yatay_mesafe_hesapla(p1, p4)

print(f"p1 - p2 Yatay Mesafesi: {mesafe_p1_p2:.2f} metre")
print(f"p1 - p3 Yatay Mesafesi: {mesafe_p1_p3:.2f} metre")
print(f"p1 - p4 Yatay Mesafesi: {mesafe_p1_p4:.2f} metre")