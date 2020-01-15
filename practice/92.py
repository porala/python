#Count files with a .py extension inside the root1 directory]
import glob
file_list=glob.glob1("/vagrant/python/practice","*.py")
#file_list2=glob.glob1("subdirs/**/*.py", recursive=True)
print(len(file_list))
# print(len(file_list2))
