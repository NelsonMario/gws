from modules.AwsCli import AwsCli
from modules.Chocolatey import Chocolatey
from modules.Gsts import Gsts
from modules.Npm import Npm
from modules.Saml2Aws import Saml2Aws 
import subprocess

# Setup Command Class
class SetupCommand:
    def __call__(self):
        # Return available command in this class
        return {
            'prepare' : {
                'function': self.install,
                'description': 'Install all requirement module'
            },
            'tidy-up' : {
                'function': self.uninstall,
                'description': 'Uninstall existing module. Don\'t forget to remove chocolatey manually!'
            }
        }
    
    def __init__(self):
        self.chocolatey = Chocolatey()
        self.npm = Npm()
        self.awscli = AwsCli()
        self.saml2aws = Saml2Aws()
        self.gsts = Gsts()
    
    def install(self):
        # Install modules
        self.chocolatey.install()
        self.npm.install()
        self.awscli.install()
        self.saml2aws.install()
        self.gsts.install()
    
    def uninstall(self):
        # Uninstall modules
        subprocess.check_call(['RefreshEnv'], shell=True)
        self.npm.uninstall()
        self.awscli.uninstall()
        self.saml2aws.uninstall()
