import os
def write_file(working_directory:str,file_path:str,content:str) -> str:
    try:
        working_dir_path = os.path.abspath(working_directory)
    except Exception as e:
    print(f"Error: Abs path error {e}")
    try:
        target_dir = os.path.normpath(os.path.join(working_dir_path,file_path))
    except Exception as e:
        print(f"Error: normpath or join error {e}")
    try:
        valid_target_dir = os.path.commonpath([working_dir_path,target_dir]) == working_dir_path
        if not valid_target_dir:
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    except Exception as e:
        print(f"Error: common path error {e}")
    try:
        is_file=os.path.isfile(target_dir)
        is_dir=os.path.isdir(target_dir)
    except Exception as e:
        print(f"Error: isfile {e}")
    if not is_file:
        return f'Error: File not found or is not a regular file: "{file_path}"'
    if is_dir:
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    try:
        file_path_exits = os.makedirs(target_dir,exist_ok=True)
    except Exception as e:
        print(f'Error: file_path_exists {e}')
    try:
        file = open(target_dir,mode="w")
    except Exception as e:
        print(f'open {e}')
    try:
        count = file.write(content)
    except Exception as e:
        print(f'write {e}')
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'