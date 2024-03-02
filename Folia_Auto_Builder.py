#This file builds Folia, Or Paper MC. Made for Folia.
#Requires git installed on terminal. Not in python.

# Requirements (IMPORTANT!)
# - git (terminal)
# - shutil (python)
#END OF Requirements

tempFolder='foliaGit'
# Name of folder to place github pull
MoveBuildToMainDir=True
# This moves build
DeletetempFolderTree=True
# Removes folder, uses shutil.
Build=False
# Skips build, just collects files.

import os, sys, time, shutil # Needed to access terminal
os.system('clear') # Clears terminal
current_directory = os.getcwd() #Does not get modified after intial value is set.
'''Directory At startup'''
print('Build Will Occur In:',current_directory)
Exit = False
while Exit == False:
    confirm=input('Confirm Action (y/n): ')
    if confirm.lower() in ['y', 'n']:
        Exit = True
if confirm == 'y': # Continue
    os.system('clear')
    print('-- Action Confirmed! --',
          '\nImporting Folia into folder:', tempFolder)
    if os.path.exists(tempFolder): # Check to see if folder exists.
        print('System: Folder Exists, Skipping creation.')
    else:
        os.system("mkdir '"+ str(tempFolder)+ "'")
    time.sleep(1) # Give time for user to read then clear.
    #commands=[[tempFolder, 1],['clear', 0], ['pwd', 0], ['Folia',1]] #Testing Commands
    commands=[[tempFolder, 1],['clear', 0], ['pwd', 0], ['git clone https://github.com/PaperMC/Folia', 0], ['Folia',1], ['./gradlew applyPatches', 0, Build], ['./gradlew createReobfBundlerJar', 0, Build]]
    # 0 = system command, 1 = chdir command.
    for i in range(len(commands)):
        try:
            (commands[i])[2] # Errors if doesn't exist.
            allowRun=(commands[i])[2]
            if allowRun == False:
                print('Skipping command:',i)
        except: allowRun=False
        if (commands[i])[1] == 0:
            if allowRun==True:
                os.system((commands[i])[0])
        else:
            os.chdir(str((commands[i])[0]))
    if MoveBuildToMainDir:
        os.chdir(str(os.getcwd()+'/build/libs'))
        files=(os.listdir())
        os.rename(files[0], 'Folia_Server.jar')
        buildNum=1
        checkedCurrentBuilds=False
        while checkedCurrentBuilds==False:
            file = str(current_directory+'/Folia_Server_#'+str(buildNum)+'.jar')
            if os.path.exists(file):
                buildNum+=1
            else:
                checkedCurrentBuilds=True
        os.replace(str(os.getcwd()+'/Folia_Server.jar'),current_directory+'/Folia_Server_#'+str(buildNum)+'.jar') 
        print('System: File has been placed at root directory from startup:', current_directory)
        os.chdir(current_directory)
        time.sleep(2)
        if DeletetempFolderTree==True:
            shutil.rmtree(tempFolder) # Clears all of tempFolder
            print('System: Build and Rm of temp folder has been completed. Closing Script.')
        else:
            print('System: Build has been completed. Closing Script.')
    else:
        build_Dir= str(os.getcwd()+'/build/libs')
        print('System: If build completed, it will be placed in: ',
            build_Dir)
    

else: # End App
    print("-- Action Cancelled! --")
    exit()