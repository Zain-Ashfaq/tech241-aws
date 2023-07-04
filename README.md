# Differences between AWS + Azure

- **Resource groups**
  - In `Azure`, everything goes in a resource group
  - in `AWS`, resource group not necessary to use
- **IP public address**
  - In `Azure`, by default, uses `static`
  - In `AWS`, by default, uses `dynamic` (changes everytime you restart VM)
- **Terminology**
  - Launch instance = Create VM

key - Pair. aws creates one for you, keeps pub key and makes you download the private key
![alt text](./images/making-a-key-pair.jpg)

# what is dev ops

DevOps is a set of practices that combines software development and operations to improve collaboration, efficiency, and quality in the software development lifecycle. It emphasizes automation, continuous integration and delivery, infrastructure as code, automated testing, and monitoring.

# Create a VM

## Choose region

- Has to be set to Ireland for Sparta training

## Choose image

- AMI = amazon machine image - ami-0a7493ba2bc35c1e9 (the one we use (18.04 lts 1e9))
  ![alt text](./images/choosing-image.jpg)

## Choose key & SG

- Next you choose your key pair to SSH into your VM. Use the global tech241 pub key and private one is in local .ssh folder.
- **SG: ** Allows SSH, Port 27017 as inbound rules
- ![alt text](./images/select-key-pair-and-network-sg.jpg)

## Finalise

- Once you have completed the set up, you can search for your VM's using the search bar.
- You can also delete you instance (known as VM) on this menu aswell as seen in this image.
- ![alt text](./images//search-for-and-terminate-VM.jpg)

## SSH into VM

- SSH commands are shown in this image. Here is an example of a command to log in ssh -i `"~/.ssh/tech241.pem" ubuntu@ec2-54-246-226-45.eu-west-1.compute.amazonaws.com`
- ![alt text](./images/SSH-into-VM.jpg)

# MongoDB Script

- After you create a DB VM, run the DB script.
- Check the DB is running by using `sudo systemctl status mongod`. You should get a output like this image.
  ![alt text](./images/mongodb-check-status.PNG)
- Next run `sudo cat /etc/mongod.conf` and make sure the BindIP has changed to resemble this image.
  ![alt text](./images/mongodb-check-bindIP-change.PNG)

# App Script

- After you create a App VM, change this IP address to match your own DB IP in the app script `
`# Define the DB_HOST variable
  export DB_HOST=52.214.194.115:27017/posts`
- If the script ran correctly it should look like this image at the end of your command line.
  ![alt text](./images/App-Script-Check-NodeJs.PNG)
- Run the Script
- Run this command and check if the proxy has been changed correctly `sudo nano /etc/nginx/sites-available/default`
- It should look like this image
  ![alt text](./images/App-check-proxy.PNG)
