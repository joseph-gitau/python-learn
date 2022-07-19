import os

# PATH = r"D:\idm"
# get directory t be sorted eg 'D:\idm\.txt'
PATH1 = input("Paste a directory path to sort: ")
# escape any characters
PATH = rf'{PATH1}'
# print(PATH1)
# quit()
files = os.listdir(PATH)
extensions = []
old_extension = []
extensions_new = []
for f in files:
    root_ext = os.path.splitext(f)
    old_extension.append(root_ext[0])
    # print(root_ext)
    if root_ext[1] != "":
        extensions.append(f)
        # print(extensions)
        #         not in list after extensions
        root_ext_new = os.path.splitext(f)
        extensions_new.append(root_ext_new[1])

# check file extensions not created
unavailable1 = []
for ext_n in extensions_new:
    if ext_n not in old_extension:
        unavailable1.append(ext_n)
unavailable = set(unavailable1)
print(f"unavailable saves: {unavailable}")
# get unmarked files
# for name in extensions:
# print(name)

print(f"old_extension: {old_extension}")
print(f"extensions_new: {extensions_new}")
# make unavailable extensions
for unavail in unavailable:
    os.mkdir(os.path.join(PATH, unavail))

# move all files to their respective Folders
try:
    final_extensions = []
    temp_files = os.listdir(PATH)
    for tf in temp_files:
        temp_root_ext = os.path.splitext(tf)
        if temp_root_ext[1] == "":
            temp_extension = temp_root_ext[0]
            final_extensions.append(temp_extension)

        main, extension = os.path.splitext(tf)
        oldPath = os.path.join(PATH, tf)
        newPath = os.path.join(PATH, extension, tf)
        os.rename(oldPath, newPath)
except FileExistsError as e:
    print(f"Some file already exist: {e}")
print(f"final extension lists: {final_extensions}")
