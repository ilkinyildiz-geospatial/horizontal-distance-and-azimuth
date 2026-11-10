import math

def semt_hesapla(nokta1, nokta2):
   
    
    x1, y1 = nokta1
    x2, y2 = nokta2
    
    dx = x2 - x1  
    dy = y2 - y1  

    if dx == 0 and dy == 0:
        return 0.0
    if dx > 0 and dy == 0:
        return 0.0
    if dx == 0 and dy > 0:
        return 100.0
    if dx < 0 and dy == 0:
        return 200.0
    if dx == 0 and dy < 0:
        return 300.0
        

    nu_radyan = math.atan(abs(dy) / abs(dx))
    nu_grad = nu_radyan * (200.0 / math.pi)

    if dx > 0 and dy > 0:
        semt = nu_grad
    elif dx < 0 and dy > 0:
        semt = 200.0 - nu_grad
    elif dx < 0 and dy < 0:
        semt = 200.0 + nu_grad
    elif dx > 0 and dy < 0:
        semt = 400.0 - nu_grad
    else:
        semt = 0.0
        
    return semt

p1 = (100.0, 100.0)
p2 = (130.0, 140.0)
p3 = (160.0, 100.0)
p4 = (130.0, 60.0)

semt_p1_p3 = semt_hesapla(p1, p3)
semt_p2_p4 = semt_hesapla(p2, p4)
semt_p3_p4 = semt_hesapla(p3, p4)

print(f"p1 - p3 Semt Açısı: {semt_p1_p3:.4f} grad")
print(f"p2 - p4 Semt Açısı: {semt_p2_p4:.4f} grad")
print(f"p3 - p4 Semt Açısı: {semt_p3_p4:.4f} grad")