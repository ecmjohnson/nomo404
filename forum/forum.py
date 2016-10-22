import math

def get_sum_first(arr):
    if type(arr) is int:
        return arr
    if type(arr[0]) is list:
        if type(arr[0][0]) is list:
            return sum(arr[0][0])
        return sum(arr[0])
    else:
        return arr[0]

def get_sum_last(arr):
    if type(arr) is int:
        return arr
    if type(arr[-1]) is list:
        if type(arr[-1][-1]) is list:
            return sum(arr[-1][-1])
        return sum(arr[-1])
    else:
        return arr[-1]

def recursive_merging(sizes, bin_size):
    if len(sizes) == 1:
        return sizes
    else:
        arr1 = sizes[:len(sizes)/2]; arr2 = sizes[len(sizes)/2:];
        return merge_func(recursive_merging(arr1, bin_size), recursive_merging(arr2, bin_size), bin_size)

# arr1 and arr2 should be only lists of lists of integers
def merge_func(arr1, arr2, bin_size):
    # import ipdb; ipdb.set_trace()
    len1 = len(arr1); len2 = len(arr2);
    if len1 == len2 == 1: # trivial merge logic
        if type(arr1[0]) is list:
            arr1_val = sum(arr1[0])
        else:
            arr1_val = arr1[0]
        if type(arr2[0]) is list:
            arr2_val = sum(arr2[0])
        else:
            arr2_val = arr2[0]
        ER_curr1 = math.fabs(arr1_val - bin_size)
        ER_curr2 = math.fabs(arr2_val - bin_size)
        ER_comb = math.fabs(arr1_val + arr2_val - bin_size)
        if ER_comb <= ER_curr1 and ER_comb <= ER_curr2:
            return arr1+arr2 # already lists
        else:
            return [arr1, arr2]
    else:
        # we want to combine only the last elem of arr1 and first elem of arr2
        arr1_val = get_sum_last(arr1); arr2_val = get_sum_first(arr2);
        ER_curr1 = arr1_val - bin_size; ER_curr2 = arr2_val - bin_size;
        # ER_curr1 = sum(arr1[-1]) - bin_size; ER_curr2 = sum(arr2[0]) - bin_size;
        # we only need to consider re-allocating the inside elements of arrs
        # three cases:
        #  1. arr1[-1][-1] -> arr2
        #  2. arr2[0][-1] -> arr1
        #  3. arr1[-1][-1], arr2[0][-1] -> new_arr
        #  4. full combination
        #  5. leave separate
        arr1_val = get_sum_last(arr1)
        cs_1_1 = ER_curr1 - arr1_val; cs_1_2 = ER_curr2 + arr1_val;
        # cs_1_1 = ER_curr1 - arr1[-1][-1]; cs_1_2 = ER_curr2 + arr1[-1][-1];
        if cs_1_1 <= ER_curr1 and cs_1_2 <= ER_curr2:
            arr2[0].append(arr1[-1][-1])
            del arr1[-1][-1]
            if len(arr1[-1]) == 0:
                return [arr2]
            else:
                return [arr1, arr2]
        arr2_val = get_sum_last(arr2[0])
        cs_2_1 = ER_curr1 + arr2_val; cs_2_2 = ER_curr2 - arr2_val;
        # cs_2_1 = ER_curr1 + arr2[0][-1]; cs_2_2 = ER_curr2 - arr2[0][-1];
        if cs_2_1 <= ER_curr1 and cs_2_2 <= ER_curr2:
            arr1[-1].append(arr2[0][-1])
            del arr2[0][-1]
            if len(arr2[0]) == 0:
                return [arr1]
            else:
                return [arr1, arr2]
        arr1_val = get_sum_last(arr1); arr2_val = get_sum_last(arr2[0]);
        cs_3_1 = ER_curr1 - arr1_val; cs_3_2 = ER_curr2 - arr2_val;
        # cs_3_1 = ER_curr1 - arr1[-1][-1]; cs_3_2 = ER_curr2 - arr2[0][-1];
        cs_3_3 = math.fabs(arr1_val + arr2_val - bin_size)
        # cs_3_3 = math.fabs(arr1[-1][-1] + arr2[0][-1] - bin_size)
        if cs_3_1 <= ER_curr1 and cs_3_2 <= ER_curr2 and cs_3_3 <= ER_curr1 and cs_3_3 <= ER_curr2:
            if len(arr1[-1]) == 0 and len(arr2[0]) == 0:
                return [arr1[-1][-1], arr2[0][-1]]
            elif len(arr1[-1]) == 0:
                del arr2[0][-1]
                return [[arr1[-1][-1], arr2[0][-1]], arr2]
            elif len(arr2[0]) == 0:
                del arr1[-1][-1]
                return [arr1, [arr1[-1][-1], arr2[0][-1]]]
            else:
                return [arr1, [arr1[-1][-1], arr2[0][-1]], arr2]
        else:
            # import ipdb; ipdb.set_trace()
            if type(arr1) is list and type(arr2) is list and len(arr1) != len(arr2):
                error = sum(arr1) + sum(arr2)
                if error > 1.7*bin_size:
                    return [arr1]+[arr2]
                else:
                    return arr1 + arr2
            else:
                return [arr1]+[arr2]


while True:
    # get the definitions for the next test case
    try:
        temp = raw_input("")
        posts_per_page = int(temp.split(" ")[0])
        num_posts = int(temp.split(" ")[1])
    except EOFError:
        break

    # get the test case data
    threads = []
    for i in range(1, num_posts+1):
        link = int(raw_input(""))
        if i == 1: # this is the first post, must be 0
            threads.append([i])
        else:
            if link == 0: # this is the first post in a new thread
                threads.append([i])
            else: # this post links to a previous thread
                for thread in threads:
                    if link in thread:
                        threads[threads.index(thread)].append(i)

    # sum reduce the threads array
    post_sums = map(len, threads)

    assignment = recursive_merging(post_sums, posts_per_page)
    # import ipdb; ipdb.set_trace()
    sums = map(sum, assignment)
    sums = [x - posts_per_page for x in sums]
    sums = map(math.fabs, sums)
    print(int(max(sums)))
