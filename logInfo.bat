@echo off
@cd c:\users\Samil.Vargas\Desktop\
For /f "tokens=2-4 delims=/ " %%a in ('date /t') do (set mydate=%%c-%%a-%%b)
For /f "tokens=1-2 delims=/:" %%a in ('time /t') do (set mytime=%%a%%b)
@echo Some one entered on the computer "at" %mydate%_%mytime%  >> info.txt