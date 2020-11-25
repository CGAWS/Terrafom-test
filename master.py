import sys
from inputparser import *

import os

#should conver to singleton
GlobalParameters = {}   

def prod():
    print("setting up the environments as production\n")

def staging():
    print("setting up the environments as Staging\n")

def qa():
    print("setting up the environments as QA\n")

def uat():
    print("setting up the environments as UAT\n")

def dev():
    print("setting up the environments as DEV\n")

def infra():
    # this one will build whole aws infra
    print("\nTerraform bootstraping - setting whole infra on AWS ...\n")
    local('terraform init && terraform apply')

def up():
    infra()
    print("Init function to buld the environments\n")

def destroy():
    # destroys whole infra
    print(red("\n\nTerraform - destroying whole infra!!!\n"))
    if confirm(prompt='This will destroy whole env - are you sure?', resp=False):
        print("Destroying the environment")
        #local('cd %s && terraform init && terraform destroy' % env.ENV)

def compare():
    # compares files for prod and staging - shouldn't be significant differences except variables
    #local('diff -ENwbur -x "*.tfstate*" -x ".terraform" prod/ staging/')
    print("Comparing the environments")

# global functions
def confirm(prompt=None, resp=False):    
    if prompt is None:
        prompt = 'Confirm'

    if resp:
        prompt = '%s [%s]|%s: ' % (prompt, 'y', 'n')
    else:
        prompt = '%s [%s]|%s: ' % (prompt, 'n', 'y')
        
    while True:
        ans = raw_input(prompt)
        if not ans:
            return resp
        if ans not in ['y', 'Y', 'n', 'N']:
            print ("please enter y or n.")
            continue
        if ans == 'y' or ans == 'Y':
            return True
        if ans == 'n' or ans == 'N':
            return False


def orchestrate(argv):
    #print ('paramaters passed are: '+str(argv))
    print ("The orchestrator to create the infrastructure kicked off\n")
    if inputvalidation(argv) == False:
        print("Orchestrator has been halted as incorrect parameters have been passed")
        return False

    print("Setting the global parameters")
    GlobalParameters['env'] = str(argv[0]).lower()
    GlobalParameters['branch'] = str(argv[1]).lower()
    GlobalParameters['provision'] = str(argv[2]).lower()
    GlobalParameters['executionplan'] = str(argv[3]).lower()

    terraformcommand = ""
    print(GlobalParameters['executionplan'])
    
    if GlobalParameters.get('executionplan') == 'all':
        #call the original main.tf with modules included from all the files 
        #still to check the feasibility
        print("This is to execute all the components")
    elif GlobalParameters.get('executionplan') == 'component':
        #need to be changed the generic component based on the input 
        componentName = 'basenetwork'
        componentDirectory = './Modules/'+componentName
        print ("Company Directory is : "+componentDirectory)
        variableName = componentName+'/'+componentName+'_'+GlobalParameters['env']+'.tfvars'
        variableFileName= '../../Environments/'+GlobalParameters['env']+'/'+variableName
        print ("Variable Directory is : "+variableFileName)
        terraformcommand =  'cd %(1)s && terraform init && terraform validate && terraform apply --var-file %(2)s' % {"1" : componentDirectory, "2" : variableFileName}
        print ("Final terraformcommand to be executed is : "+terraformcommand)
        os.system(terraformcommand)
    else :
        print ("Wrong execution plan")
        


if __name__ == "__main__":
    orchestrate(sys.argv[1:])