
def find_second_max(lst):
    for l in lst:
        m = max(l)
        for i in l[::-1]:
            if(i < m):
                print(i)
                break

def main():
    lst = []

    N = int(input())

    for _ in range(N):
        
        tmp = [int(i) for i in input().split()]
        tmp.sort()
        lst.append(tmp)

    find_second_max(lst)

if __name__ == '__main__':
    main()