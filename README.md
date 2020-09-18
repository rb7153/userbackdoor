# userbackdoor

To run:
A) Start the ssh_b.py file with the arguments: 
  1) The IP address of the target machine
  2) the username of the new user
  3) the password of the new user
These arguments must be used and ran before the create_account.py is ran on the target machine

B) Start the create_account.py file on the target machine with these arguments:
  1) The new username for the new account
  2) The IP address of the attacking machine
  3) Needs to be port 22 
  
One needs to run ssh_b.py first; when running create_account.py one must make sure that they create the username and password the same as what was specified in the ssh_b.py or the SSH session will not be created. 

*** The new username must be new or the ssh_b.py file will not create a session ***

