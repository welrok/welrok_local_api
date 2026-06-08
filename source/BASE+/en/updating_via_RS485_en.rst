Instruction for Updating the Device via RS485
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**1. Preparation**

These steps are performed once on the computer before using the script for the first time.

  1.1. Installing Python

  Download and install Python from the official website:

  https://www.python.org/downloads/

  During installation, be sure to enable the option:

  Add Python to PATH

  1.2. Preparing the Files

  Extract the archive updater.zip to any convenient folder on your computer.

  :download:`updater.zip <../../_Files/updatingViaRS485/updater.zip>`

  Open the extracted folder.

  1.3. Opening a Command Prompt in the Script Folder

  In the File Explorer address bar, where the folder path is displayed, enter:

  cmd

  and press Enter.

  A command prompt will open already positioned in the required folder.

  .. image:: /_picinstr/updatingViaRS485Ru/PIC1.png
     :width: 100%
     :align: center
     :alt: Picture 1

  1.4. Creating a Virtual Environment

  Run the command:

  python -m venv .venv

  1.5. Activating the Virtual Environment

  Run the command:

  .venv\Scripts\activate

  After activation, the beginning of the command line will display:

  (.venv)

  1.6. Installing Dependencies

  Run the command:

  pip install -r requirements.txt

  After that, the preparation is complete.

**2. Updating the Device**

These steps are performed each time the device firmware needs to be updated.

  2.1. Connecting the Hardware

  Connect the USB-to-RS485 adapter to a USB port on the computer.

  Connect the RS485 output of the adapter to your board.

  2.2. Determining the COM Port

  Open Device Manager:

  Start → Device Manager

  Open the section:

  Ports (COM & LPT)

  Find the USB-to-RS485 device and note the port number, for example:

  COM3

  If multiple ports are present, disconnect and reconnect the adapter.

  The correct COM port will disappear and reappear.

  .. image:: /_picinstr/updatingViaRS485Ru/PIC2.png
     :width: 100%
     :align: center
     :alt: Picture 2

  2.3. Opening a Command Prompt

  Navigate to the folder containing the extracted script.

  In the File Explorer address bar, enter:

  cmd

  and press Enter.

  2.4. Activating the Virtual Environment

  Run the command:

  .venv\Scripts\activate

  After that, the command line should begin with:

  (.venv)

  2.5. Starting the Update

  General command format:

  python modbus_updater.py -p COM# -b 115200 --stop 1 --parity N -f apt.3g -a 247

  Parameters:

  • -p COM# — COM port of the adapter, for example COM3

  • -b 115200 — communication speed; must match the device baud rate

  • --stop 1 — number of stop bits: 1 or 2

  • --parity N — parity bit:

  o N — no parity

  o O — odd parity

  o E — even parity

  • -f apt.3g — firmware name

  If specified without an extension, the latest version will be downloaded from the cloud.

  If specified with an extension, for example apt.3g.1.5.bin, a local file from the script folder will be used.

  • -a 247 — Modbus network address of the device

  A value of 0 indicates the broadcast address.

  If the parameter is not specified, the script will scan all addresses.

**3. If There Is Only One Device on the Bus**

Use a command with the specific device address, for example 247.

This is the most reliable method because the script receives confirmation from the device.

Example command:

python modbus_updater.py -p COM3 -b 115200 --stop 1 --parity N -f apt.3g -a 247

**4. If There Are Two or More Devices on the Bus**

Use the broadcast address 0.

In this mode, the script transmits the firmware file without receiving acknowledgements from the devices. This method is faster, but packet loss is possible. Some devices may need to be updated again.

Example command:

python modbus_updater.py -p COM3 -b 115200 --stop 1 --parity N -f apt.3g -a 0

The broadcast method also works for a single device, but it is less reliable than updating using a specific device address.

**5. Completion**

After the update is finished, you can close the command prompt and disconnect the hardware.