

# Recursive Filesystem Code Line Counter
In this repository is a program that recursively scans a directory in a filesystem, detecting all code files for defined filename extensions.

## Installation
There is none. Just put the [count_code_lines.py](https://github.com/jwaitze/Count-Code-Lines-in-Directory/blob/main/count_code_lines.py "count_code_lines.py") file in your code directory and import it:
> from count_code_lines import *

## Parameters
|Parameter|Description
|----------------|-------------------------------|
|`prnt`|if `True`, it is verbose
|`count_blank_lines`|if `True`, blank lines and whitespace is also counted
There are several other parameters that can be adjusted, but if you are confident enough to adjust them, then you are confident enough to take a gander inside the one code file. :P

## Usage
Below is the basic usage:
### Example 1
```python
from count_code_lines import *
result = count_code_lines('D:\\Count-Code-Lines-in-Directory')
count_files, count_lines, time_elapsed \
             = (result[k] for k in ('count_files', 'count_lines', 'time_elapsed'))
print(f'Files: {count_files}, Lines: {count_lines}, Elapsed: {time_elapsed}s')
```
#### Output:
```
Elapsed: 0s, Lines File: 78, Lines Total: 78, Files: 1, Filename: count_code_lines.py
Files: 1, Lines: 78, Elapsed: 0.05s
```

-----

### Example 2
```python
from count_code_lines import *
result = count_code_lines('D:\\Count-Code-Lines-in-Directory', count_blank_lines=True)
count_files, count_lines, time_elapsed \
             = (result[k] for k in ('count_files', 'count_lines', 'time_elapsed'))
print(f'Files: {count_files}, Lines: {count_lines}, Elapsed: {time_elapsed}s')
```
#### Output:
```
Elapsed: 0s, Lines File: 83, Lines Total: 83, Files: 1, Filename: count_code_lines.py
Files: 1, Lines: 83, Elapsed: 0.03s
```

-----

### Example 3
```python
from count_code_lines import *
result = count_code_lines('D:\\IPT', prnt=False)
count_files, count_lines, time_elapsed \
             = (result[k] for k in ('count_files', 'count_lines', 'time_elapsed'))
print(f'Files: {count_files}, Lines: {count_lines}, Elapsed: {time_elapsed}s')
```
#### Output:
```
Files: 561, Lines: 151826, Elapsed: 21.64s
```

