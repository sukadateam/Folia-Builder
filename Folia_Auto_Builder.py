#This file builds Folia, Or Paper MC. Made for Folia.
#Requires git installed on terminal. Not in python.

# -- subprocess is used in this script for terminal returns --
# Requirements (IMPORTANT!)
# - git (terminal)
# - shutil (python)
# - JDK 17 - (java)
#END OF Requirements

tempFolder='buildGit'
# Name of folder to place github pull
MoveBuildToMainDir=True
# This moves build
DeletetempFolderTree=True
# Removes folder, uses shutil.
Build=True
# Skips build, just collects files. MoveBuildToMainDir Does nothing if Build=False.

import os, sys, time, shutil, subprocess # Needed to access terminal
os.system('clear') # Clears terminal
os.chdir(str(os.getcwd()+'/Desktop'))
current_directory = os.getcwd() #Does not get modified after intial value is set.
'''Directory At startup'''
while True:
    os.system('clear')
    print('Build Will Occur In:',current_directory)
    buildType=input('What are we building?\n1 - (Folia)\n2 - (PaperMC)\n3 - (Change Directory)\nYour choice: ')
    '''1 - Folia, 2 - PaperMC'''
    if buildType in ['1', '2']:
        break
    if buildType=='3':
        finished=False
        clearScreen=True
        while finished==False:
            if clearScreen == True:
                os.system('clear')
            clearScreen=True # Resets back to True, just incase it's still false.
            current_directory = os.getcwd()
            print('Current Directory:',current_directory)
            print('ls - lists all in current dir',
                  '\nback - Goes back 1 folder',
                  '\nreturn - Go back to build')
            output=input('Input new directory: ')
            if output=='back':
                c=len(current_directory)
                a = c
                for i in range(c):
                    if current_directory[a-1] == "/":
                        try:
                            os.chdir(str(current_directory[0:a-1]))
                        except:
                            os.system('clear')
                            print('Not recommended to go beyond users.')
                            clearScreen=False
                    else:
                        a-=1
            elif output=='ls':
                #os.system('clear')
                x = subprocess.check_output(['ls'])
                x = x.decode()
                xlist=[]
                a, b = 0, 0
                for i in range(len(x)):
                    if x[i] == '\n':
                        xlist.append(x[a:b])
                        a = b; b = a+1
                    else:
                        b+=1
                xlist[0]='\n'+xlist[0] # Fixes the first entry not being a valid file/folder
                print(xlist)
                for i in range(len(xlist)):
                    print(('('+str(i)+') - '+str((xlist[i])[1:len(xlist[i])])))
                totalEntryC=len(xlist) # Total amount of files/folders
                output = input('Enter Number to select: ')
                if int(output) <= totalEntryC-1:
                    if int(output) > -1:
                        choice = int(output); changedir = (str((xlist[choice])[1:len(xlist[choice])])); os.chdir(changedir)
                    else:
                        print('Invalid Number: Less than expected.')
                else:
                    print('Invalid Number: Bigger than expected.')
            elif output=='return':
                break
            else:
                try: os.chdir(output)
                except: print('Invalid Change!')
Exit = False
while Exit == False:
    if input('Confirm Action (y/n): ').lower() == "y":
        Exit = 'y' # Redefine Exit
if Exit == 'y': # Continue
    os.system('clear')
    print('-- Action Confirmed! --',
          '\nImporting Folia/or/Paper into folder:', tempFolder)
    if os.path.exists(tempFolder): # Check to see if folder exists.
        print('System: Folder Exists, Removing Tree')
        shutil.rmtree(tempFolder)
    os.system("mkdir '"+ str(tempFolder)+ "'")
    time.sleep(1) # Give time for user to read then clear.
    #commands=[[tempFolder, 1],['clear', 0], ['pwd', 0], ['Folia',1]] #Testing Commands
    commands=[[tempFolder, 1],['clear', 0], ['pwd', 0], ['git clone https://github.com/PaperMC/Folia', 0], ['Folia',1], ['./gradlew applyPatches', 0, Build], ['./gradlew createReobfBundlerJar', 0, Build]]
    if buildType=='2': # Changes what we are bulding.
        (commands[3])[0]='git clone https://github.com/PaperMC/Paper'
        (commands[4])[0]='Paper'
    # 0 = system command, 1 = chdir command.
    for i in range(len(commands)):
        try:
            (commands[i])[2] # Errors if doesn't exist.
            allowRun=(commands[i])[2]
            if allowRun == False:
                print('Skipping command:',i)
        except: allowRun=True
        if (commands[i])[1] == 0:
            if allowRun==True:
                os.system((commands[i])[0])
        else:
            os.chdir(str((commands[i])[0]))
    if MoveBuildToMainDir:
        if Build==True:
            os.chdir(str(os.getcwd()+'/build/libs'))
            files=(os.listdir())
            if buildType=='2':
                os.rename(files[0], 'Paper_Server.jar')
            else:
                os.rename(files[0], 'Folia_Server.jar')
            buildNum=1
            checkedCurrentBuilds=False
            while checkedCurrentBuilds==False:
                if buildType=='2':
                    file = str(current_directory+'/Paper_Server_#'+str(buildNum)+'.jar')
                else:
                    file = str(current_directory+'/Folia_Server_#'+str(buildNum)+'.jar')
                if os.path.exists(file):
                    buildNum+=1
                else:
                    checkedCurrentBuilds=True
            if buildType=='2':
                os.replace(str(os.getcwd()+'/Paper_Server.jar'),current_directory+'/Paper_Server_#'+str(buildNum)+'.jar') 
            else:
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
