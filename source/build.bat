@echo off
cd /d "C:\Users\user\Documents\welrok\API\docs\source"
py -m sphinx.cmd.build -b html . "C:\Users\user\Documents\welrok\API\version1"
echo Documentation updated!
pause