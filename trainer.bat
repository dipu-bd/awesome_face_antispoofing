@ECHO OFF

SET ENV_NAME=venv

IF NOT EXIST "%ENV_NAME%" (
    ECHO ---------- CREATE NEW VIRTUAL ENV -----------
    python -m venv %ENV_NAME%
    ECHO Created %ENV_NAME%
)

CALL %ENV_NAME%\Scripts\activate.bat

ECHO ---------- INSTALL PIP REQUIREMENTS -----------
python -m pip install -U pip
python -m pip install -r requirements.txt -f https://download.pytorch.org/whl/torch_stable.html
ECHO

FOR /L %%A IN (1,1,15) DO (
    ECHO --------------- TRAINING %%A --------------
    python main.py train
    xcopy checkpoints\MyVggNet16 checkpoints\MyVggNet16_%%A /E /I
    ECHO -------------------------------------------
    ECHO
)

ECHO DONE
