from functions.get_files_info import get_files_info


print("result for current dir")
print(get_files_info("calculator","."))
print("result for pkg")
print(get_files_info("calculator","pkg"))
print("result for /bin")
print(get_files_info("calculator","/bin"))
print("result for ../")
print(get_files_info("calculator","../"))
