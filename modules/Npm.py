import subprocess
import sys
from validators.ModuleValidator import ModuleValidator

class Npm(ModuleValidator):
    def install(self):
        # Check the module is already installed
        if self.check_module_installed('npm'):
            print('npm is already installed.')
            return
        try:
            # Installing the module if the module isn't installed
            print('Installing npm...')
            subprocess.check_call(['RefreshEnv'], shell=True)
            subprocess.check_call(['choco', 'install', 'nodejs.install'], shell=True)
            print('npm installation completed.')
        except subprocess.CalledProcessError as e:
            print('Error occurred during npm installation:', e)
            sys.exit(1)
            
    def uninstall(self):
        # Check the module is already installed
        if self.check_module_installed('npm'):
            try:
                # Uninstalling module if the module is already installed
                print('Uninstalling npm...')
                subprocess.check_call(['choco', 'uninstall', 'nodejs.install'], shell=True)
                print('npm uninstallation completed.')
            except subprocess.CalledProcessError as e:
                print('Error occurred during npm uninstallation:', e)
                sys.exit(1)
