from modules.Saml2Aws import Saml2Aws 
from modules.AwsCli import AwsCli

# Configuration Command Class
class ConfigCommand:
    def __call__(self):
        # Return available command in this class
        return {
            'configure-saml2aws': {
                'function': self.saml2aws.configure_saml2aws,
                'description': 'Configure the email and password for the aws'
            },
            'add-aws-config': {
                'function': self.awscli.add_aws_config,
                'description': 'Add aws config to ~/.aws/config, but you can adding the config manually'
            },
        }
        
    def __init__(self):
        self.saml2aws = Saml2Aws()
        self.awscli = AwsCli()

        
        
