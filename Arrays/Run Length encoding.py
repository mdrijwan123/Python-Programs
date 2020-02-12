def run_length(string):
    cur_char = ''
    start = string[0]
    final_string = ""
    cnt = 1
    for i in range(1,len(string)):
        if string[i] != start:
            final_string = final_string + string[i-1] + str(cnt)
            start = string[i]
            cnt = 1
        else:
            cnt += 1
    final_string = final_string + string[i] + str(cnt)

    print(final_string)

string = "wwwwaaadexxxxxx"
run_length(string)
