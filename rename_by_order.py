# 以下文件都存在于同一文件夹下，否则逻辑上会更复杂
# 文件名中必须有一个数字
# 生成的命名是顺序的，但顺序命名的规则是按文件的“Date modified”来排序的

# 在一个文件夹中找所有带指定前缀的文件， 如spam001.txt, spam002.txt, spam004.txt, spam007.txt
# 定位缺失的编号
# 对后面的所有文件重命名， 消除缺失的编号 

# 遍历文件夹 -- os.walk()
# 匹配合适的文件名 -- compile()
    # 方法一： re.compile(r'^(spam)(\d){3}(.txt)$')  /  re.compile(r'spam(\d){3}.txt$') / re.compile(r'spam(\d{3}).txt$') / re.compile(r'spam+(\d{3})+.txt')
    # 方法二： if filename.startswith('spam') and filename.endswith('.txt'): 
# 找到总的匹配文件数量 -- range()
    # 满足匹配的，每次都提取出名字，放入一个列表
    # 统计总的数量
# 依次比对文件名，找出第一个不匹配的位置 
    # 依次将文件名的编号用次序（i+1）来替代
    # 存入： #  beforeFilename =  os.path.joint(source_path, file_lsit[i]),  文件的绝对路径
            # afterFilename = os.path.joint(source_path, new_file_name)， 文件的绝对路径
# 在相同文件夹下依次重命名文件名 -- shutil.move
    # shutil.move(beforeFilename, afterFilename)
    # 使用shutil.move()方法前，先注释掉试一试。使用时在外面加print()查看输出内容


import os, shutil, re
from pathlib import Path

source_path = Path(r'D:\03_program\python\source_folder')
print(source_path)


search_reg = re.compile(r'^(spam)(\d{1,3})(.txt)')  # 该表达式可以
# search_reg = re.compile(r'^(spam)(\d){1,3}(.txt)')  # 该表达式可以
# search_reg = re.compile(r'spam+\d{1,3}+.txt')  # 该表达式可以
# search_reg = re.compile(r'spam+(\d{1,3})+.txt')  # 该表达式不建议使用， 会乱
file_list = []
count = 0
folder_list = []
for folder, subfolder, filenames in os.walk(source_path):
    print(filenames)
    for filename in filenames: 
        if search_reg.search(filename):
            file_list.append(filename)
            count += 1
            folder_list.append(folder)

# print(count)
print(file_list)
for i in range(count):
    beforeFilename = os.path.join(source_path, file_list[i])
    new_file_name = f'spam{i}.txt'   #  该表达式可以. # ToDo 找个更讨巧的命名规则
    # new_file_name = 'spam' + str(i) + '.txt' # 该表达式可以. # ToDo 找个更讨巧的命名规则
    # print(new_file_name)
    afterFilename = os.path.join(source_path, new_file_name)  
    print(shutil.move(beforeFilename,afterFilename))  # 改名

print('done.')



    
