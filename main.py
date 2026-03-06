import json
import zipfile
from wheels import IsUsable, MakeDir, MoveDir

EXTRACT_PATH = "proj"
RESOURCE_PATH = "asset"


def PreLoad():
    print(
        """
          ___
         q888p
        8   60
        8   6
        8 OO
        8O                 q88  88
       08p                  88  ""
      0 8                   88
    00  8        ,adPPYba,  88 d88 d8b,dPPYbap    ,adPPYba,    dooo    qoob
   0    8       a8P_____88. 88  88  88P`   `"8a  a8P_____88.  0p   p  q    0
_00     8      d00```````"  88  88  88       88  8PP``````"  dp    0p88    8
0       8  00p "8b,    ,__  88  88  88       88  "8b,      _dp    qq  p    0
        800      `"Ybbd8"`  88p 88p 88       88p  `"Ybbd80p     dp    doop
       08    _________________________________________________dp
     0p 8   d00000000000000000000000000000000000000000000000000b
   0p   p   8                                                  8
  0p   pp   8                                                  8
 00    pp   8       FelineXEditor | by 田悠汗X 晋珞涵          8
 q    pp    8                                                  8
 qb000p     Q00000000000000000000000000000000000000000000000000P
   **
|你好，我是Feline-pi，Feline编辑器的Python实现+后台
|请开始你的表演！
"""
    )


def LoadScFile():
    print("|当前环节：加载文件")
    print("o输入文件路径: ")
    source = input(">>").strip()
    if not source:
        print("X 文件路径为空")
        return None

    if not IsUsable(source, "r"):
        print("X 文件不存在或不可读")
        return None

    try:
        with zipfile.ZipFile(source, "r") as sb3file:
            MakeDir(EXTRACT_PATH)
            sb3file.extractall(EXTRACT_PATH)
    except zipfile.BadZipFile:
        print("X 压缩包格式错误")
        return None
    except Exception as e:
        print(f"X 解压失败: {e}")
        return None

    try:
        with open(EXTRACT_PATH + "/project.json", "r", encoding="utf-8") as metafile:
            metadata = json.load(metafile)
    except FileNotFoundError:
        print("X project.json 未找到")
        return None
    except json.JSONDecodeError:
        print("X project.json 解析错误")
        return None

    try:
        metajson = json.dumps(metadata, indent=4)
        print(metajson)
        with open(EXTRACT_PATH + "/project.json", "w", encoding="utf-8") as metafile:
            metafile.write(metajson)
        characters = metadata.get("targets", [])
    except Exception as e:
        print(f"X project.json 再次写入失败: {e}")
        return None

    print("|读取完毕，将要分类文件至./" + RESOURCE_PATH + "/[角色名]/[造型名]")
    MakeDir(RESOURCE_PATH)
    for item in characters:
        char_dir = RESOURCE_PATH + "/" + item.get("name", "unnamed") + "/"
        MakeDir(char_dir)
        for i in item.get("costumes", []):
            src = EXTRACT_PATH + "/" + i.get("md5ext", "")
            dst = char_dir + i.get("name", "unnamed") + "." + i.get("dataFormat", "png")
            try:
                MoveDir(src, dst)
            except Exception as e:
                print(f"X 移动造型文件失败: {src} -> {dst}: {e}")

    return metadata


def BasicProcess(metadata):
    if not metadata:
        print("X 没有元数据，无法进行基本处理")
        return

    try:
        metadata.setdefault("meta", {}).setdefault("platform", {})
        metadata["meta"]["platform"]["name"] = "FelineX"
        metadata["meta"]["platform"]["url"] = (
            "FelineX是由田悠汗制作的Scratch编辑器, 基于Feline_Editor和Turbowarp"
        )
        print("|变量: ")
        for item in metadata.get("targets", []):
            for values in item.get("variables", {}):
                print("名称: " + item["variables"][values][0])
                print("值: " + str(item["variables"][values][1]))
            print("|列表: ")
            for values in item.get("lists", {}):
                print("名称: " + item["lists"][values][0])
                print("值: " + ",".join(str(x) for x in item["lists"][values][1]))

    except Exception as e:
        print(f"X 基本处理错误：{e}")


def main():
    PreLoad()
    print("|预加载完毕")
    metadata = LoadScFile()
    print("|文件加载完毕")
    BasicProcess(metadata)
    print("|作品加载完毕")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"X 程序发生未捕获异常：{e}")
