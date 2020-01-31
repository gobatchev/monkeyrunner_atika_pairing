import sys
import os
import time
import datetime

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

# Runs the component
device.startActivity(component=runComponent)


WIDTH_PHONE = float(device.getProperty("display.width"))
HEIGHT_PHONE = float(device.getProperty("display.height"))

for s in range(0,9):
   amazon_not_fully_connected = False
   date = str(datetime.datetime.now().strftime("%Y-%m-%d-%Hh-%Mmin")) 
   path = '/mnt/c/Users/G603606/Results_MonkeyRunner'
   
   # Wait boot apk screen
   MonkeyRunner.sleep(5)
   # Click on add a speaker
   device.touch(750./1080*WIDTH_PHONE,390./2032*HEIGHT_PHONE,'DOWN_AND_UP')
   MonkeyRunner.sleep(1)
   # Click on Continue 5 times to skip the tutorial
   for i in range(1,5):
      device.touch(500./1080*WIDTH_PHONE,1870./2032*HEIGHT_PHONE, 'DOWN_AND_UP') 
      MonkeyRunner.sleep(1)
   
   # Wait if the SB logo appears 
   # MonkeyRunner.sleep(8)
   
   
   #------------------USELESS NOW--------------------------------------------------------------
   # Test connection 10 times plus 1 more for the first try
   
   # while (value == True and i < 11) :
   #    newimage = device.takeSnapshot()
   #    reference = MonkeyRunner.loadImageFromFile('C:\\Users\\G603606\\retry_scan.png')
   #    value =  MonkeyImage.sameAs( newimage, reference, 0.9 )
   #    if i > 0 :
   #       print('Error, screen re-scan appears, loop ' + str(i))
   # 
   #    device.touch(500./1080*WIDTH_PHONE,./2032*HEIGHT_PHONE 1300, 'DOWN_AND_UP')
   #    MonkeyRunner.sleep(5)
   #    i = i + 1
   #------------------USELESS NOW--------------------------------------------------------------
   
   # if not sub_image.sameAs(reference, 0.9):
   #            print "Images do not match!"
   #                   # do something
   
   
   value = False
   i = 0
   a = time.time()
   # Check if the SB logo appears 
   # maximum 45s
   while (value == False and i < 45) :
      i = time.time() - a
      newimage = device.takeSnapshot()
      sub_image = newimage.getSubImage((300./1080*WIDTH_PHONE,806./2032*HEIGHT_PHONE,480./1080*WIDTH_PHONE,480./2032*HEIGHT_PHONE))
      reference = MonkeyRunner.loadImageFromFile('C:\\Users\\G603606\\SB_compare.png')
      value =  MonkeyImage.sameAs( sub_image, reference, 0.8 )
      print(i)
   
   if not value :
      print('Atika not found')
      # Take a screenshot
      result = device.takeSnapshot()
      # Write the screenshot to a file
      #result.writeToFile( path + '/lost_SB_logo_level.png','png')
      result.writeToFile('C:\Users\G603606\Results_MonkeyRunner\lost_SB_logo_level' + date + '.png','png')
      # quit properly the monkeyrunner
      signal.signal(signal.SIGINT, signal.getsignal(signal.SIGINT))
      device.shell('killall com.android.commands.monkey')
      sys.exit()
   
      
   # device.drag((152,1496),(929,1640), 1, 1)
   device.touch(540./1080*WIDTH_PHONE,1568./2032*HEIGHT_PHONE,'DOWN_AND_UP')
   
   
   value = False
   i = 0
   a = time.time()
   # Check if we reach connexion wifi screen
   # maximum 16s
   while (value == False and i < 45) :
      i = time.time() - a
      newimage = device.takeSnapshot()
      sub_image = newimage.getSubImage((102./1080*WIDTH_PHONE,946./2032*HEIGHT_PHONE,876./1080*WIDTH_PHONE,148./2032*HEIGHT_PHONE))
      reference = MonkeyRunner.loadImageFromFile('C:\\Users\\G603606\\connexion_wifi_textbox.png')
      value =  MonkeyImage.sameAs( sub_image, reference, 0.8 )
      print(i)
       
   if not value :
      print('No connexion button found')
      # Takes a screenshot
      result = device.takeSnapshot()
      # Writes the screenshot to a file
      result.writeToFile('C:\Users\G603606\Results_MonkeyRunner\lost_connexion_wifi_textbox ' + date + '.png','png')
      # quit properly the monkeyrunner
      signal.signal(signal.SIGINT, signal.getsignal(signal.SIGINT))
      device.shell('killall com.android.commands.monkey')
      sys.exit()
       
   #------------------USELESS NOW--------------------------------------------------------------
   #   newimage = device.takeSnapshot()
   #   sub_image = newimage.getSubImage((300./1080*WIDTH_PHONE,806./2032*HEIGHT_PHONE,480./1080*WIDTH_PHONE,480./2032*HEIGHT_PHONE))
   #   reference = MonkeyRunner.loadImageFromFile('C:\\Users\\G603606\\wifi_selction_menu.png')
   #   #    Petites notes pour taper les mdp reseau
   #   #    device.touch(x, y, MonkeyDevice.DOWN_AND_UP)
   #   #    MonkeyRunner.sleep(1)
   #   #    device.type('USER')
   #------------------USELESS NOW--------------------------------------------------------------
   
   
   
   # Click on text box for wifiPasword
   device.touch(489./1080*WIDTH_PHONE,826./2032*HEIGHT_PHONE,'DOWN_AND_UP')
   MonkeyRunner.sleep(1)
   device.touch(489./1080*WIDTH_PHONE,826./2032*HEIGHT_PHONE,'DOWN_AND_UP')
   MonkeyRunner.sleep(1)
   
   # wifi password
   # vodafone90F0
   # device.type('6XXJ2L7DXUZLRS')
   # ONO6447 
   # device.type('EVrbNuHk696n')
   # VodafoneB269
   # device.type('UMDPIUGBQ9TWS2')
   # vodafone42AO --rooter access DWMYJMNL --
   device.type('DDZJRJZJFTYYQG')
   
   
   MonkeyRunner.sleep(1)
   
   # Valid pswd
   device.touch(540./1080*WIDTH_PHONE,1020./2032*HEIGHT_PHONE,'DOWN_AND_UP')
   MonkeyRunner.sleep(1)
   device.touch(540./1080*WIDTH_PHONE,1020./2032*HEIGHT_PHONE,'DOWN_AND_UP')
   MonkeyRunner.sleep(1)
   
   value = False
   i = 0
   a = time.time()
   while (value == False and i < 45) :
      i = time.time() - a
      newimage = device.takeSnapshot()
      sub_image = newimage.getSubImage((48./1080*WIDTH_PHONE,116./2032*HEIGHT_PHONE,984./1080*WIDTH_PHONE,81./2032*HEIGHT_PHONE))
      reference = MonkeyRunner.loadImageFromFile('C:\\Users\\G603606\\friendly_name.png')
      value =  MonkeyImage.sameAs( sub_image, reference, 1 )
      print(i)
       
   if not value :
      print('Firendly name menu issue')
      # Takes a screenshot
      result = device.takeSnapshot()
      # Writes the screenshot to a file
      result.writeToFile('C:\Users\G603606\Results_MonkeyRunner\lost_friendly_name' + date + '.png','png')
      # quit properly the monkeyrunner
      signal.signal(signal.SIGINT, signal.getsignal(signal.SIGINT))
      device.shell('killall com.android.commands.monkey')
      sys.exit()
   
   # Write a friendly name
   MonkeyRunner.sleep(2)
   #   device.drag((480,646),(489,646), 1, 1)
   #   MonkeyRunner.sleep(5)
   #   device.touch(489./1080*WIDTH_PHONE,646./2032*HEIGHT_PHONE,'DOWN_AND_UP')
   #   MonkeyRunner.sleep(2)
   device.touch(489./1080*WIDTH_PHONE,646./2032*HEIGHT_PHONE,'DOWN_AND_UP')
   MonkeyRunner.sleep(2)
   #   device.touch(489./1080*WIDTH_PHONE,646./2032*HEIGHT_PHONE,'DOWN_AND_UP')
   #   MonkeyRunner.sleep(2)
   device.type(date)
   #   MonkeyRunner.sleep(2)
   # Clic on Save
   device.touch(540./1080*WIDTH_PHONE,1836./2032*HEIGHT_PHONE,'DOWN_AND_UP')
   print('touch action')
   MonkeyRunner.sleep(1)
   device.touch(540./1080*WIDTH_PHONE,1836./2032*HEIGHT_PHONE,'DOWN_AND_UP')
   print('touch action2')
   
   # Wait no_update_available screen
   # -------------------------------------------
   # -------------------------------------------
   # -------------------------------------------
   # -------------------------------------------
   # /!\ case with update TO DO
   # -------------------------------------------
   # -------------------------------------------
   # -------------------------------------------
   # -------------------------------------------
   value = False
   i = 0
   a = time.time()
   while (value == False and i < 20) :
      i = time.time() - a
      newimage = device.takeSnapshot()
      sub_image = newimage.getSubImage((132./1080*WIDTH_PHONE,888./2032*HEIGHT_PHONE,816./1080*WIDTH_PHONE,130./2032*HEIGHT_PHONE))
      reference = MonkeyRunner.loadImageFromFile('C:\\Users\\G603606\\no_update_available.png')
      value =  MonkeyImage.sameAs( sub_image, reference, 0.8 )
      print(i)
   
   if not value :
      print('No update menu issue')
      # Takes a screenshot
      result = device.takeSnapshot()
      # Writes the screenshot to a file
      result.writeToFile('C:\Users\G603606\Results_MonkeyRunner\lost_no_update_available' + date + '.png','png')
      # quit properly the monkeyrunner
      signal.signal(signal.SIGINT, signal.getsignal(signal.SIGINT))
      device.shell('killall com.android.commands.monkey')
      sys.exit()
   
   device.touch(540./1080*WIDTH_PHONE,1236./2032*HEIGHT_PHONE,'DOWN_AND_UP')
   print('touch continuer')
   
   # Amazon Section
   value = False
   i = 0
   a = time.time()
   while (value == False and i < 20) :
      i = time.time() - a
      newimage = device.takeSnapshot()
      sub_image = newimage.getSubImage((84./1080*WIDTH_PHONE,843./2032*HEIGHT_PHONE,912./1080*WIDTH_PHONE,178./2032*HEIGHT_PHONE))
      reference = MonkeyRunner.loadImageFromFile('C:\\Users\\G603606\\AmazonTextMenu.png')
      value =  MonkeyImage.sameAs( sub_image, reference, 0.8 )
      print(i)
   
   if not value :
      print('Amazon menu issue')
      # Takes a screenshot
      result = device.takeSnapshot()
      # Writes the screenshot to a file
      result.writeToFile('C:\Users\G603606\Results_MonkeyRunner\Amazon_menu_issue' + date + '.png','png')
      # quit properly the monkeyrunner
      signal.signal(signal.SIGINT, signal.getsignal(signal.SIGINT))
      device.shell('killall com.android.commands.monkey')
      sys.exit()
   
   device.touch(540./1080*WIDTH_PHONE,1777./2032*HEIGHT_PHONE,'DOWN_AND_UP')
   print('touch Connexion amazon')
   
   MonkeyRunner.sleep(1)
   
   # Amazon Section end
   value = False
   i = 0
   a = time.time()
   while (value == False and i < 20) :
      i = time.time() - a
      newimage = device.takeSnapshot()
      sub_image = newimage.getSubImage((838./1080*WIDTH_PHONE,127./2032*HEIGHT_PHONE,194./1080*WIDTH_PHONE,58./2032*HEIGHT_PHONE))
      reference = MonkeyRunner.loadImageFromFile('C:\\Users\\G603606\\terminer_button_amazon.png')
      value =  MonkeyImage.sameAs( sub_image, reference, 0.8 )
      print(i)
   
   if not value :
      print('Amazon menu end issue ')
      # Takes a screenshot
      result = device.takeSnapshot()
      # Writes the screenshot to a file
      result.writeToFile('C:\Users\G603606\Results_MonkeyRunner\Amazon_menu_issue_end' + date + '.png','png')
      # quit properly the monkeyrunner
      signal.signal(signal.SIGINT, signal.getsignal(signal.SIGINT))
      device.shell('killall com.android.commands.monkey')
      sys.exit()
   
   device.touch(540./1080*WIDTH_PHONE,1699./2032*HEIGHT_PHONE,'DOWN_AND_UP')
   print('touch terminer amazon')
   MonkeyRunner.sleep(1)
   
   
   # Click on Continue 2 times to skip the tutorial
   for i in range(0,2):
      device.touch(500./1080*WIDTH_PHONE,1870./2032*HEIGHT_PHONE, 'DOWN_AND_UP') 
      MonkeyRunner.sleep(1)
   
   
   # Menu SB section
   value = False
   i = 0
   a = time.time()
   while (value == False and i < 20) :
      i = time.time() - a
      newimage = device.takeSnapshot()
      sub_image = newimage.getSubImage((106, 410, 144, 288))
      reference = MonkeyRunner.loadImageFromFile('C:\\Users\\G603606\\sb_name_menu.png')
      value =  MonkeyImage.sameAs( sub_image, reference, 0.8 )
      print(i)
   
   if not value :
      print('sb name menu issue ')
      # Takes a screenshot
      result = device.takeSnapshot()
      # Writes the screenshot to a file
      result.writeToFile('C:\Users\G603606\Results_MonkeyRunner\sb_name_menu_issue' + date + '.png','png')
      # quit properly the monkeyrunner
      signal.signal(signal.SIGINT, signal.getsignal(signal.SIGINT))
      device.shell('killall com.android.commands.monkey')
      sys.exit()
   
   device.touch(540./1080*WIDTH_PHONE,333./2032*HEIGHT_PHONE,'DOWN_AND_UP')
   print('touch SB name')
   MonkeyRunner.sleep(1)
   
   
   # Menu SB selected section
   value = False
   i = 0
   a = time.time()
   while (value == False and i < 20) :
      i = time.time() - a
      newimage = device.takeSnapshot()
      sub_image = newimage.getSubImage((936./1080*WIDTH_PHONE,84./2032*HEIGHT_PHONE,144./1080*WIDTH_PHONE,144./2032*HEIGHT_PHONE))
      reference = MonkeyRunner.loadImageFromFile('C:\\Users\\G603606\\setup_sb_menu.png')
      value =  MonkeyImage.sameAs( sub_image, reference, 0.8 )
      print(i)
   
   if not value :
      print('sb namer menu issue ')
      # Takes a screenshot
      result = device.takeSnapshot()
      # Writes the screenshot to a file
      result.writeToFile('C:\Users\G603606\setup_sb_menu_issue' + date + '.png','png')
      # quit properly the monkeyrunner
      signal.signal(signal.SIGINT, signal.getsignal(signal.SIGINT))
      device.shell('killall com.android.commands.monkey')
      sys.exit()
   
   device.touch(1008./1080*WIDTH_PHONE,156./2032*HEIGHT_PHONE,'DOWN_AND_UP')
   print('touch setup button')
   MonkeyRunner.sleep(1)
   
   
   # Setup reset menu SB section
   value = False
   i = 0
   a = time.time()
   while (value == False and i < 20) :
      i = time.time() - a
      newimage = device.takeSnapshot()
      sub_image = newimage.getSubImage((216./1080*WIDTH_PHONE,116./2032*HEIGHT_PHONE,816./1080*WIDTH_PHONE,81./2032*HEIGHT_PHONE))
      reference = MonkeyRunner.loadImageFromFile('C:\\Users\\G603606\\setup_setup_sb_menu.png')
      value =  MonkeyImage.sameAs( sub_image, reference, 0.8 )
      print(i)
   
   if not value :
      print('sb namer menu issue ')
      # Takes a screenshot
      result = device.takeSnapshot()
      # Writes the screenshot to a file
      result.writeToFile('C:\Users\G603606\Results_MonkeyRunner\setup_setup_sb_menu_issue' + date + '.png','png')
      # quit properly the monkeyrunner
      signal.signal(signal.SIGINT, signal.getsignal(signal.SIGINT))
      device.shell('killall com.android.commands.monkey')
      sys.exit()
      
   
   # Setup reset menu SB section
   value = False
   i = 0
   a = time.time()
   while (value == False and i < 20) :
      i = time.time() - a
      newimage = device.takeSnapshot()
      sub_image = newimage.getSubImage((0./1080*WIDTH_PHONE,1404./2032*HEIGHT_PHONE,1080./1080*WIDTH_PHONE,132./2032*HEIGHT_PHONE))
      reference = MonkeyRunner.loadImageFromFile('C:\\Users\\G603606\\Reset_button.png')
      value =  MonkeyImage.sameAs( sub_image, reference, 1 )
      print(i)
   
   if not value :
      print('amazon not fully connected ')
      # Takes a screenshot
      result = device.takeSnapshot()
      # Writes the screenshot to a file
      result.writeToFile('C:\Users\G603606\Results_MonkeyRunner\Amazon_not_fully_connected_issue' + date +  '.png','png')
      amazon_not_fully_connected = True
      # Not quit the app because it is not a critical bug
      # sys.exit()
   
   if amazon_not_fully_connected :
      device.touch(540./1080*WIDTH_PHONE,1338./2032*HEIGHT_PHONE,'DOWN_AND_UP')
      print('touch factory reset button, with amazon connected issue')
      MonkeyRunner.sleep(1)
   
   else : 
      device.touch(540./1080*WIDTH_PHONE,1470./2032*HEIGHT_PHONE,'DOWN_AND_UP')
      print('touch factory reset button')
      MonkeyRunner.sleep(1)
   
   device.touch(817./1080*WIDTH_PHONE,1227./2032*HEIGHT_PHONE,'DOWN_AND_UP')
   print('touch factory reset button confirmation')
   
   # Wait 45 seconds, time of factory reset
   MonkeyRunner.sleep(45)

   result = device.takeSnapshot()
   # Writes the screenshot to a file
   result.writeToFile('C:\Users\G603606\Results_MonkeyRunner\itteration' + str(s) + '_' + date + '.png','png')


#   # Takes a screenshot
#   result = device.takeSnapshot()
#   # Writes the screenshot to a file
#   result.writeToFile('C:\Users\G603606\shot1.png','png')
#   sub_image.writeToFile('C:\Users\G603606\shot1.png','png')


#device.stopActivity(component=runComponent)


#   def checkIfPageIsReached ( picture_ref_path, type_screen_ref, x_coordinate, y_coordinate, width, height, tolerance ) :
#      newimage = device.takeSnapshot()
#      sub_image = newimage.getSubImage((x_coordinate, y_coordiante, width, height )
#      reference = MonkeyRunner.loadImageFromFile ( picture_ref_path )
#      value =  MonkeyImage.sameAs( sub_image, reference, tolerance )
#      return value
