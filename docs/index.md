# cURL & Python Requests Hands-On Study Resources

## :fontawesome-solid-laptop-code: About

What's the big fuss over IT automation?  Well, more than anything, the excitement is about the sorts of things that you _don't_ have to do when automation is on your side.  Things like _not_ having to either copy and paste configuration changes to dozens (maybe hundreds) of different systems or repeat the same click, click, click, click, click-through-the-UI marathon over, and over, and over..._every single time_ there's a need to make a bulk change :rage:.  To automate these sorts of workflows, you need to learn to write some form of automation-specific code, and that code needs to interact with IT systems using some form of API, usually a **REST API**.

---

## :fontawesome-brands-python: Overview

This repository has a variety of hands-on, step-by-step exercies that will teach you to use [cURL](https://curl.se "cURL Homepage"){target=_blank} and Python [Requests](https://docs.python-requests.org/ "Python Requests Homepage"){target=_blank} to work with REST APIs. Even if you are new to cURL or Python Requests, this walkthrough will help you learn the syntax for both tools and get you comfortable with REST API calls to several Cisco platforms, including:

- ACI
- DNA Center
- Meraki
- vManage SD-WAN
- Webex

Each of these REST APIs uses different authentication mechanisms, URI endpoints, and payload formats, so you will learn to work REST APIs in a variety of different ways. Even if you're thinking, _"I don't work with Cisco products, why should I care about Cisco APIs?"_ If you complete the hands-on exercises in this repository, you should be able to work with just about _any_ REST API, which means you will have some mega automation superpowers.

You'll get the most from the hands-on exercises if you have at least a little bit of exposure to Python fundamentals, although we put the step-by-step directions together in a way that welcomes all experience levels.

---

## :material-bash: REST API Tools

// TODO

## :fontawesome-solid-flag: Getting Started

// TODO

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

--8<-- "includes/glossary.txt"

## :fontawesome-brands-git-alt: Contributions

// TODO
