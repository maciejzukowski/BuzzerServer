BuzzerServer
============

Buzz into your own apartment with your phone.

## Overview
If you have a intercom system with a button to buzz people in then this is for you.  Perfect for really lazy people who don't wanna get off the couch to buzz someone in BUT willing to purchase a RaspberryPi and setup a server (weird these people exist).  The setup involves a RaspberryPi near the intercom.  The PI is connected to the internet and has an attached USB relay (link below).  You need to open up the intercom and run two wires to the relay.  The PI runs buzzer_server.py.  When an http request comes in on port 50001, it flips the relay for twenty seconds effectively "buzzing" someone in.

####Frontend
I created a frontend that users connect to which kicks off a message to the PI.  I had issues with my home internet cutting out and wanted friends and neighbors to get a nice message when the PI was unreachable.
  

## Requirements
* Server to run frontend service (optional. you can connect to RaspPi directly at [home ip address]:50001
* A RaspberryPi connected to internet
* USB Relay connected to RaspPi ($5) [Ebay](http://www.ebay.com/itm/MICRO-USB-5V-2-Channel-Relay-Module-USB-Control-Relay-Module-Perfect-/131260502296?pt=LH_DefaultDomain_0&hash=item1e8fbc5118)
* Apartment with intercom and manual buzzer button 

## Installation
1. Configure PI to have static IP address.  Make sure router is forwarding port 50001 to the PI 
2. Make sure PI has python installed and [PySerial](http://pyserial.sourceforge.net/pyserial.html#installation)
3.  Connect USB relay to PI and find resource name.
  -  E.G. Use **lsusb** command or find in the /dev/ folder.  Should be something like **/dev/tty.usbserial-XXXXX**
  - Update buzzer_server.py with the resource name
4.  Run buzzer_server.py in the background
> nohup buzzer\_server.py &
5. Test operation by connecting to PI 192.168.1.xxx:50001 in a webbrowser.  You should hear the relay POP which means it works.
###Frontend Installation
1. Create folder on server and copy contents of FrontendServer.
2. Setup apache vhost for this folder.
3. Update config.php with ip address of PI
4. Hit index.php from browser to test operation (it should connect to PI and trigger relay)


## TODO
* Security with password
* dynamic ip address for frontend server

## Pictures
**Intercom & PI & USB Relay**

![](http://i.imgur.com/MuTVqQq.jpg)

**Wiring**

![](http://i.imgur.com/Y0JDq5H.jpg)

**USB RELAY**

![](http://i.imgur.com/fEKvXbp.jpg?2)

**Frontend connecting**

![](http://i.imgur.com/MfvExdm.png)

**Buzz Successful**

![](http://i.imgur.com/BauRiyO.png)




