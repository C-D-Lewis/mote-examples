# peter-examples

Example code and files for Peter.

* `mote` - Example scripts for the Mote RGB lights.


## Cheatsheet

### Connect to the Pi

Discover the IP address, usually via your router's internal control panel.

1. Find the gateway address, usually `192.168.0.1` or find out on Google.
2. Look at any available list of connected devices, or check the DHCP list.

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

* `ctrl + s` - Save
* `ctrl + x` - Exit

### Move or copy a file or directory

Use `mv` and `cp`:

```shell
cp README.md README.md.backup
```

```shell
mv README.md.backup README.md
```

### Run a Python script

Use Python 3.x (2.x is deprecated)

```shell
python3 mote/brideg.py
```

### Update this repository

Use `git` to reset all local changes:

```shell
git checkout .
```

Then fetch new changes and update the local `main` branch:

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
