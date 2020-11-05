# For question go to:
# https://www.hackerrank.com/challenges/electronics-shop/problem

budget, no_of_keyboards, no_of_usb_drives = map(int, input().split())
keyboard_models = sorted(list(map(int, input().split())))
usb_drives = sorted(list(map(int, input().split())))

most_expensive = -1
cost_of_keyboard_usb = []
for itr in range(no_of_keyboards):
    for ctr in range(no_of_usb_drives):
        if keyboard_models[itr] + usb_drives[ctr] > budget:
            break
        if keyboard_models[itr] + usb_drives[ctr] > most_expensive:
            most_expensive = keyboard_models[itr] + usb_drives[ctr]

print(most_expensive)