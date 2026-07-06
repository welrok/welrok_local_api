@echo OFF
echo Building HTML documentation...
call make.bat html

echo Building Markdown documentation...
call make.bat markdown

echo Documentation updated!
pause