import math
def Haversine(lat1, long1, lat2, long2):
    sin2 = math.pow(math.sin((lat1-lat2)/2),2)
    cos2sin2 = math.cos(lat1)*math.cos(lat2)*math.pow(math.sin((long1-long2)/2),2)
    return 2*6378137*math.asin(sin2+cos2sin2)

# now do the actual problem
madhu_location = input("")
m_lat = float(madhu_location.split(",")[0])
m_long = float(madhu_location.split(",")[1])
max_dist = float(input(""))
# read the header line
temp = input("")
last_dist = 0
subs = []
while last_dist < max_dist:
    temp = input("").split(",")
    s_lat = float(temp[1])
    s_long = float(temp[2])
    s_num = temp[3]
    last_dist = Haversine(m_lat, m_long, s_lat, s_long)
    if last_dist < max_dist:
        subs.append(s_num)

output = ",".join(s_num)
print(output)
