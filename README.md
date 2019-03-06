# CI-fileDiff

The purpose of this project is to generate large files which store JSON objects and find the difference between them at a row and column level.
Considering ,the JSON dumps are non-relational and not in rows and columns , I have compared them in a non-relational way.(compared row wise with 1 column)
The test_generator.py file contains test which are integrated to CI pipeline implemented using Travis CI.

Screenshot and logs of Travis CI output are attached 

1.24s$ python -m pytest -v
============================= test session starts ==============================
platform linux2 -- Python 2.7.14, pytest-3.0.6, py-1.5.2, pluggy-0.4.0 -- /home/travis/virtualenv/python2.7.14/bin/python
cachedir: .cache
rootdir: /home/travis/build/tarunavardha/CI-fileDiff, inifile: 
collected 1 items 
tests/test_generator.py::DiffFileTestCase::test_same_file_check PASSED
=========================== 1 passed in 0.93 seconds ===========================
The command "python -m pytest -v" exited with 0.
Done. Your build exited with 0.
