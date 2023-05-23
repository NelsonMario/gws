import subprocess
import sys
from validators.ModuleValidator import ModuleValidator
import credential

class Gsts(ModuleValidator):
    def install(self):
        # Check the module is already installed
        if self.check_module_installed('gsts'):
            print('gsts is already installed.')
            return
        try:
            # Installing the module if the module isn't installed
            print('Installing gsts...')
            subprocess.check_call(['RefreshEnv'], shell=True)
            subprocess.check_call(['npm', 'install', '-g', 'gsts@4.0.1'], shell=True)
            print('gsts installation completed.')
        except subprocess.CalledProcessError as e:
            print('Error occurred during gsts installation:', e)
            sys.exit(1)
            
    def login(self):
        # Make GSTS shortcut so the windows user just edit the credential from the ./constant/credential.py
        try:
            subprocess.call('gsts ' + '--aws-profile saml' + ' --idp-id ' + credential.GOOGLE_IDP_ID + ' --sp-id ' + credential.GOOGLE_SP_ID + ' --aws-region ' + credential.REGION, shell=True)
        except subprocess.CalledProcessError as e:
            print('Error occurred during login with gsts :', e)
            sys.exit(1)

