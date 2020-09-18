# SensorsAndTurtles

## To ssh to turtlebot on Linux enabling displays

The turtlebot is configured to connect to the UTS Wifi network. When restarting, the IP address of the turtlebot will likely change.

1. Find the IP address of the turtlebot

Connect the turtlebot to a display, and find the IP address by running `ifconfig` in a terminal window

2. On the turtlebot, ensure that `/etc/ssh/sshd_config` has the following lines:

```
X11Forwarding yes
X11DisplayOffset 10
X11UseLocalhost no
```

3. On the remote PC, open (or create) the file `~/.ssh/config` and add the following lines:

```
Host *
  ForwardAgent yes
  ForwardX11 yes
```

4. On the remote PC, ssh into the turtlebot by running the command:

`ssh -X turtlebot3@[IP_ADDRESS]`

where `IP_ADDRESS` is the IP address of the turtlebot found in step 1. `-X` will enable X11 forwarding to allow the display to show on the remote PC

Further reading: https://unix.stackexchange.com/questions/12755/how-to-forward-x-over-ssh-to-run-graphics-applications-remotely
