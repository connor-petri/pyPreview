from os import system

if __name__ == "__main__":
  system('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
  system("pip3 install pysimplegui")
  system("brew install tcl-tk")
  system("clear")
  print("\nDone!\n")
