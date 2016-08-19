#!/usr/bin/python

import os

ans=True
while ans:
    print("""
    1.Update System
    2.Install Software
    3.Check IP
    4.Run Lynis
    5.Exit/Quit
    """)
    ans=raw_input("What would you like to do? ")
    if ans=="1":
      os.system ('sudo apt-get update && sudo apt-get upgrade -y')
    elif ans=="2":
      pack=raw_input("Enter package: ")
      os.system("sudo apt-get install %s" %pack)
    elif ans=="3":
      print("The Public IP is:")
      os.system ("curl -s checkip.dyndns.org | sed -e 's/.*Current IP Address: //' -e 's/<.*$//'")
    elif ans=="4":
      os.system ('sudo ./lynis -c')
      print("\n Goodbye") 
      ans = None
    else:
       print("\n Not Valid Choice Try again")