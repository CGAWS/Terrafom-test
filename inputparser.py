#parse the input parameters and certify to invoke the proper terraform script base don environment
#environment 
#branch 


#Parses and orchestrates all the input validation necessary 
def inputvalidation(initiatorList) :

    #print ('Length of parameters : '+str(len(initiatorList)))
    if len(initiatorList) < 4:
        print("Pass the right parameters to the script:\n")
        print("Environment: dev, prod, qa, staging, uat \n")
        print("Branch: master\[Default\], valid branch from repository\n")
        print("Provision Type: NEW, FRESH, UPDATE")
        print('Execution Plan: ALL, COMPONENT')
        return False

    # We donot check the branch and can be incorporated with github API later
    if environmentverification(str(initiatorList[0])) == False:
        return False
    elif provisiontypeverification(str(initiatorList[2])) == False:
        return False
    elif executionplanverification(str(initiatorList[3])) == False:
        return False
    else:
        return True
    
   
#Checks the environments being passed as input to the script 
def environmentverification(Environment) :
    environment = Environment.lower()
    print ('Environment is : '+environment+'\n')
    if environment == 'dev':
        print("Environment passed is dev")
    elif environment == 'qa':
        print("Environment passed is qa")
    elif environment == 'uat':
        print("Environment passed is uat")
    elif environment == 'staging':
        print("Environment passed is staging")
    elif environment == 'prod':
        print("Environment passed is production")
    else :   
        print("Environment set is not available\n")
        print(" Abort the script")
        return False
    return True;

# Checks the provision type for the infrastructure 
def provisiontypeverification(ProvisionType):
    provisionType = ProvisionType.lower()
    print("Provision Type is : "+provisionType+"\n")
    returnvalue = False
    if provisionType == 'new' : 
        returnvalue = True
        print("The provision type is new")
    elif provisionType == 'fresh' : 
        returnvalue = True
        print("The provision type is fresh")
    elif provisionType == 'update':
        returnvalue = True
        print("The provision type is update")
    else:
        returnvalue = False
        print("The provision type passed is wrong")
    return returnvalue 

#Verify the execution plan
def executionplanverification(ExecutionPlan):
    executionPlan = ExecutionPlan.lower()
    print('Execution Plan is : '+executionPlan)
    returnvalue = False
    if executionPlan == 'all':
        returnvalue = True
    elif executionPlan == 'component':
        returnvalue = True
    else:
        returnvalue = False
    return returnvalue