import os


def readFile(path, source, target, isALL):
    count = 0
    if isALL:
        file = open(path + 'new\\' + "new_" + target,
                    mode='w', encoding="UTF8")
    else:
        file = open(path + "new_" + target, mode='w', encoding="UTF8")
    with open(path + source, encoding="UTF8") as sfile:
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


target_dic = {}
path = input("Please input path of lang \n") + "\\"
source = input("Please input the souse lang(without .lang)\n") + ".lang"
target = input(
    "Please input the target lang(without .lang) or just input all for others\n") + ".lang"

if 'all' in target:
    if not os.path.exists(path + 'new'):
        os.mkdir(path + 'new')
    for lang in os.listdir(path):
        if source in lang or os.path.isdir(path + lang):
            continue
        target_dic = {}
        with open(path + lang, encoding="UTF8") as file:
            for lines in file.readlines():
                if '=' in lines:
                    target_dic[lines.split("=")[0]] = lines.split("=")[1]
        readFile(path, source, lang, True)
else:
    with open(path + target, encoding="UTF8") as file:
        for lines in file.readlines():
            if '=' in lines:
                target_dic[lines.split("=")[0]] = lines.split("=")[1]
    readFile(path, source, target, False)
