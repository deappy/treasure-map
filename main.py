line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() 
alpha=position[0].lower()
abc=["a","b","c"]
alpha_index=abc.index(alpha)
num_index=int(position[1])-1
map[num_index][alpha_index]='X'
print(f"{line1}\n{line2}\n{line3}")