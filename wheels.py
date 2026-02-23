from pathlib import Path
import os

def MakeDir(path, mode="c") -> None:
    root = Path(path).resolve()
    try:
        if root.exists():
            if mode == "c":  # clean and continue
                all_paths = list(root.rglob("*"))
                sorted_paths = sorted(all_paths, key=lambda p: p, reverse=True)
                for item in sorted_paths:
                    try:
                        if item.is_file():
                            item.unlink(missing_ok=True)
                        elif item.is_dir():
                            item.rmdir()
                    except Exception as e:
                        print(f"X 清理路径失败: {item}: {e}")
        else:
            root.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(f"X 创建目录失败: {path}: {e}")

def MoveDir(source, dest) -> None:
    source_path = Path(source)
    dest_path = Path(dest)
    try:
        target_dir = dest_path.parent
        if not target_dir.exists():
            target_dir.mkdir(parents=True)
        source_path.rename(dest_path)
    except Exception as e:
        print(f"X 移动文件失败 {source} -> {dest}: {e}")

def IsUsable(path, mode) -> bool:
    file_path = Path(path)
    if not file_path.exists():
        return False
    if file_path.is_file():
        for i in mode:
            if i == "r":
                if not os.access(file_path, os.R_OK):
                    return False
            elif i == "w":
                if not os.access(file_path, os.W_OK):
                    return False
            else:
                return False
        return True
    elif file_path.is_dir():
        for i in mode:
            if i == "r":
                if not os.access(file_path, os.R_OK):
                    return False
            elif i == "w":
                if not os.access(file_path, os.W_OK):
                    return False
            else:
                return False
        return True
    return False
