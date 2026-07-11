import os
def get_file_content(working_directory: str,file_path: str) -> str:
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
    except Exception as e:
        print(f"Error: isfile {e}")
    if not is_file:
        return f'Error: File not found or is not a regular file: "{file_path}"'
    file = open(target_dir,mode='r')
    result = file.read(10000)
    if file.read(1):
        result+= f'[...File "{file_path}" truncated at 10000 characters]'
    return result
schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "gets and reads the content of a file and returns the content of the one specific file (file_path) at max 10000 characters, file must exist it is different from listing files!",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "path to the file to read"
                }
            },
            "required": ["file_path"]
        },
    },
}
