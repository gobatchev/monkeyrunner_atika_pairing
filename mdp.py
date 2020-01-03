import sys

# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()

# Installs the Android package. Notice that this method returns a boolean, so you can test
# to see if the installation worked.
device.installPackage('/sdcard/test_monkeyRunner')

# sets a variable with the package's internal name
package = 'com.sagemcom.soundbox.vodabeta'

# sets a variable with the name of an Activity in the package
activity = 'com.sagemcom.soundbox.vodabeta.MainActivity'

# sets the name of the component to start
runComponent = package + '/' + activity





# Click on text box for wifiPasword
print( 'b' )
device.touch(489,826,'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(489,826,'DOWN_AND_UP')
MonkeyRunner.sleep(3)

print( 'c' )
# mot de passe wifi
#device.type('DDZJRJZJFTYYQG')
#device.type('6XXJ2L7DXUZLRS')
device.type('EVrbNuHk696n')
#device.touch(600,1050,'DOWN_AND_UP')
MonkeyRunner.sleep(5)

device.touch(540,1020,'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(540,1020,'DOWN_AND_UP')
MonkeyRunner.sleep(4)
