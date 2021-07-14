# Hands-On Exercises

## :fontawesome-solid-flask: Lab Overview

The lab environment runs in a Docker Container and contains references for all of the **cURL** scripts and **Python Requests** code that you will build.  A PowerPoint Presentation file will guide you through each of the following exercises:

1. **cURL** Introduction.
2. **Python Requests** Introduction.
3. ACI[^1]
4. DNAC[^1]
5. Meraki[^1]
6. vManage SD-WAN[^1]
7. Webex[^1]

---

## :fontawesome-brands-docker: Lab Requirements

You only need a few things to start working through the hands-on exercises:

1. A Docker runtime environment.

    - [Docker Desktop for Windows or macOS](https://www.docker.com/products/docker-desktop "Docker Desktop for Windows or macOS"){target=_blank}
    - [Docker for Linux](https://hub.docker.com/search?offering=community&operating_system=linux&q=&type=edition "Docker for Linux"){target=_blank}.

2. A terminal program.

    - [Visual Studio Code Integrated Terminal](https://code.visualstudio.com/docs/editor/integrated-terminal "Visual Studio Code Integrated Terminal"){target=_blank}.
    - [Microsoft PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-windows?view=powershell-7.1 "PowerShell Installation Instructions"){target=_blank}.
    - [macOS Terminal application](https://support.apple.com/guide/terminal/welcome/mac "macOS Terminal Application"){target=_blank}.

3. [Microsoft PowerPoint](https://support.microsoft.com/en-us/office/view-a-presentation-without-powerpoint-2f1077ab-9a4e-41ba-9f75-d55bd9b231a6 "View a PowerPoint Presentation"){target=_blank}.

---

## :material-beaker: Lab Setup Instructions

Follow these steps to setup the hands-on lab environment:

???+ example "Lab Setup Directions"

    !!! attention

        - This option assumes you have an operational Docker runtime environment and that your Docker daemon can connect to and download images from [Docker Hub](https://hub.docker.com/repository/docker/wwt01/curl-pyreq "Lab Image on Docker Hub){target=_blank}.
        - The screenshots in the directions represent an example from a **macOS Terminal**, and the same commands and procedures also work with **Windows PowerShell**.

    ???+ todo "Step 1"

        1. Copy the following command to your clipboard.
        2. Open a terminal shell on the same system as your Docker runtime environment.
        3. Paste the command into your terminal shell.
        4. Run the command.

        ```bash
        docker run -it --name curl-pyreq1 wwt01/curl-pyreq
        ```

        ??? help "Docker Command Details"

            The Docker Command performs the following actions:

            1. Downloads the **wwt01/curl-pyreq** Docker Image from [Docker Hub](https://hub.docker.com/repository/docker/wwt01/curl-pyreq "Lab Image on Docker Hub){target=_blank}.
            2. Creates a new Docker Container with the name **curl-pyreq1**
            3. Attaches to the Container shell.

        [![1_docker_run](../images/docker_hub/1_docker_run.png "Docker Run Command")](../images/docker_hub/1_docker_run.png){target=_blank}


    ??? todo "Step 2"

        Click the botton below to download the instructional Microsoft PowerPoint slides:

        <div align="center" target="_blank">[Download Presentation :fontawesome-solid-file-powerpoint:](https://github.com/wwt/curl-requests-foundations/raw/main/curl-requests-foundations.pptx){ .md-button }</div>

        [![2_jupyter_started](../images/docker_hub/2_jupyter_started.png "Operational JupyterLab Server Output")](../images/docker_hub/2_jupyter_started.png){target=_blank}

    ??? todo "Step 3"

        Open the PowerPoint Presentation.

        [![3_open_python_folder](../images/docker_hub/3_open_python_folder.png "Open the 'part_i_python' folder")](../images/docker_hub/3_open_python_folder.png){target=_blank}

    ??? todo "Step 4"

        Complete each of the excercises, in sequence:

        1. The slides provide command examples for you to follow.
        2. The presenter notes provide step-by-step instructions to guide you through each slide and exercise.
        3. After each **cURL** command entry or **Python Requests** code run, a slide with a screen recording will show you what you should expect to see.

        !!! attention

            - There may be some slight variances between the output in the screen recordings and the output in your Docker environment, although each of the **cURL** commands and **Python Requests** code blocks should run successfuly.

        [![4_open_python_notebook](../images/docker_hub/4_open_python_notebook.png "Open the file 'python.ipynb'")](../images/docker_hub/4_open_python_notebook.png){target=_blank}

    ??? help "Lab Environment Shutdown and Restart"

        - To shut down the lab environment, from your terminal window press ++ctrl+d++.

        [![5_stop_jupyter](../images/docker_hub/5_stop_jupyter.png "Stop the JupyterLab Server")](../images/docker_hub/5_stop_jupyter.png){target=_blank}

    ??? note "Lab Environment Docker Command Reference"

        Use the following commands to manage your Docker lab environment:

        - Restart an existing lab environment Container (restores previous lab progress):

        ```bash
        docker start curl-pyreq1
        ```

        - Delete an existing lab environment Container (removes previous lab progress):

        ```bash
        docker stop curl-pyreq1
        docker rm curl-pyreq1
        ```

        - Remove the Docker Image:

        ```bash
        docker stop curl-pyreq1
        docker rm curl-pyreq1
        docker rmi wwt01/curl-pyreq
        ```

---

- Start the presentation in _slide show_ mode for a walkthrough experience.
- I use animation to help deliver the topics in small chunks, and much of the presentation will look like a mess if you don't navigate the animation in slide show mode.
- The hands-on sections of the presentation list all of the cURL and Python commands you need to follow along with each task, and there are also screen recordings that demonstrate each task.
- I include presenter notes on every slide, and if you have a second monitor, you can click through the slide show and read the script simultaneously.

- \*\*Note - your terminal prompt will change to `/code#` to indicate the Container is active.

7. The Git repository includes subfolders that contain reference files and scripts for the hands-on portion of the slide show.

   - The [resources](https://github.com/wwt/curl-requests-foundations/tree/master/resources "resources Folder") folder contains:
     - All of the shell scripts and Python code in the PowerPoint slides, within **curl** and **python** subdirectories.
     - Both the **curl** and **python** directories contain subdirectories for each section of the presentation (examples, ACI, DNAC, etc.).

---

## :fontawesome-brands-git-alt: Feedback, Issues, & Contributions

// TODO

[^1]: Includes the following sub-sections: Platform-Specific API Overview, **cURL** REST API exercises, and **Python Requests** REST API exercises.

--8<-- "includes/glossary.txt"
