# GWS

GSTS for Windows Shell

Provide command line to setup and run codebuild aggregator in CMD especially for windows user.

1. #### **Getting Started**

   Follow the steps below to get a working `gws` installation


   - Installing `python`
     Go [python](https://www.python.org/downloads/) web and download the latest version.
   - Open the installer and following the steps below

     - Choose customize installation and don't forget to checklist `add python.exe to PATH`
     - Then, click next
     - For final step, checklist `Install Python 3.11 for all users`
   - Validating `python`

     - Test the python command to makesure the python has been installed to your computer

     ```
     py --version
     ```
     or

     ```
     python3 --version
     ```
2. ### Configure the credential.py

   After install the python then,


   - Open `credential.py`
   - Set value for each value in `credential.py`. You can refer to this [document](https://29022131.atlassian.net/wiki/spaces/ENG/pages/2403074159/AWS+Single+Sign+On+-+How+to+assume+role+in+CLI+using+Google+SSO+SAML) or ask the engineer for help.
3. #### Run GWS Script

   Here is the command to use GWS:


   ```
   python3 gws.py <arg>
   ```
   `<arg>` can be replaced by:

   - `prepare`
     Initialize required module to run aggregator throught CLI. Make sure to running in **powershell with administrator mode**
     - notes:
       if you encountered this error, 

       ```
       Installing gsts...
       Refreshing environment variables from registry for cmd.exe. Please wait...Finished..
       'npm' is not recognized as an internal or external command,
       operable program or batch file.
       Error occurred during gsts installation: Command '['npm', 'install', '-g', 'gsts@4.0.1']' returned non-zero exit status 1.
       ```
       Don't worry, just run a **new powershell with administor mode** and running the same script
   - `tidy-up`
     Uninstall existing module. Mostly chocolatey are installed in `C:/ProgramData/chocolatey` and to uninstall it just remove the folder manually
   - `login`
     Login to aws through cli, It same like gsts
   - `add-aws-config`
     Add aws config to ~/.aws/config, but you can adding the config manually
   - `configure-saml2aws`
     Configure the email and password for the aws
4. ### Running Aggregator through CLI

   Here is [sheet](https://docs.google.com/spreadsheets/d/1qwVGdhWfVwiVBKryOwFpAtKjjuymrcSgyUMHNj-h98A/edit?usp=sharing) that generate aggregator command line for windows. Make sure if your email already listed in related role in AWS.
5. ### Feedback

   Please contact related engineer if there are a issues regarding of installation.
