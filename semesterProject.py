import Tkinter


#dia1: north and south straight, both can turn right but not left
#dia2: east and west can turn left, 
#dia3: north and South Trun left,
#dia4: east and west straight, both can turn right bot not left

print("Model 1: north and south straight, both can turn right but not left")
print("Model 2: east and west can turn left")
print("Model 3: north and South Turn left")
print("Model 4: east and west straight, both can turn right bot not left")
model = input("Enter Model Number: ")
northIn = input("enter inflow of traffic for North Side(vehicles/second): ")
southIn = input("enter inflow of traffic for South Side(vehicles/second): ")
eastIn = input("enter inflow of traffic for East Side(vehicles/second): ")
westIn = input("enter inflow of traffic for West Side(vehicles/second): ")

forwardMultiplier = .7
rightTurnMultiplier = .2
leftTurnMultiplier = .1
northOut = 0
southOut = 0
eastOut = 0
westOut = 0

if model == 1:
    northOut = southIn * forwardMultiplier
    southOut = northIn * forwardMultiplier
    eastOut = southIn * rightTurnMultiplier
    westOut = northIn * rightTurnMultiplier
elif model == 2:
    northOut = (westIn * leftTurnMultiplier) + (eastIn * rightTurnMultiplier)
    southOut = (eastIn * leftTurnMultiplier) + (westIn * rightTurnMultiplier)
    eastOut = southIn * rightTurnMultiplier
    westOut = northIn * rightTurnMultiplier
elif model == 3:
    northOut = westIn * rightTurnMultiplier
    southOut = eastIn * rightTurnMultiplier
    eastOut = (southIn * leftTurnMultiplier) + (northIn * rightTurnMultiplier)
    westOut = (northIn * leftTurnMultiplier) + (southIn * rightTurnMultiplier)
elif model == 4:
    northOut = eastIn * rightTurnMultiplier
    southOut = westIn * rightTurnMultiplier
    eastOut = westIn * forwardMultiplier
    westOut = eastIn * forwardMultiplier

print 'north outflow: ', northOut
print 'south outflow: ', southOut
print 'east outflow: ', eastOut
print 'west outflow: ', westOut
