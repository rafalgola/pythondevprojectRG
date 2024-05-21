import subprocess
import os


def display_start_message():
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
    # cont = input("{prompt}   Y/n? ".format(prompt='-' * 70))
    cont = 'Y'
    return cont


def prepare_virtual_env():
    print("Creation of virtual environment: ")
    create_venv = subprocess.Popen("python -m venv virtenv", shell=True)
    create_venv.wait()
    activate_script = r'.\virtenv\Scripts\activate'
    if os.path.exists(activate_script):
        print("[DONE]")


def activate_virtual_env_and_perform_logic():
    print("Activation of virtual environment: ")
    activate_script = r'.\virtenv\Scripts\activate'
    subprocess.run(f'{activate_script} && python projektzaliczeniowy/usedjango.py', shell=True,
                   executable='C:\Windows\System32\cmd.exe')


def main():
    cont = display_start_message()
    if cont.lower() == 'y':
        prepare_virtual_env()
        activate_virtual_env_and_perform_logic()
    else:
        print("Your choose not to proceed...")
    input("Press enter to quit...")


if __name__ == '__main__':
    main()
