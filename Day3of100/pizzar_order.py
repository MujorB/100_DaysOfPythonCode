#! /usr/bin/python3

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

small_pzr, mid_pzr, lrg_pzr = 15, 20, 25
pepprn_sml, pepprn_lrg_n_mid, cheese_ext = 2, 3, 1
s, m, l, y, n = "S", "M", "L", "Y", "N"
final_bill = 0

if size == s:
    final_bill += small_pzr
    if add_pepperoni == y:
        final_bill += pepprn_sml
    if extra_cheese == y:
        final_bill += cheese_ext
elif size == m:
    final_bill += mid_pzr
    if add_pepperoni == y:
        final_bill += pepprn_lrg_n_mid
    if extra_cheese == y:
        final_bill += cheese_ext
elif size == l:
    final_bill += lrg_pzr
    if add_pepperoni == y:
        final_bill += pepprn_lrg_n_mid
    if extra_cheese == y:
        final_bill += cheese_ext
else:
    if size == s:
        final_bill = small_pzr
    elif size == m:
        final_bill = mid_pzr
    else:
        final_bill = lrg_pzr

print(f"Your final bill is: ${final_bill}.")