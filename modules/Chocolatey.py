import subprocess
import sys
from validators.ModuleValidator import ModuleValidator

class Chocolatey(ModuleValidator):
    def install(self):
        # Check the module is already installed
        if self.check_module_installed('choco'):
            print('choco is already installed.')
            return
        try:
            # Installing the module if the module isn't installed
            print('Installing Chocolatey...')
            subprocess.check_call(['powershell.exe', '-Command', '(New-Object System.Net.WebClient).DownloadFile(\'https://chocolatey.org/install.ps1', 'install_choco.ps1\')'], shell=True)
            subprocess.check_call(['powershell.exe', '-Command', '& {Set-ExecutionPolicy Bypass -Scope Process -Force; ./install_choco.ps1}'], shell=True)
            print('Chocolatey installation completed.')
        except subprocess.CalledProcessError as e:
            print('Error occurred during Chocolatey installation:', e)
            sys.exit(1)
