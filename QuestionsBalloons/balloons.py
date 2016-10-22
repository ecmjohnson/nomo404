test_cases =  int(raw_input(""))

for case in range(0, text_cases):
    test_info = raw_input("")
    total_qs = int(test_info.split(" ")[0])
    lies = int(test_info.split(" ")[1])
    arrays = []
    for q in range(0, total_qs):
        question = raw_input("")
        answer = raw_input("")
        if "and" in question:
            arrays.append(generate_and(question))
        elif "or" in question:
            subs = question.split(" or ")
            lies = lies + len(subs) -1
            for sub in subs:
                arrays.append(generate_array(sub.split(" ")))
        else: # single case
            arrays.append(generate_array(question.split(" ")))


# generates array of length 14 with structure:
# first ten are chars (r,g or b)
# next 3 are numbers in order r,g and b
# and a flag: -1 for false, +1 for true
RED = 10; GREEN = 11; BLUE = 12;
def generate_array(info_arr):
    out_arr = [0]*14
    if "colour" in info_arr:
        index = int(info_arr[1])
        out_arr[index] = info_arr[2]
    else:
        if info_arr[1] == "r":
            out_arr[RED] = int(info_arr[2])
        elif info_arr[1] == "g":
            out_arr[GREEN] = int(info_arr[2])
        else:
            out_arr[BLUE] = int(info_arr[2])

def generate_and(info_arr):
    parts = info_arr.split(" and ")
    out_arr = [0]*14
    for part in parts:
        if "colour" in info_arr:
            index = int(info_arr[1])
            out_arr[index] = info_arr[2]
        else:
            if info_arr[1] == "r":
                out_arr[RED] += int(info_arr[2])
            elif info_arr[1] == "g":
                out_arr[GREEN] += int(info_arr[2])
            else:
                out_arr[BLUE] += int(info_arr[2])
