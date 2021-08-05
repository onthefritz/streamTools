import sys
import os
import json

settings = {}

# Gets the parameter if it exists. Otherwise return None
# parameterToGet = parameter needed to be obtained.
def getParameter(parameterToGet):
    # check the total number of records in the args.
    if len(sys.argv) >= parameterToGet + 1:
        return sys.argv[parameterToGet]
    else:
        return None

# Updates Multiplier setting for the app.
def updateMultiplierSetting(multiplierValue):
    # get the current directory of this file. 
    cwd = os.path.dirname(os.path.realpath(__file__))

    # read current settings file
    with open(cwd + '/appsettings.json', 'r') as f:
        data = f.read()

    f.close()

    current_settings = json.loads(data)
    current_settings["multiplier"] = multiplierValue

    # overwrite what is in the file with the new total
    with open(cwd + '/appsettings.json', 'w') as f:
        f.write(json.dumps(current_settings))

    f.close()

# Loads settings for the app.
def loadSettings():
    # get the current directory of this file. 
    cwd = os.path.dirname(os.path.realpath(__file__))

    # read current settings file
    with open(cwd + '/appsettings.json', 'r') as f:
        data = f.read()

    f.close()

    global settings
    settings = json.loads(data)

# Edits the points file to increase but the amount passed in.
# increaseBy = points to increase by
def editFile(increaseBy):
    # get the current directory of this file. 
    cwd = os.path.dirname(os.path.realpath(__file__))

    # read what is currently in the file
    with open(cwd + '/data/points.txt', 'r') as f:
        data = f.read()

    f.close()

    # overwrite what is in the file with the new total
    with open(cwd + '/data/points.txt', 'w') as f:
        f.write(str(int(data) + int(increaseBy)))

    f.close()

# Gets the multiplier of points by the tier at which the subs are at.
# tier = the tier of the subs
def getMultiplier(tier):
    global settings

    if tier.lower() == "tier 1":
        return int(settings["tier1Multiplier"])
    elif tier.lower() == "tier 2":
        return int(settings["tier2Multiplier"])
    elif tier.lower() == "tier 3":
        return int(settings["tier3Multiplier"])

    return 1

# Gets the points to increase the file by.
# alertType = the type of alert. 
#   1 = sub (or single gifted sub)
#   2 = more than 1 gift sub
#   3 = cheer
# amount = the amount of the alert. (number of bits / subs)
# tier = the tier of the subs
def getPoints(alertType, amount, tier):
    global settings

    # sub or gift subs
    if alertType == 1 or alertType == 2:
        return (amount * getMultiplier(tier)) * settings["multiplier"]
    # cheer
    elif alertType == 3:
        return int(amount / int(settings["bitsPerPoint"])) * settings["multiplier"]

    # something went wrong so don't increase the count
    return 0

# get the parameters passed into the app.
firstArg = int(getParameter(1))
secondArg = int(getParameter(2))
thirdArg = getParameter(3)

if firstArg == 0:
    updateMultiplierSetting(secondArg)
else:
    # load settings
    loadSettings()
    # get the number of points
    pointsToAdd = getPoints(firstArg, secondArg, thirdArg)
    # edit the file being used to hold the number of points.
    editFile(pointsToAdd)