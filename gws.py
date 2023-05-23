import sys
import argparse
from commands.CommandCoordinator import CommandCoordinator

class Main:
    def __init__(self):
        # Check the system platform or OS 
        if sys.platform != 'win32':
            print('[!] Chocolatey, awscli, npm, gsts, and saml2aws can only be installed on Windows.')
            return
        
        # Call Command Coordinator
        command_coordinator = CommandCoordinator()
        command_coordinator.coordinate()
        
        # Create the parser
        parser = argparse.ArgumentParser(description= 'GWS is script which make windows user can use AWS easier')
        subparser = parser.add_subparsers(dest='command', help='[!] Available command :')
        
        # Add the arguments with the multiple opt
        for opt, config in command_coordinator.args_map.items():
            subparser.add_parser(opt, help=config['description'])
        
        # Parse the arguments
        args = parser.parse_args()
        
        # Get selected command
        selected_command = command_coordinator.args_map[args.command]['function']
        
        # Execute the selected function
        selected_command()
        

if __name__ == '__main__':
    Main()

