import time
print("Let's sort things out with the Bubble Sorting Method!")

def bubble_sort(list):
    n = len(list)
    for i in range(1,n)[::-1]:
        for j in range(0,i):
            first = list[j]
            second = list[j+1]
            if second < first and j == n - 2:
                list = list[0:j] + [second] + [first]
            elif second < first and j == 0:
                list = [second] + [first] + list[j+2:n]
            elif second < first:
                list = list[0:j] + [second] + [first] + list[j+2:n]
    return list

while True:
    our_list = input("What list do you want to sort? Please insert it number by number without commas. \n")
    our_list_splited = our_list.split(' ')
    our_list_splited = list(map(int,our_list_splited))

    start_time = time.time()

    our_list_sorted = bubble_sort(our_list_splited)

    spend_time = time.time() - start_time
    print(f"Your list {our_list_splited} sorted is {our_list_sorted} and the bubble method spent {spend_time} seconds.")

    play_again = input('Want to sort anything else? ')
    if not(play_again.lower() == 'yes'):
        break