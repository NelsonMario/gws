from modules.Saml2Aws import Saml2Aws 
from modules.Gsts import Gsts
import subprocess

# Credential Command Class
class CredentialCommand:
    def __call__(self):
        # Return available command in this class
        return {
            'login' : {
                'function': self.login,
                'description': 'Login to aws through cli, It same like gsts'
            }
        }
    
    def __init__(self):
        self.saml2aws = Saml2Aws()
        self.gsts = Gsts()
    
    def login(self):
        # Login to AWS
        self.saml2aws.login()
        self.gsts.login()
        subprocess.check_call(['RefreshEnv'], shell=True)
