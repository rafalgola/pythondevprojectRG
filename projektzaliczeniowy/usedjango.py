import subprocess
import time


def find_django_processes():
    """This function checks processes running in cli started with manage.py"""
    django_procs = []
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        if proc.info['cmdline'] and 'manage.py' in ' '.join(proc.info['cmdline']) and 'runserver' in ' '.join(
                proc.info['cmdline']):
            django_procs.append(proc)
    return django_procs


def stop_django_processes():
    """This function stops all django server processes"""
    django_procs = find_django_processes()
    for proc in django_procs:
        proc.kill()


print("[DONE]")
print("Required packages will be installed to virtual environment. This may take some time. Summary will be displayed.")
install_packages = subprocess.Popen("pip install -r requirements.txt", stdout=subprocess.PIPE, shell=True)
(result, err) = install_packages.communicate()
install_packages.wait()
if not err:
    print(result.decode('utf-8'))

print("\nStarting django server.")
run_server = subprocess.Popen("python projektzaliczeniowy\manage.py runserver",
                              stdout=subprocess.PIPE, shell=True)
time.sleep(5)

subprocess.run("python projektzaliczeniowy/project.py", shell=True,
               executable='C:\Windows\System32\cmd.exe')

import psutil

print("Stopping all django server processes.")
stop_django_processes()

