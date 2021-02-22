
SETLOCAL

CALL :SetupEnv 1 , venv_common , shared_lib

EXIT /B %ERRORLEVEL%

rem SetupEnv(bool reqs, str venvName, str rootname)
:SetupEnv

    set reqs=%~1
    set venvName=%~2
    set rootname=%~3

    cd .\venvs\
    python -m venv --clear %venvName%
    call .\%venvName%\Scripts\activate
    @echo on
    cd ..\%rootname%\
    pip install wheel
    if %reqs% == 0 (
        pip install .
    ) else (
        pip install -r requirements.txt
    )
    call deactivate
    @echo on
    cd ..

EXIT /B %ERRORLEVEL%
