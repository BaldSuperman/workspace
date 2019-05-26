from multiprocessing import Manager, Pool
import os
def copy_file(q, file_name, old_folder_name, new_folder_name ):
    '''完成文件复制'''

    old_f = open(old_folder_name + "/" +file_name,"rb")
    content = old_f.read()
    old_f.close()
    new_f = open(new_folder_name + '/' +file_name, "wb")
    new_f.write(content)
    new_f.close()
    #如果拷贝完，就像队列中写入一个信息，表示已近完成
    q.put(file_name)
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
    #创建队列
    q = Manager().Queue()
    #向进程池中添加copy文件的任务
    for file_name in file_names:
        po.apply_async(copy_file, args=(q, file_name, old_folder_name, new_folder_name ))

    # 复制文件夹中的文件，到新文件夹中的文件夹中去
    po.close()
    #po.join()
    all_file_num = len(file_names)
    copy_ok = 0
    while True:
        if copy_ok >= all_file_num:
            break
        file_name = q.get()
        print("已经完成copy： {0}".format(file_name))
        print("拷贝的进度为： %f %%"%(copy_ok*100/all_file_num))
        copy_ok += 1

if __name__ == '__main__':
    main()