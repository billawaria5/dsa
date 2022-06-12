# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def get_subsequence(n, sub_arr, arr):
    # Use a breakpoint in the code line below to debug your script.
    arr_len = len(arr)
    if n >= arr_len:
        print(sub_arr)
        return
    sub_arr.append(arr[n])
    #print(sub_arr)
    get_subsequence(n+1, sub_arr, arr)
    sub_arr.pop(len(sub_arr)-1)
    get_subsequence(n + 1, sub_arr, arr)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arr = [3,1,2]
    get_subsequence(0, [], arr)

