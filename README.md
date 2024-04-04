# Folia/Paper-Builder
Automated Project Folia Builder. Easy to run and only 4 settings.

#Settings are as followed:
  - tempFolder='foliaGit' # Name of folder to place github pull
  - MoveBuildToMainDir=True # This moves built jar file to main dir.
  - DeletetempFolderTree=True # Removes tempFolder, uses shutil.
  - Build=True # Skips build, just collects files. MoveBuildToMainDir Does nothing if Build=False.


#The main goal for this script is to allow server hosts that use folia or paper, to automatically build and check for updates. Automation arguments will be implmented soon, these will be used on call of the script. EX: python Folia_Auto_Builder.py -b -f -r

Arguments will be as followed:
-     -b , --Build (Build) - Called First
-     -f , --Folia (Folia) - Following -b
-     -p , --Paper (Paper) - Following -b
-     -r , --Remove (Clean up after build)


Updates To script last commit:
  - 1) Added last commit date for each repo. Seen on startup.
