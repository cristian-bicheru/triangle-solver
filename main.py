import math
vals = input("(1)SSS (2)SSA (3)SAA: ")
if vals == "1":
    sides = list(map(float, input("a, b, c: ").split(",")))
    sides.sort()
    if sides[0]+sides[1]>sides[2]:
        for each in sides: print(float(round(each,1)))
        C = math.degrees(math.acos((sides[0]**2+sides[1]**2-sides[2]**2)/(2*sides[0]*sides[1])))
        B = math.degrees(math.asin(sides[1]*math.sin(math.radians(C))/sides[2]))
        for each in [180-B-C, B, C]: print(float(round(each,1)))
    else: print("degenerate triangle")
elif vals == "2":
    sides = list(map(float, input("a, b, C: ").split(",")))
    if 0<sides[2]<180:
        for each in range(0,2): print(float(round(sides[each],1)))
        c = math.sqrt(sides[0]**2+sides[1]**2-2*sides[0]*sides[1]*math.cos(math.radians(sides[2])))
        A = math.degrees(math.asin(sides[0]*math.sin(math.radians(sides[2]))/c))
        for each in [c, A, 180-A-sides[2], sides[2]]: print(float(round(each,1)))
    else: print("no reflex or negative angles")
elif vals == "3":
    sides = list(map(float, input("a, B, C: ").split(",")))
    if sides[1]>0 and sides[2]>0 and sides[1]+sides[2]<180:
        print(float(round(sides[0],1)))
        for each in [(sides[0]*math.sin(math.radians(sides[1])))/(math.sin(math.radians(180-sides[1]-sides[2]))), (sides[0]*math.sin(math.radians(sides[2])))/(math.sin(math.radians(180-sides[1]-sides[2]))), 180-sides[1]-sides[2], sides[1], sides[2]]: print(float(round(each,1)))
    else: print("no infinite triangles or negative/reflex angles")
else: print("invalid choice")
