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

- DevOps is a set of practices that combines software development and operations to improve collaboration, efficiency, and quality in the software development lifecycle. It emphasizes automation, continuous integration and delivery, infrastructure as code, automated testing, and monitoring.

- Dev Ops role is to ensure code is released ASAP so the end users can have a working piece of software.

- devs were developing on their own machines but the enviroments didnt match e.g different version of OS, different dependencies. Now dev ops can set up a dev enviroment, you can automate the deployment of code since with the same enviroment you can reduce bugs.

# Create a VM

## Choose region

- Has to be set to Ireland for Sparta training

## Choose image

- AMI = amazon machine image - used to make identical copy of VM - ami-0a7493ba2bc35c1e9 (the one we use (18.04 lts 1e9))
  ![alt text](./images/choosing-image.jpg)

## Choose key & SG

- Next you choose your key pair to SSH into your VM. Use the global tech241 pub key and private one is in local .ssh folder.
- **SG:** Allows SSH, Port 27017 as inbound rules
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

# Define the DB_HOST variable

- export DB_HOST=52.214.194.115:27017/posts`
- If the script ran correctly it should look like this image at the end of your command line.
  ![alt text](./images/App-Script-Check-NodeJs.PNG)
- Run the Script
- Run this command and check if the proxy has been changed correctly `sudo nano /etc/nginx/sites-available/default`
- It should look like this image
  ![alt text](./images/App-check-proxy.PNG)

User data: auto runs the script for only one time when the VM instance gets started and running. Root user so no need for sudo comands. Under advanced details section ![alt text](./images/user-data.jpg)

Create an image: This is how you create an image ![alt text](./images/making-a-image.PNG)

# Amazon Machine Images (AMIs)

## Introduction

An Amazon Machine Image (AMI) is a template that contains a software configuration (for example, an operating system, an application server, and applications). From an AMI, you launch instances, which are copies of the AMI running as virtual servers in the cloud. You can launch multiple instances from a single AMI when you need multiple instances with the same configuration.

## Why Create an AMI?

Creating your own AMI allows you to:

1. **Launch instances quickly**: Once you have an AMI, you can launch new instances whenever you need them.
2. **Preserve your instance configuration**: If you have spent time configuring an instance to meet your needs, you can create an AMI from it to avoid doing the same setup in the future.
3. **Control and maintain your software**: AMIs allow you to manage your own set of custom software for your projects.
4. **Share software with others**: You can share your AMIs with other AWS accounts or make them public.

## How to Create an AMI

Here are the general steps to create an AMI from an Amazon EC2 instance:

1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose 'Instances'.
3. Select the instance that you want to create an AMI of.
4. Choose 'Actions', then choose 'Create Image'.
5. In the 'Create Image' dialog box, type a unique name and description, and choose 'Create Image'.
6. After the process completes, the AMI is available for use.

For more detailed instructions, refer to the [Amazon EC2 documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-an-ami-ebs.html).

## Conclusion

AMIs are a powerful tool in AWS, allowing you to quickly launch and manage instances with your custom software and configurations. By understanding how to create and use AMIs, you can greatly improve your efficiency and productivity in AWS.

# Setting Up a Dashboard and CPU Usage Alarm in AWS

## Introduction

This document provides a step-by-step guide on how to set up a dashboard and create a CPU usage alarm for an EC2 instance in AWS. It also includes instructions on how to receive a notification via email when the alarm is triggered.

## Setting Up a Dashboard

1. Open the AWS Management Console.
2. Navigate to the CloudWatch service.
3. In the navigation pane, click on 'Dashboards'.
4. Click on 'Create dashboard'.
5. Enter a name for the dashboard and click on 'Create'.
6. On the new dashboard screen, click on 'Add widget'.
7. Select the type of widget you want to add (e.g., line, stacked area, number, text, etc.).
8. Configure the widget as per your requirements and click on 'Create widget'.

## Creating a CPU Usage Alarm

1. In the CloudWatch service, click on 'Alarms' in the navigation pane.
2. Click on 'Create alarm'.
3. Click on 'Select metric'.
4. In the 'All metrics' tab, select 'EC2 metrics'.
5. Find the instance you want to monitor and select the checkbox next to the 'CPUUtilization' metric.
6. Click on 'Select metric'.
7. Under 'Conditions', configure the alarm to trigger when the average CPU utilization is greater than a specified threshold (e.g., 7%) for a specified number of periods (e.g., 1 minute). Should look like this image.
   ![alt text](./images/Alarm/Specify%20metric%20and%20conditions.jpg)

8. Click on 'Next'.
9. Under 'Notification', select 'In alarm' and choose an SNS topic to notify when the alarm is in the 'ALARM' state.
   Should look like this image.
   ![alt text](./images/Alarm/2-Configure%20actions.jpg)
10. Click on 'Next', enter a name and description for the alarm, and click on 'Create alarm'.
    Should look like this image.
    ![alt text](./images/Alarm/3-Add%20name%20and%20description%20.jpg)

## Receiving a Notification

When the CPU usage alarm is triggered, a notification will be sent to the email address associated with the SNS topic you selected. The email will contain details about the alarm and the current state of your EC2 instance. The email should look like this
![alt text](./images/Alarm/Alarm-email.PNG)

## Testing the Alarm

You can test the alarm by SSHing into your EC2 instance and running commands like `apt update/upgrade` to increase CPU usage.

## Conclusion

Setting up a dashboard and CPU usage alarm in AWS allows you to monitor your EC2 instances effectively and receive notifications when specified conditions are met. This can help you manage your resources efficiently and respond quickly to any issues.

For more detailed instructions, refer to the [Amazon CloudWatch documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/US_AlarmAtThresholdEC2.html).
