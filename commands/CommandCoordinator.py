import os
from importlib import util
import inspect


# This class will coordinate all commands and validate if the arguments is doesn't collide with each other
class CommandCoordinator:
    def __init__(self):
        self.args_map = dict()
    
    def coordinate(self):
        # Current folder path
        folder_path = os.path.dirname(os.path.abspath(__file__))
        
        # Get the list of files in this folder
        file_list = [f for f in os.listdir(folder_path) if f.endswith('Command.py')]
        
        # Loop through the files        
        for file_name in file_list:
            # Remove the py extension to get the module name
            module_name = os.path.splitext(file_name)[0]

            # Construct the file path
            file_path = os.path.join(folder_path, file_name)
            
            # Load the module from the file
            spec = util.spec_from_file_location(module_name, file_path) 
            module = util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            for attribute_name, attribute in inspect.getmembers(module):
                # Load the main class only not the imported classes
                if inspect.isclass(attribute) and inspect.getmodule(attribute) is None:
                    main_class = getattr(module, attribute_name)
                    instance = main_class()
                    
                    # Get all args in loaded class
                    arguments = instance()
                    
                    for arg, func in arguments.items():
                        if arg in self.args_map:
                            raise Exception(f'[!] There is an duplicate argument -> {arg}')
                        self.args_map[arg] = {
                            'function': func['function'],
                            'description': func['description']
                        }
                    