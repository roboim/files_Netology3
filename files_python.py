# Чтение, сортировка и запись в файл
import os


def create_dump_file(current_path, target_path_result):
    folder_name = target_path_result
    path_to_target_file = os.path.join(current_path, folder_name, 'result.txt')
    with open(path_to_target_file, 'w', encoding='UTF-8') as t_file:
        t_file.write('')


def sorting_of_files(current_path, target_folder):
    folder_name = target_folder
    path_to_target_folder = os.path.join(current_path, folder_name)
    target_files = os.listdir(path_to_target_folder)
    target_list = []
    for file in target_files:
        path_to_target_file = os.path.join(current_path, folder_name, file)
        with open(path_to_target_file, 'r', encoding='UTF-8') as t_file:
            qty_lines = len(t_file.readlines())
            target_list.append([qty_lines, file])
    target_list.sort(key=lambda x: x[0], reverse=False)
    return target_list


def write_result_file(current_path, source_file_dir, result_file_dir, file_name, file_lines):
    result_folder_name = result_file_dir
    target_folder_name = source_file_dir
    path_to_result_file = os.path.join(current_path, result_folder_name, 'result.txt')
    path_to_target_file = os.path.join(current_path, target_folder_name, file_name)
    with open(path_to_result_file, 'a', encoding='UTF-8') as result_file:
        result_file.write(file_name + '\n')
        result_file.write(str(file_lines) + '\n')
        with open(path_to_target_file, 'r', encoding='UTF-8') as source_file:
            content_of_target = source_file.readlines()
        content_of_target[-1] = content_of_target[-1].rstrip()
        result_file.writelines(content_of_target)
        result_file.write('\n')


source = 'source'
result = 'result'
current_path_main = os.getcwd()
create_dump_file(current_path_main, result)

target_list = sorting_of_files(current_path_main, source)
for file in target_list:
    write_result_file(current_path_main, source, result, file[1], file[0])
