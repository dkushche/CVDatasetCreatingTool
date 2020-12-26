# CVDatasetCreatingTool
# Linux setup
Open terminal and run from project directory.
```
./install.sh
./webcam.sh
```
# Windows setup
If you don't have [Python](https://www.python.org/downloads/) install it. Instalation for all users is optional but It's __important__ to add it to __PATH__ . I advise choosing "Install Now" if you're not an experienced user.

If you have python, open command line and run from project directory.
```
windows_install.bat
webcam_env\Scripts\activate.bat
python src\application.py
webcam_env\Scripts\deactivate.bat (_optional_)
```

# Info
You may play with constans in src/config.py and setup program as you want.

With default config program:
- Creates folder named as SURNAME value in src/config(__Important__ You need to replace it by yours)
- Creates 3 subfolders for types of background defined in config
- For each type of background it takes 120 photos, but because I decided to make photos with 3 types of clothes when you push space button it make 40 photos with defined in config interval.

It was the most important moments. Other stuff you may check in config. If you have any questions contact me via email or telegram.
