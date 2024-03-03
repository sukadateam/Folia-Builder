# Folia/Paper-Builder
Automated Project Folia Builder. Easy to run and only 4 settings.

#Settings are as followed:
  - tempFolder='foliaGit' # Name of folder to place github pull
  - MoveBuildToMainDir=True # This moves built jar file to main dir.
  - DeletetempFolderTree=True # Removes tempFolder, uses shutil.
  - Build=True # Skips build, just collects files. MoveBuildToMainDir Does nothing if Build=False.
