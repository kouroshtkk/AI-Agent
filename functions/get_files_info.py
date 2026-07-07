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
    return f'Success: "{directory}" is within the working directory'
