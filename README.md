#  Tanner tools program opener 

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#change-log">Change log</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

The project inspiration is based off the need for a tool that allows a user to open any version of installed tools without having to navigate to it

### Built With

* [Python](https://www.python.org/)


<!-- GETTING STARTED -->
## Getting Started

To get started with using this code, ensure you have python 3 installed. 

### Prerequisites
The  [**requirements.txt**](https://github.com/jymes9/Tanner-Tools-Program-Opener/blob/main/requirements.txt) file contains the required python libraries needed to run this program.
you can install them via pip  
For example

* PySimpleGUI
  ```sh
  pip install PySimpleGUI
  ```


### Installation

1. Open the project at **..\James\Completed scripts\program_opener** with an editor. Preferrably [**vscode**](https://code.visualstudio.com/)
2. You could also clone the repo
   ```sh
   git clone https://github.com/jymes9/Tanner-Tools-Program-Opener.git
3. Compile the file into a `.exe` or `.bin` using **pyinstaller**     
        **`pyinstaller --onefile --icon=<icon> <path to pyw>`**

<!-- MAKING CHANGES -->
## Usage

- Launch the program opener executable by clicking on the .exe file or by ./*.bin file in Linux. 
If the config.ini file doesn't exist which contains the location of the tanner tools folder, all the drives on the system shall be searched until the folder is located and then the config.ini file will be written to ease launch the next time round. 
If this directory isnt found, a dialog shall appear prompting for the location of the tools.


<!-- ROADMAP -->
## Roadmap

1. Make improvements to the GUI to handle more tools
2. Make the script more dynamic for betas.
 

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- CHANGE LOG -->
## Change log


### Beta 0.1.1 04/02/2020
- Disabled docking temporarily with "".
- Added Lib Manager
- Added check so that if dockings are disabled, proceed to open program section. TEMPORARY.
- Added nicer names (instead of ledit, L-Edit)


### 04/02/2020 BETA 0.1.2:
- Fixed Linux part to work with sourcing files. This does not work but changes were made in how programs and versions are read. 
### 04/02/2020 BETA 0.1.3:
- Commented code.
- Simplified "lastprogramchosen" by removing redundant code.
- Fixed docking issue.
### (05-11)/02/2020 BETA 0.1.4:
- Fixed remove docking (not working on 0.1.3)
- Linux program opening fixed
### (11-12)/02/2020 BETA 0.1.5:
- Added counter function (not in use)
- Fixed remove old doking bug
- Fixed .wine-tanner folder.
- Fixed program opening screen bug - linux twice same version. -> changed location of `vers = ["nothing"]`
### 13/02/2020 BETA 0.2:
- Fixed: Remember position of window 
             https://github.com/PySimpleGUI/PySimpleGUI/issues/829 
### 13/02/2020 Release 1.0.0:
- Tool finished and released
### 13/02/2020 Release 1.0.1:
- Fixed Linux bug with size of GUI due to the the fonts having different spacings in the different OSs.
### 18/03/2020 Release 1.0.2:
- Added support for different size screens.
- EH 005 Added program Icon.
### 20/04/2020 Release 1.0.3:
- DR 001 Fixed 2020.1u4 not coming up -> `(listofstuff[11])` not present.
- Started EH 001 Added back button although not coded or enabled yet (1/2)
### 29/04/2020 Release 1.0.4:
- Implemented EH 001 Add back button on open program.
-  Done by adding flags and functions to open_program()
- Implemented EH 003 Add latest version order.
- Organise the tools by latest version first.
Done by using sorted() function in `find_tanner()`.
- Started EH 002 Add Support for many different versions of the tools.
- Whenever we have too many versions of the tools, we need to change page or scroll up and down.
- Changed the way elements are counted.
### 30/04/2020 Release 1.0.5:    
- Implemented EH 002 Add Support for many different versions of the tools.
- Whenever we have too many versions of the tools, we need to change page or scroll up and down.
- Added columns "col" and "top". top contains the "Back" button and the question, and col contains the buttons.
- Added support for up to 50 versions of the same tool (up from 18)
### xx/xx/2020 Release 1.0.6:
- EH 002 Add Support for many different versions of the tools.
- Whenever we have too many versions of the tools, we need to change page or scroll up and down.
- EH 004 Add system independent tool support.
- Make the program compatible with different os architectures (i.e. Mentorgraphics in C: o D: or with a "Tanner" folder, etc.)
  Documentation link:
                https://realpython.com/documenting-python-code/
### 09/12/2022 Release 2.0.0:
- Made the tool shown version number match github
- added GNU public license

<!-- LICENSE -->
## License

GNU Genral Publuic License v3.0

<!-- CONTACT -->
## Contact

Support - support@eda-solutions.com

Project Link: [tools installer and downloader](https://github.com/EDA-Solutions-Limited/Tanner-Tools-Program-Opener.git)
