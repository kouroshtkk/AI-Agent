import os
def write_file(working_directory:str,file_path:str,content:str) -> str:
    try:
        working_dir_path = os.path.abspath(working_directory)
    except Exception as e:
        return f"Error: Abs path error {e}"
    try:
        target_dir = os.path.normpath(os.path.join(working_dir_path,file_path))
    except Exception as e:
        return f"Error: normpath or join error {e}"
    try:
        valid_target_dir = os.path.commonpath([working_dir_path,target_dir]) == working_dir_path
        if not valid_target_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    except Exception as e:
        return f"Error: common path error {e}"
    try:
        is_dir=os.path.isdir(target_dir)
    except Exception as e:
        print(f"Error: isfile {e}")
    if is_dir:
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    try:
        parent = os.path.dirname(target_dir)
        file_path_exits = os.makedirs(parent,exist_ok=True)
    except Exception as e:
        print(f'Error: file_path_exists {e}')
    try:
        file = open(target_dir,mode="w")
    except Exception as e:
        return f'Error: open {e}'
    try:
        count = file.write(content)
    except Exception as e:
        return f'Error: write {e}'
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "writes to a file if it does not exist creates it, if it exist it overwrites it",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "relative path of file in the working directory"
                },
                "content": {
                    "type": "string",
                    "description": "contents to write to file",
                }
            },
            "required": ["file_path","content"]
        },
    },
}