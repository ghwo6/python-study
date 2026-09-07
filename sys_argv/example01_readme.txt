ghwo61351@c6r3s6 python-study % python ./sys_argv/example01.py 
Traceback (most recent call last):
  File "/Users/ghwo61351/tasks_ghwo6/python-study/./sys_argv/example01.py", line 3, in <module>
    file_path = sys.argv[1]
                ~~~~~~~~^^^
IndexError: list index out of range
ghwo61351@c6r3s6 python-study % python ./sys_argv/example01.py .
File path : .
ghwo61351@c6r3s6 python-study % python ./sys_argv/example01.py ./sys_argv/example01.py
File path : ./sys_argv/example01.py
ghwo61351@c6r3s6 python-study % python ./sys_argv/example01.py ./sys_argv/example01.py ./
Insufficient arguments
ghwo61351@c6r3s6 python-study % python ./sys_argv/example01.py ./sys_argv/example01.py ./ ./
Insufficient arguments
ghwo61351@c6r3s6 python-study % 