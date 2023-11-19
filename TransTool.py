path = input("Please input path of lang \n") + "\\"
sourse = input("Please input the souse lang(without .lang)\n") + ".lang"
target = input("Please input the target lang(without .lang)\n") + ".lang"
count = 0
target_dic = {}
with open(path + target, encoding="UTF8") as file:
    for lines in file.readlines():
        if '=' in lines:
            target_dic[lines.split("=")[0]] = lines.split("=")[1]

file = open(path + "new_" + target, mode='w', encoding="UTF8")
with open(path + sourse, encoding="UTF8") as sfile:
    for lines in sfile.readlines():
        if '=' in lines:
            if lines.split("=")[0] in target_dic:
                if "\n" in target_dic[lines.split("=")[0]]:
                    file.writelines(lines.split(
                        "=")[0] + "=" + target_dic[lines.split("=")[0]])
                else:
                    file.writelines(lines.split(
                        "=")[0] + "=" + target_dic[lines.split("=")[0]] + "\n")
            else:
                file.writelines(lines.replace("\n", "") + "#WTT" + "\n")
                count += 1
        else:
            file.writelines(lines)
file.close()
print("Create a new file named " + ("new_" + target))
print("There are ", count, "lines wait to trans, mark with #WTT")
