Follow the below steps in order to create a virtual network consists of 
host machines and virtual machines and implement a firewall function to
enable/disable firewall on all of those devices.

1. Create the necessary virtual machines

2. Create an OpenVSwitch on each of the devices
	
   https://askubuntu.com/questions/333170/how-do-i-install-open-vswitch

3. Connect the OpenVswitch to the default NIC port,
   and the virtual machines by creating tap ports

   http://networkstatic.net/openflow-openvswitch-lab/

4. Download and extract the POX controller

   https://github.com/noxrepo/pox

5. Copy the "gui.py and "firewall.py" files into the "ext" folder in 
   the extracted folder.

6. Boot up the pox controller, and add firewall as a component.

   https://openflow.stanford.edu/display/ONL/POX+Wiki

7. Set the controller for the OpenVSwitches.
	
   http://networkstatic.net/openflow-openvswitch-lab/

8. Enable/Disbale the firewall on required websites using the GUI porivded
   by the "gui.py" program
