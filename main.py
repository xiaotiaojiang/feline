import json
import zipfile
import os
from wheels import MakeDir


def PreLoad():
    print("")
    print("")
    print("         /888\\                                              ")
    print("         8   6|                                              ")
    print("         8   6                                               ")
    print("         8 OO                                                ")
    print("        /8O                 88  88                           ")
    print('       08/                  88  ""                           ')
    print("      0 8                   88                               ")
    print("    00  8        ,adPPYba,  88  88  8b,dPPYba,    ,adPPYba,   ooo    qoob  ")
    print('   0    8       a8P_____88. 88  88  88P`   `"8a  a8P_____88. b   p  q    b ')
    print('_00     8    /008PP"""""""0 88  88  88       88  8PP"""""""0      88       ')
    print('0       8  00/  "8b,   ,__  88  88  88       88  "8b,   ,__  o   q  p    p ')
    print('        800      `"Ybbd8"`  88  88  88       88   `"Ybbd8"`   doob   doop  ')
    print("       08                                                    ")
    print("     0/ 8                                                    ")
    print("   0/   p                                                    ")
    print("  0/   p/                                                    ")
    print(" 0|    p/                                                    ")
    print(" q    p/                                                     ")
    print(" \\b000/                                                     ")
    print("   **                                                        ")
    print("|你好，我是Feline-pi，Feline编辑器的Python实现+后台")
    print("|请开始你的表演！")


def LoadScFile():
    print("|当前环节：加载文件")
    print("o输入文件路径: ")
    source = input(">>")
    if os.path.exists(source):
        with zipfile.ZipFile(source, "r") as sb3file:
            MakeDir("proj")
            sb3file.extractall("./proj/")
            with open("./proj/project.json", "r") as metafile:
                global metadata
                global metajson
                metadata = json.load(metafile)
                metajson = json.dumps(metadata, indent=4)
                print(metajson)

        with open("./tmp/project.json", "w") as metafile:
            metafile.write(metajson)
            characters = metadata["targets"]
        print("|读取完毕，将要分类文件至./assets/[角色名]/[造型名]")
        MakeDir("assets")
        for item in characters:
            MakeDir("./assets/" + item["name"] + "/")
            for i in item["costumes"]:
                os.rename(
                    "./proj/" + i["md5ext"],
                    "./assets/"
                    + item["name"]
                    + "/"
                    + i["name"]
                    + "."
                    + i["dataFormat"],
                )
    else:
        print("X文件不存在")


def BasicProcess():
    metadata["meta"]["platform"]["name"] = "FelineX"
    metadata["meta"]["platform"]["url"] = (
        "FelineX是由田悠汗制作的Scratch编辑器, 基于Feline_Editor和Turbowarp"
    )
    print("|变量: ")
    for item in metadata["targets"]:
        for values in item["variables"]:
            print("名称: " + item["variables"][values][0])
            print("值: " + str(item["variables"][values][1]))
        print("|列表: ")

    for item in metadata["targets"]:
        for values in item["lists"]:
            print("名称: " + item["lists"][values][0])
            print("值: " + ",".join(str(x) for x in item["lists"][values][1]))


def main():
    PreLoad()
    print("|预加载完毕")
    LoadScFile()
    print("|文件加载完毕")
    BasicProcess()
    print("|作品加载完毕")


main()
