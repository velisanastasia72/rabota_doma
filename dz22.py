import os


def task_file_tree():
    root_dir = 'Work'


    os.makedirs(os.path.join(root_dir, 'F1'), exist_ok=True)
    os.makedirs(os.path.join(root_dir, 'F2', 'F21'), exist_ok=True)

    open(os.path.join(root_dir, 'F1', 'f11.txt'), 'w').close()
    open(os.path.join(root_dir, 'F1', 'f13.txt'), 'w').close()

    with open(os.path.join(root_dir, 'w.txt'), 'w', encoding='utf-8') as f:
        f.write("Текст в файле w.txt")

    with open(os.path.join(root_dir, 'F1', 'f12.txt'), 'w', encoding='utf-8') as f:
        f.write("Текст в файле f12.txt")

    with open(os.path.join(root_dir, 'F2', 'F21', 'f211.txt'), 'w', encoding='utf-8') as f:
        f.write("Текст в файле f211.txt")

    with open(os.path.join(root_dir, 'F2', 'F21', 'f212.txt'), 'w', encoding='utf-8') as f:
        f.write("Текст в файле f212.txt")

    print("Дерево директорий и файлы успешно созданы!\n")

    print("Обход Work снизу вверх")
    for root, dirs, files in os.walk(root_dir, topdown=False):
        print(root)
        print(dirs)
        print(files)

    print("-" * 50)

    print("Обход Work сверху вниз")
    for root, dirs, files in os.walk(root_dir, topdown=True):
        print(root)
        print(dirs)
        print(files)

    print("-" * 50)


if __name__ == "__main__":
    task_file_tree()