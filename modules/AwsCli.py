import subprocess
import sys
import os
import re
import credential
from validators.ModuleValidator import ModuleValidator

class AwsCli(ModuleValidator):
    def install(self):
        # Check the module is already installed
        if self.check_module_installed('aws'):
            print('awscli is already installed.')
            return
        try:
            # Installing module if the module isn't installed
            print('Installing awscli...')
            subprocess.check_call(['RefreshEnv'], shell=True)
            subprocess.check_call(['choco', 'install', 'awscli', '--version=1.27.134'], shell=True)
            print('awscli installation completed.')
        except subprocess.CalledProcessError as e:
            print('Error occurred during awscli installation:', e)
            sys.exit(1)
        
        # Initialize the aws config when first installment
        self.generate_aws_config()
        self.add_aws_config()
        
    def uninstall(self):
        # Check the module is already installed
        if self.check_module_installed('aws'):
            try:
                # Uninstalling module if the module is already installed
                print('Uninstalling awscli...')
                subprocess.check_call(['RefreshEnv'], shell=True)
                subprocess.check_call(['choco', 'uninstall', 'awscli', '--version=1.27.134'], shell=True)
                print('awscli uninstallation completed.')
            except subprocess.CalledProcessError as e:
                print('Error occurred during awscli uninstallation:', e)
                sys.exit(1)
            
    def generate_aws_config(self):
        # Creating the ~/.aws/config
        print('Generating AWS configuration...')
        email = credential.EMAIL
        
        root_path = os.path.expanduser('~')
        
        # Some windows has ~ as their user home directory
        if root_path[0] != 'C':
            root_path = os.path.expanduser('%USERPROFILE%')
            
        aws_folder_path = os.path.join(root_path, '.aws')
        config_file_path = os.path.join(aws_folder_path, 'config')

        # AWS configuration content
        config_content = \
        f"""
    [profile saml]
    region = ap-southeast-1
    output = json
    google_config.role_arn = arn:aws:iam::811468751499:role/SAMLUser
    google_config.provider = arn:aws:iam::811468751499:saml-provider/GoogleApps
    google_config.google_idp_id = {credential.GOOGLE_IDP_ID}
    google_config.google_sp_id = {credential.GOOGLE_SP_ID}
    google_config.google_username = {email}
    google_config.duration = 3600
    google_config.ask_role = False
    google_config.u2f_disabled = True
        """ + os.linesep
        
        # Create .aws folder if it doesn't exist
        if not os.path.exists(aws_folder_path):
            os.makedirs(aws_folder_path)

        # Write config content to the config file
        with open(config_file_path, 'w') as config_file:
            config_file.write(config_content)

        print(f'AWS configuration generated and saved at: {config_file_path}')
        
    def add_aws_config(self): 
        # Add configuration for aws user or role
        print('Adding AWS configuration...')
        
        profile_name = input('Input profile name (ex: flBusinessAnalyst:tvlk-eci-stg) : ')
        email = credential.EMAIL
        account_id = input('Input your account_id : ')
        role_name = input('Input role name (flBusinessAnalyst) : ')
        
        
        if profile_name == None or email == None or account_id == None or role_name == None or not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email) :
            print('Error occurred when adding aws config')
            sys.exit(1)
        
        root_path = os.path.expanduser('~')
        
        # Some windows has ~ as their user home directory
        if root_path[0] != 'C':
            root_path = os.path.expanduser('%USERPROFILE%')
            
        aws_folder_path = os.path.join(root_path, '.aws')
        config_file_path = os.path.join(aws_folder_path, 'config')

        # AWS configuration content
        additional_config_content = \
        f"""
    [profile {profile_name}]
    role_arn = arn:aws:iam::{account_id}:role/{role_name}
    source_profile = saml
    role_session_name = {email.split('@')[0]}
    region = ap-southeast-1
        """ + os.linesep
    
    
        # Create .aws folder if it doesn't exist
        if not os.path.exists(aws_folder_path):
            os.makedirs(aws_folder_path)

        # Write config content to the config file
        with open(config_file_path, 'a') as config_file:
            config_file.write(additional_config_content)

        print(f'AWS configuration added and saved at: {config_file_path}')

