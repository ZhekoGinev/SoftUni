import os

# this only affects files in the same directory where the renamer.py is located!!!
# you can either copy the files over or move the renamer.py to their directory
# or you can improve the script, maybe with os.walk(), and be so kind as to share it with me

current_dir = os.listdir()

for file in current_dir:
    if file in [
        "renamer.py",
    ]:  # files in this list will not be renamed
        # it was used in earlier version but could be useful
        continue
    new_name = file

    # make your changes to the file name below
    # I had files named -- 01. file_name_something.py
    # And wanted to have - 01-file-name-something.py
    # below is just an example code, you should delete it!!!
    new_name = "-".join(new_name.split(". "))
    new_name = new_name.replace("_", "-").replace(" link", "")

    # this will rename the file with the new_name
    os.rename(file, new_name)
