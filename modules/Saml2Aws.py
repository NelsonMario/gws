import subprocess
import sys
import credential
import getpass
from validators.ModuleValidator import ModuleValidator

class Saml2Aws(ModuleValidator):
    def install(self):
        # Check the module is already installed
        if self.check_module_installed('saml2aws'):
            print('saml2aws is already installed.')
            return
        try:
            #Installing the module if the module isn't installed
            print('Installing saml2aws...')
            subprocess.check_call(['RefreshEnv'], shell=True)
            subprocess.check_call(['choco', 'install', 'saml2aws'], shell=True)
            print('saml2aws installation completed.')
            self.configure_saml2aws()
        except subprocess.CalledProcessError as e:
            print('Error occurred during saml2aws installation:', e)
            sys.exit(1)
            
    def uninstall(self):
        # Check the module is already installed
        if self.check_module_installed('saml2aws'):
            try:
                #Uninstalling module if the module is already installed
                print('Uninstalling saml2aws...')
                subprocess.check_call(['RefreshEnv'], shell=True)
                subprocess.check_call(['choco', 'uninstall', 'saml2aws'], shell=True)
                print('saml2aws uninstallation completed.')
            except subprocess.CalledProcessError as e:
                print('Error occurred during saml2aws uninstallation:', e)
                sys.exit(1)

    def configure_saml2aws(self):
        # Configure saml2aws through CLI with one command
        print('Configuring saml2aws...')
        email = credential.EMAIL
        password = getpass.getpass('Input password for ' + email + ' : ')
        url = credential.URL

        try:
            subprocess.check_call(['saml2aws', 'configure', '--idp-provider=GoogleApps', 
                                f'--url={url}', '--profile=saml', 
                                f'--username={email}', 
                                f'--password={password}'])
            print('saml2aws configuration completed.')
        except subprocess.CalledProcessError as e:
            print('Error occurred during saml2aws configuration:', e)
            sys.exit(1)
            
    def login(self):
        # Login aws to create credential at ~/.aws/credential
        print('Configuring saml2aws...')
        try:
            subprocess.check_call(['saml2aws', 'login'])
            print('saml2aws login completed.')
        except subprocess.CalledProcessError as e:
            print('Error occurred during saml2aws configuration:', e)
            sys.exit(1)
