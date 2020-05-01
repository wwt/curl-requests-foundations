# cURL & Python Requests Foundations Hands-On Walkthrough
Get ready to learn how to use **cURL** and **Python Requests** to work with REST APIs!  Even if you are new to either cURL or Python Requests, this walkthrough will help you learn the syntax for both tools and get you comfortable with REST API calls to several Cisco platforms, including:

- ACI
- DNA Center
- Meraki
- Viptela SD-WAN
- Webex Teams

This walkthrough DOES NOT cover a few topics which you should be familiar with before you get started:

- Linux/Unix commands.
- Basic Python syntax and objects (variables, strings, lists, dictionaries, etc.)

This repo is heavy in hands-on work so that the *result* of your learning will be your ability to comfortably use cURL and Python Requests to the extent that you can explain or teach both to someone else.  I believe that learning the information in this repo will give you the information and skills necessary for the **Cisco DevNet Associate** exam.



## Get Started

To use this repo:

1. Download the repo files in one of two ways:
   - Use Git to clone the repo to your computer.
     - HTTP - `git clone https://github.com/wwt/curl-requests-foundations.git`
     - SSH - `git clone git@github.com:wwt/curl-requests-foundations.git `
   - If you don't know how to use Git, you can download the repo files at:
     - [https://github.com/wwt/curl-requests-foundations/archive/master.zip]()
2. Open the PowerPoint presentation ***curl-requests-foundations.pptx*** and start slide show mode.
   - I use animation to help deliver the topics in small chunks and much of the presentation will look like a mess if you don't navigate the animation in slide show mode.
   - The hands-on sections lists all of the cURL and Python commands you need to follow along with each task plus screen recordings which demonstrate each task.
   - I include my presenter notes on every slide and if you have a second monitor you can click through the slide show and read the script concurrently.
3. Install Docker Desktop:
   
   - [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)
4. Use this command in your terminal shell to create a Docker Container for the hands-on activities.
   ```shell
   # Create and switch to a local directory to mount to the Docker Container
   mkdir ~/code && cd ~/code # macOS/Linux
   mkdir ~/code; cd ~/code # Windows Powershell
   
   # Run the Docker Container
   docker container run -itv ~/code:/code --name curl-pyreq1 wwt01/curl-pyreq
   ```
5. The repo includes subfolders which contain reference files and scripts for the hands-on portion of the slide show.
   - The [***docker-image***](https://github.com/wwt/curl-requests-foundations/tree/master/docker-image "docker-image") folder contains:
     - A copy of the Dockerfile for the Docker Image which you use in the walkthrough (***Dockerfile***).
     - A text file which lists the Python packages in the Docker Image (***requirements.txt***).
   - The [***sample-files***](https://github.com/wwt/curl-requests-foundations/tree/master/sample-files "sample-files") folder contains:
     - All of the shell scripts and Python code in the PowerPoint slides.
     - There are **curl** and **python** subdirectories.
     - Each of those contain subdirectories for each section of the presentation (examples, ACI, DNAC, etc.)



## Feedback

I welcome any feedback or changes to the repo!  Please create a Git Pull Request or contact me if you want to make any changes and let me know if you have ANY questions; especially if you get stuck on something.

I wish you success with your learning journey!



Tim Hull - tim.hull@wwt.com