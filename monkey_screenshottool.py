# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()

# sets a variable with the package's internal name
package = 'com.sagemcom.soundbox.vodabeta'

# sets a variable with the name of an Activity in the package
activity = 'com.sagemcom.soundbox.vodabeta.MainActivity'

# sets the name of the component to start
runComponent = package + '/' + activity

#   Test some issue 
#   # Write a friendly name
#   MonkeyRunner.sleep(3)
#   device.touch(489,646,'DOWN_AND_UP')
#   MonkeyRunner.sleep(1)
#   device.touch(489,646,'DOWN_AND_UP')
#   MonkeyRunner.sleep(1)
#   device.type('Wazaaaaa')
#   MonkeyRunner.sleep(1)
#   # Clic on Save
#   device.touch(540,1836,'DOWN_AND_UP')
#   MonkeyRunner.sleep(1)
#   device.touch(540,1836,'DOWN_AND_UP')
#   # Runs the component




# Takes a screenshot
result = device.takeSnapshot()
#how use get.SubImage(x,y,x_lengh,y_lengh)
sub_image = result.getSubImage((132,1227,816,148))
# Writes the screenshot to a file
sub_image.writeToFile("C:\Users\G603606\Rescan.png", "png")
#   a=device.getProperty("display.width")
#   b=device.getProperty("display.height")
#   print(a)
#   print(b)
