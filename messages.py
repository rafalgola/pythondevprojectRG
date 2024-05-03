def displaystartmessage():
    print("-" * 80)
    print("| %s |" % "This is Rafal's final project for postgraduate 'Python Developer' studies. ".center(76))
    print("| %s |" % "Following operations will take be performed:".center(76))
    print("| %s |" % "1. Creating virtual environment".center(76))
    print("| %s |" % "2. Activating virtual environment".center(76))
    print("| %s |" % "3. Installing the required packages".center(76))
    print("| %s |" % "4. Starting django server offering api with PESEL validator".center(76))
    print("| %s |" % "5. Getting PESEL numbers from online generator using Selenium and saving to".center(76))
    print("| %s |" % "   .csv. Make sure to have proper chromedriver.exe in projektzaliczeniowy".center(76))
    print("| %s |" % "   directory ( subdirectory of project directory ) or in your os PATH".center(76))
    print("| %s |" % "6. Assert for randomly chosen PESEl from .csv file and reply from validator".center(76))

    print("|", " " * 66, "-" * 11)
    print("| %s |" % "Be warned: it will take some time to complete run of this project".center(66), "Proceed?")
    cont = input("{prompt}   Y/n? ".format(prompt='-' * 70))
    return cont


def displayendmessage():
    print("That'a all Folks!")
    return None
