import subprocess

class ModuleValidator:
    # Checking the module whether installed or not
    def check_module_installed(self, module_name):
        try:
            subprocess.check_call([module_name, '--version'], shell=True, stderr=subprocess.DEVNULL)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False
