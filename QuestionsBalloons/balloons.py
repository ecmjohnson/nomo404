test_cases =  int(raw_input(""))

for case in range(0, text_cases):
    test_info = raw_input("")
    total_qs = int(test_info.split(" ")[0])
    lies = int(test_info.split(" ")[1])
    for q in range(0, total_qs):
        question = raw_input("")
        answer = raw_input("")
        if "and" in question:
            pass
        elif "or" in question:
            subs = question.split(" or ")
            lies = lies + len(subs) -1
            for sub in subs:
                generate_array(sub)
        else: # single case
            generate_array(question)


# generates array of length 14 with structure:
# first ten are chars (r,g or b)
# next 3 are numbers in order r,g and b
# and a flag: -1 for false, +1 for true
def generate_array(info):
    
