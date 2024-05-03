import subprocess
import os
import messages


while True:
    cont = messages.displaystartmessage()
    if cont.lower() != 'y':
        break
    print("Creation of virtual environment: ")
    # create_venv = subprocess.Popen("python -m venv testowevirtenv ", stdout=subprocess.PIPE, shell=True)
    create_venv = subprocess.Popen("python -m venv testowevirtenv5 ", shell=True)
    create_venv.wait()
    activate_script = r'.\testowevirtenv5\Scripts\activate'
    if os.path.exists(activate_script):
        print("[DONE]")
    print("Activation of virtual environment: ")
    subprocess.run(f'{activate_script} && python projektzaliczeniowy/usedjango.py', shell=True,
                   executable='C:\Windows\System32\cmd.exe')
    break
messages.displayendmessage()
input("Press enter to quit...")