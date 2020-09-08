*** Settings ***
| Library | Collections
| Library | Process
| Library |  DataDriver
| ...     |  net.csv
| ...     |  delimiter=
| ...     |  encoding=UTF-8
| Test Template  |  print files
*** Test Cases ***
| testcase1
| | print files
*** Keywords ***
| print files

| | [Arguments]  |  ${filename}
| | Log To Console | ${filename}
| | ${result}= | run process | python3 | netrobot.py
| | ${a}= | Should Contain  | ${result.stdout} | ${filename} | msg=Contain Syntax error
| | Log To Console | ${a}





