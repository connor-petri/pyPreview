from os import system


if __name__ == "__main__":
    system('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')

    system("brew install pyenv")
    system("brew install tcl-tk")

    # pyenv setup
    system("pyenv install 3.10.6")
    system("pyenv virtualenv 3.10.6 pyPreview")
    system("pyenv activate pyPreview")

    # install; packages
    system("pip install pysimplegui")

    # make bash script on desktop to run main.py
    system("cp pyPreview.sh ~/Desktop")
    system("chmod +x ~/Desktop/pyPreview.sh")

    # system("clear")
    print("\nDone!\n")