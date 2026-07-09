import os
def get_files_info(working_directory:str,directory:str)-> str:
    try:
        working_dir_path = os.path.abspath(working_directory)
    except Exception as e:
        print(f"Error: Abs path error {e}")
    try:
        target_dir = os.path.normpath(os.path.join(working_dir_path,directory))
    except Exception as e:
        print(f"Error: normpath or join error {e}")
    try:
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
    except Exception as e:
        print(f"Error: is dir error {e}")
    try:
        valid_target_dir = os.path.commonpath([working_dir_path,target_dir]) == working_dir_path
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    except Exception as e:
        print(f"Error: common path error {e}")
    try:
        new_list = os.listdir(target_dir)
    except Exception as e:
        print(f"Error: list dir {e}")
    files_list=[]
    for item in new_list:
        try:
            is_dir = os.path.isdir(target_dir+"/"+item)
            item_size=os.path.getsize(target_dir+"/"+item)
        except Exception as e:
            print(f"Error: get size or is_dir {e}")
        files_list.append("- "+item+": file_size="+str(item_size)+" bytes, is_dir="+str(is_dir))

    total_str = "\n".join(files_list)
    return total_str
