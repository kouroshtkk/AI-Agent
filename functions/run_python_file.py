import os
import subprocess
def run_python_file(
        working_directory:str,file_path:str,args:list[str] | None = None
) -> str:
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
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    except Exception as e:
        return f"Error: common path error {e}"
    try:
        is_file=os.path.isfile(target_dir)
    except Exception as e:
        return f"Error: isfile {e}"
    if not is_file:
        return f'Error: File not found or is not a regular file: "{file_path}"'
    if not target_dir.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file'
    command = ["python",target_dir]
    if args:
        command.extend(args)
    try:
        completed = subprocess.run(command,text=True,capture_output=True,timeout=30)
    except Exception as e:
        return f'Error: subprocess.run {e}'
    return_str = ""
    if completed.returncode != 0:
        return_str+=f"Process exited with code {completed.returncode} "
    if not completed.stdout and not completed.stderr:
        return_str+="No output produced"
    else:
        return_str+=f"STDOUT: {completed.stdout}, STDERR:{completed.stderr}"
    return return_str
