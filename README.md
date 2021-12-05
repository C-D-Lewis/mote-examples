# peter-examples

Example code and files for Peter.

* `mote` - Example scripts for the Mote RGB lights.


## Cheatsheet

### Connect to the Pi

Discover the PI's IP address, usually via your router's internal control panel:

> If plugged into a display, run `ifconfig | grep 192` instead.

1. Find the gateway address, usually `192.168.0.1` or find out on Google.
2. Look at any available list of connected devices, or check the DHCP client list.

Use `ssh` (Secure Shell), for example when the IP is `192.168.0.109`:

```shell
ssh pi@192.168.0.109
```

Enter the password for the `pi` user (default is `raspberry`).

### See current directory

```shell
pwd
```

Use `ls` or `ls -la` for a detailed list of this (`.`) or another directory:

> File and directory names can be auto-completed with Tab

```shell
ls -la mote/
```

### View a file's contents

Use `cat`:

```shell
cat README.md
```

### Quickly edit a file

Use `nano`:

```shell
nano README.md
```

Use the commands at the bottom to save and exit:

* `ctrl + o` - Overwrite (Save)
* `ctrl + x` - Exit

### Move or copy a file or directory

Use `mv` and `cp`:

```shell
cp README.md README.md.backup
```

```shell
mv README.md.backup README.md
```

### Delete a file

```shell
rm README.md
```

If the file was controlled with `git`, check it out to bring it back:

```shell
git checkout .
```

### Run a Python script

Use Python 3.x (2.x is deprecated)

```shell
python3 mote/rgb.py
```

### Update this repository with more recent changes

Reset all local changes:

```shell
git checkout .
```

Then update the local `main` branch:

```shell
git checkout main
git pull origin main
```

### Shutdown the Pi

```shell
sudo shutdown -h now
```

or reboot:

```shell
sudo reboot
```

### Update system software

Update the list of packages that can be upgraded:

```shell
sudo apt update
```

Then install those upgrades (and auto-answer 'yes'):

```shell
sudo apt upgrade -y
```
