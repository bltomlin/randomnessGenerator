MIN_LENGTH = 100
bin_str = ""
count = 0

# Loops while the string fails requirements

while (len(bin_str) < MIN_LENGTH and count < MIN_LENGTH):
    print("Print a random string containing 0 or 1:")
    user_in = input()
    
    # parses 1s and 0s from input
    
    for num in user_in:
        if num == "1":
            bin_str += "1"
            count += 1
        elif num == "0":
            bin_str += "0"
            count += 1
        else:
            continue
    remain_count = MIN_LENGTH - count 
    
    # logic for printing results
    
    if (remain_count > 0 ):
        print("Current data length is " + str(count) + ", " + str(remain_count) + " symbols left" )
    else:
        print("Final data string:")
        print(bin_str)
        break
