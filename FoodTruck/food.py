import math
import datetime
def Haversine(lat1, long1, lat2, long2):
    sin2 = math.pow(math.sin((lat1-lat2)/2),2)
    cos2sin2 = math.cos(lat1)*math.cos(lat2)*math.pow(math.sin((long1-long2)/2),2)
    return 2*6378.137*math.asin(sin2+cos2sin2)

# now do the actual problem
madhu_location = raw_input("")
m_lat = float(madhu_location.split(",")[0])
m_long = float(madhu_location.split(",")[1])
max_dist = float(raw_input(""))
# read the header line
temp = raw_input("")
last_dist = 0
saves = []
while True:
    try:
        temp = raw_input("").split(",")
    except EOFError:
        break
    s_lat = float(temp[1])
    s_long = float(temp[2])
    s_num = temp[3]
    if s_num in saves:
        pass
    last_dist = Haversine(m_lat, m_long, s_lat, s_long)
    if last_dist < max_dist:
        saves.append([str(s_num), float(last_dist)])


# output = list(set(subs))
# output = list(map(int, output))
# output.sort()
# output = list(map(str, output))
# output = ",".join(output)
print(output)
