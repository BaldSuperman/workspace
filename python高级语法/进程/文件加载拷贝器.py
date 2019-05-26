from multiprocessing import Pool
import os
def copy_file(file_name, old_folder_name, new_folder_name ):
    '''完成文件复制'''
    print("-0------模拟从{0}copy文件：{1}".format(old_folder_name, file_name))
    old_f = open(old_folder_name + "/" +file_name,"rb")
    content = old_f.read()
    old_f.close()
    new_f = open(new_folder_name + '/' +file_name, "wb")
    new_f.write(content)
    new_f.close()
def main():
    # 1.获取用户要copy的文件夹名字
    old_folder_name = input("请输入要copy的文件夹的名字")
    # 创建一个新的文件夹
    try:
        new_folder_name = old_folder_name + "[附件]"
        os.mkdir(new_folder_name)
    except:
        pass
    # 获取文件夹的所有的待copy的文件名字 listdir（）
    file_names = os.listdir(old_folder_name)
    print(file_names)
    #创建进程池
    po = Pool(5)
    #向进程池中添加copy文件的任务
    for file_name in file_names:
        po.apply_async(copy_file, args=(file_name, old_folder_name, new_folder_name ))
    # 复制文件夹中的文件，到新文件夹中的文件夹中去
    po.close()
    po.join()
if __name__ == '__main__':
    main()