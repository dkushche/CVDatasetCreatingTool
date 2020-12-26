@IF NOT EXIST webcam_env (
    @ECHO "Start installation process"
    @python -m venv webcam_env
    @webcam_env\Scripts\activate.bat
    @pip install -r requirements.txt
    @webcam_env\Scripts\deactivate.bat
    @ECHO "Installed"
) ELSE (
    @ECHO "Already installed"
)

