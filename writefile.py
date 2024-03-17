txt = "I'm writng a new file!\nThis is amazing!\n"
new_txt = "Here are some new texts!\n"
# with open('text.txt','w') as file:
#    file.write(txt)

with open('text.txt','a') as file:
    file.write(new_txt)