import os

def is_text_file(file_path):
    return file_path.lower().endswith(".txt")

def replace_lines_starting_with_num(file_path, from, to):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            if line.strip().startswith(str(from)):
                file.write(str(to) + line[1:])
            else:
                file.write(line)

def find_text_files(root_dir):
    text_files = []
    for foldername, subfolders, filenames in os.walk(root_dir):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            if is_text_file(file_path):
                text_files.append(file_path)
    return text_files

if __name__ == "__main__":
    dirs = []
    
    path = "/path/for/dataset" # 데이터셋 경로
    
    dirs.append(path + "/train/labels")    
    dirs.append(path + "/valid/labels")    
    dirs.append(path + "/test/labels")    
    

    from = 0 # 바꿀대상 클래스 번호 
    to = 1 # 변환될 클래스 번호   

    for di in dirs:
        text_files = find_text_files(di)

        if text_files:
            print("Text files found:")
            for file in text_files:
                replace_lines_starting_with_num(file, from, to)
                print(file)
