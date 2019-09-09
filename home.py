import shutil
import os
# 刪除指定目錄所有檔案或連目錄一併刪除
def delallfiles(pathname,undeldir):
    for x in range(1,16):
        dirname = pathname + str(x)
		shutil.rmtree(dirname)
		if undeldir != 'd':        # 保留目錄
			os.mkdir(dirname)      # 重建目錄
'''	
# filecopy :
    shutil.copyfile("directory_path\\source_filename","path\\destination_filename"
    目標已存在同檔名會overwrite
# directorycopy :
   from distutils.dir_util import copy_tree
   copy_tree("/a/b/c", "/x/y/z")
'''
# 刪除指定目錄之檔案
def delfiles(pathname):
	os.remove(pathname)