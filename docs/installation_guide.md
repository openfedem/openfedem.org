# Installation Guide

The easiest way to get started with FEDEM is to download and install
the latest built release, and run some of the example models provided.

## Installation

64-bit binaries are provided for Windows and Linux (Ubuntu 22.04) platform.
To install the latest Windows release, proceed as follows:

* Go to the **Download** menu in the left pane and choose **Windows installer (zip)**.
  This will download a zip-file `FedemInstaller-*.zip` with the latest installation.
  You may also go to the [Releases](https://github.com/openfedem/fedem-gui/releases)
  page of the [fedem-gui](https://github.com/openfedem/fedem-gui) repository
  on github if you need to download some of the earlier releases.
* Unzip the downloaded file at arbitrary location on your PC.
* Execute the `INSTALL.bat` file as administrator.
  This will (by default) install the software in the folder "C:\Program Files\FEDEM"
  on your PC, set the file association for FEDEM model files to the GUI executable
  (`Fedem.exe`), and optionally create short-cuts to the executable on the user's Desktop
  and in the Windows Start menu.
* Unless you already have Microsoft Visual Studio installed (2015 or later),
  you may also need to download and install some C++ runtime libraries from
  [Microsoft](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170)
  before you can run the installed FEDEM GUI or solvers on Windows.
  That is, download the file [vc_redist.x64.exe](https://aka.ms/vs/17/release/vc_redist.x64.exe)
  and execute it as administrator.

To install the latest Linux release, choose **Linux installation (tar.gz)**
from the **Downlad** menu in the left pane. This will download a compressed tar-file
`Fedem-*_Ubuntu-22.04.tar.gz` with the latest Linux installation. You will also find this
 and earlier versions on the [Releases](https://github.com/openfedem/fedem-gui/releases) page.

Unpack the downloaded file in the location where you want to have Fedem installed, e.g.:

    $ cd /usr/local
    $ sudo tar zxfv ~/Downloads/Fedem-R8.1.1_Ubuntu-22.04.tar.gz

This will install Fedem R8.1.1 in the folder `/usr/local/Fedem-8.1.1`.

Then, install the required Qt6 packages:

    $ sudo apt install libqt6core6 libqt6gui6 libqt6widgets6 libqt6opengl6

## First Run

![FEDEM](images/logo.png){: align="right" style="height:40px;width:40px"}
To start FEDEM with an empty model,
either double-click the FEDEM icon on the Desktop,
or select it from the Windows Start menu.
On Linux, execute the launcher script `/usr/local/Fedem-8.1.1/fedem`.

The welcome screen of the FEDEM GUI should then (after a few seconds) appear, like this:

![Welcome to FEDEM](images/FedemWelcome.png)

The FEDEM main windows consists of the following items:

* At the very top there is a line of standard Menus (_File_, _Edit_, etc).
* Next there are two lines (the tool bars) containing some buttons used to
  initiate commands also found in the Menus.
* One of the toolbars (for executing the solvers) are placed vertically to the right.
* In the left part of the window is the _Model Manager panel_, containing
  the _Objects_ and _Results_ tabs, which allow you to create, manage, and delete
  the objects in your model, and to define Animations and Graphs for your results.
* The largest part of the main window is occupied by the Workspace area,
  containing the _Modeler_, _Control Editor_ and _Graph_ views for constructing
  and viewing models and results. Initially (like in the image above),
  it only displays the Reference plane.
* The lower left part of the main window contains the _ID and Topology panel_
  which lists objects related to the selected item.
* The area below the Workspace area is the _Property Editor panel_,
  which allows you to view and edit the properties of individual objects in the model.
* At the very bottom of the main window, the _Status bar_ is located,
  which provides information of the status, progress information
  and whether a solver process is running.

Refer to the [Users Guide](https://github.com/openfedem/fedem-docs/releases/download/fedem-8.1.1/FedemUsersGuide.pdf)
for further details on the FEDEM GUI.

If you already have a FEDEM model file, the easiest way to open it is to just double-click the file in the Windows file browser.
