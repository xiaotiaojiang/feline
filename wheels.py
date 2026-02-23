from pathlib import Path


def MakeDir(path, mode="c") -> None:
    root = Path(path).resolve()
    if path.exists():
        if mode == "c":
            all_paths = list(root.rglob("*"))
            sorted_paths = sorted(all_paths, key=lambda p: p, reverse=True)
            for item in sorted_paths:
                if not item.is_relative_to(root):
                    continue
                if item.is_file():
                    item.unlink(missing_ok=True)
                elif item.is_dir():
                    item.rmdir()
    else:
        root.mkdir(parents=True, exist_ok=True)
