def sum_of_string(lst):
    for l in lst:
        str_sum = 0
        for i in l:
            if i.isdigit():
                str_sum += int(i)
        print(str_sum)

    

def main():
    N = int(input())
    lst = []
    for _ in range (N):
        lst.append(input())

    sum_of_string(lst)
if __name__ == "__main__":
    main()