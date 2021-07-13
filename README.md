# cURL & Python Requests Foundations Hands-On Walkthrough

Get ready to learn how to use **cURL** and **Python Requests** to work with REST APIs!  Even if you are new to either cURL or Python Requests, this walkthrough will help you learn the syntax for both tools and get you comfortable with REST API calls to several Cisco platforms, including:

- ACI
- DNA Center
- Meraki
- vManage SD-WAN
- Webex

This walkthrough DOES NOT cover a few topics which you should be familiar with before you get started:

- Basic Linux/Unix commands.
- Basic Python syntax and objects (variables, strings, lists, dictionaries, etc.).

This repo is heavy in hands-on work so that the _result_ of your learning will be your ability to comfortably use cURL and Python Requests, to the extent that you can explain or teach both to someone else.  I believe that learning the information in this repo will help you build essential skills for the **Cisco DevNet Associate** exam.

## Get Started

To use this repo:

1. Use this command in your terminal shell to create a local directory to hose the Git repository files:

   ```shell
   # Create and switch to a local directory
   
   # macOS/Linux
   mkdir ~/code && cd ~/code
   
   # Windows PowerShell
   mkdir ~/code; cd ~/code
   ```

2. Download the repo files in one of two ways:
   - Use Git to clone the repo to your computer using either HTTP _or_ SSH:
     - HTTP - `git clone https://github.com/wwt/curl-requests-foundations.git`
     - SSH - `git clone git@github.com:wwt/curl-requests-foundations.git`
   - If you don't have access to or don't know how to use Git, you can download the repo files at:
     - [https://github.com/wwt/curl-requests-foundations/archive/main.zip](https://github.com/wwt/curl-requests-foundations/archive/main.zip "Git Repository .zip File")
     - Use an archiving tool to extract the file **_main.zip_**.
     - You should now have a folder on your computer which contains the Git repository files.

3. Open Git repository folder on your computer and then locate and open the PowerPoint presentation **_curl-requests-foundations.pptx_**.

   - Start the presentation in _slide show_ mode for a walkthrough experience.
   - I use animation to help deliver the topics in small chunks, and much of the presentation will look like a mess if you don't navigate the animation in slide show mode.
   - The hands-on sections of the presentation list all of the cURL and Python commands you need to follow along with each task, and there are also screen recordings that demonstrate each task.
   - I include presenter notes on every slide, and if you have a second monitor, you can click through the slide show and read the script simultaneously.

4. Install Docker Desktop:

   - [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop "Install Docker Desktop")

5. Use this command in your terminal shell to create a Docker Container for the hands-on activities:

   ```shell
   # Run the Docker Container
   docker container run -it --name curl-pyreq1 wwt01/curl-pyreq
   ```

   - \*\*Note - your terminal prompt will change to `/code#` to indicate the Container is active.

6. Change the working directory in your Container to that of the downloaded Git repository files:

   ```shell
   # List your directories and locate the name of the Git repository folder
   ls -l
   
   # Unless you specifically renamed the folder, this command will change you to the correct directory
   cd curl-requests-foundations
   ```

7. The Git repository includes subfolders that contain reference files and scripts for the hands-on portion of the slide show.

   - The [resources](https://github.com/wwt/curl-requests-foundations/tree/master/resources "resources Folder") folder contains:
     - All of the shell scripts and Python code in the PowerPoint slides, within **curl** and **python** subdirectories.
     - Both the **curl** and **python** directories contain subdirectories for each section of the presentation (examples, ACI, DNAC, etc.).

## Feedback

I welcome any feedback or changes to this repo.  Please create a Git [Pull Request](pulls "Create Pull Request") or [Issue](issues "Create Issue"), if you want to make any changes and let me know if you have ANY questions; especially if you get stuck on something.

I wish you success with your learning journey!

Tim Hull - tim.hull@wwt.com
