import math

r=6371
cord={"lat1":41.507483,"lon1":-99.436554,"lat2":38.504048,"lon2":-98.315949}
latd=math.radians(cord["lat1"]-cord["lat2"])
lond=math.radians(cord["lon1"]-cord["lon2"])
a=math.sin(latd/2)*math.sin(latd/2)+math.cos(math.radians(cord["lat1"]))*math.cos(math.radians(cord["lat2"]))*math.sin(lond/2)*math.sin(lond/2)
c=2*math.atan2(math.sqrt(a),math.sqrt(1-a))
d=r*c
print("The distance between the two location is ",d,"km")