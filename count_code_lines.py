import os, time

this_directory = os.path.dirname(os.path.realpath(__file__))

def read_string_from_file(filepath):
    encodings = ['utf8', 'ISO-8859-1', 'cp1252']
    for encoding in encodings:
        try:
            with open(filepath, 'r', encoding=encoding) as file:
                return file.read()
        except:
            pass

def count_code_lines(directory, size_file_max=25*10**6, size_dir_max=150*10**6,
                     files_in_dir_max=500, dirs_in_dir_max=100, prnt=True,
                     count_blank_lines=False, _result=None, _depth=0,
                     extensions={'py', 'c', 'h', 'cpp', 'ac', 'js', 'html', 'css', 'go',
                                 'java', 'pl', 'rb', 'rake', 's', 'asm', 'msa', 'sql',
                                 'bat', 'sh', 'vbs', 'php', 'cs', 'pas', 'dfm', 'inc',
                                 'swift', 'hpp', 'm', 'mm', 'plist', 'modulemap', 'pch'}):
    if type(extensions) is not set:
        if type(extensions) is not list:
            raise Exception('Invalid extension(s) specified')
        extensions = set(extensions)
    kwargs = locals()
    try:
        if _depth == 0:
            _result = {
                'count_files': 0,
                'count_lines': 0,
                'time_start': time.time()
                }
        result_listdir = [filename for filename in os.listdir(directory) \
                          if os.path.isdir(os.path.join(directory, filename)) \
                          or filename.split('.')[-1].lower() in extensions]
        files_count = sum([1 for filename in result_listdir \
                           if os.path.isfile(os.path.join(directory, filename))])
        if files_count > files_in_dir_max:
            return _result
        dirs_count = sum([1 for filename in result_listdir \
                          if os.path.isdir(os.path.join(directory, filename))])
        if dirs_count > dirs_in_dir_max:
            return _result
        size_dir = sum([os.path.getsize(os.path.join(directory, filename)) for filename in result_listdir \
                           if os.path.isfile(os.path.join(directory, filename))])
        if size_dir > size_dir_max:
            return _result
        for filename in result_listdir:
            filepath = os.path.join(directory, filename)
            if os.path.getsize(filepath) > size_file_max:
                continue
            if os.path.isfile(filepath):
                _result['count_files'] += 1
                contents = read_string_from_file(filepath)
                if contents is None:
                    continue
                lines_file = 0
                if count_blank_lines:
                    lines_file += contents.count('\n') + 1
                else:
                    lines_file += sum([1 for line in contents.split('\n') if len(line.strip()) != 0])
                _result['count_lines'] += lines_file
                if prnt:
                    print(f'Elapsed: {int(time.time() - _result["time_start"])}s,\t' \
                          f'Lines File: {lines_file}, Lines Total: {_result["count_lines"]},\t' \
                          f'Files: {_result["count_files"]}, Filename: {filename}\n', end='')
            elif os.path.isdir(filepath) and filepath != this_directory:
                kwargs['_result'] = _result
                kwargs['_depth'] += 1
                kwargs['directory'] = filepath
                count_code_lines(**kwargs)
        if _depth == 0:
            _result['time_elapsed'] = round(time.time() - _result['time_start'], 2)
            del _result['time_start']
            return _result
        else:
            return _result
    except PermissionError:
        return _result

if __name__ == '__main__':
    print(f'{count_code_lines(this_directory)}\n', end='')
