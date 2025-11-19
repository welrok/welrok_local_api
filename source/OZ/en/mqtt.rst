**MQTT**
========

.. note::
   The device additionally implements the ability to block operation through the Welrok cloud. This block is controlled by the `parameter <parameters.html>`_ ``cloudBlock`` 115 = **1** or from the page http://``dev_ip``, where ``dev_ip`` is the device's IP address on the local network.
   If both blocks are enabled simultaneously via the `parameters <parameters.html>`_ ``lanBlock`` 114 = **1** and ``cloudBlock`` 115 = **1**, or the device menu item ``bLc`` = **on**, then the device is completely locked for remote control. Control is only possible via the buttons.

The ability to collect telemetry and control key parameters via MQTT protocol is available.
MQTT server connection settings are only accessible through the device web interface available at its local IP address:

``Host``/``Port`` - MQTT server IP address and port

``User``/``Password`` - username and password for MQTT server connection

``Keep alive`` - maximum allowed time interval without data exchange

``QoS`` - quality of service level

``Publish prefix`` - publication prefix for sending telemetry

``Subscribe path`` - subscription path name for commands

``Client ID`` - device name

.. note::
   If MQTT server authorization is not configured, the ``User``/``Password`` fields are ignored.

.. important::
   Maximum length for ``User`` and ``Password`` is 30 characters.

.. rubric:: **PUBLISHED TOPICS**

Once per minute, with +/- 5 seconds interval, data is published to the following topics:

``Publish prefix``/``Client ID``/``get``/``floorTemp`` - floor temperature sensor readings, returns value similar to `telemetry <telemetry.html>`_ requested via API for parameter **"t.1"** in °C as "xx.x" string

``Publish prefix``/``Client ID``/``get``/``airTemp`` - air temperature sensor readings, returns value similar to `telemetry <telemetry.html>`_ requested via API for parameter **"t.2"** in °C as "xx.x" string

``Publish prefix``/``Client ID``/``get``/``protTemp`` - internal overheating sensor readings, returns value similar to `telemetry <telemetry.html>`_ requested via API for parameter **"t.0"**. Returns in °C as "xx.x" string

``Publish prefix``/``Client ID``/``get``/``setTemp`` - setpoint temperature, returns value similar to `telemetry <telemetry.html>`_ requested via API for parameter **"t.5"**. Returns in °C as "xx.x" string

``Publish prefix``/``Client ID``/``get``/``powerOff`` - device power off status, returns value similar to `telemetry <telemetry.html>`_ requested via API for parameter **"f.16"**. Returns as string where "0" - enabled, "1" - disabled

``Publish prefix``/``Client ID``/``get``/``load`` - load status, returns value similar to `telemetry <telemetry.html>`_ requested via API for parameter **"f.0"**. Returns as string where "0" - disabled, "1" - enabled

``Publish prefix``/``Client ID``/``get``/``typeCtrl`` - control type, returns value similar to `telemetry <telemetry.html>`_ requested via API for parameter **"m.0"**. Returns as string where 0-by floor, 1-by air, 2-by air with floor limit

``Publish prefix``/``Client ID``/``get``/``maxFlrTmp`` - maximum allowed floor temperature for "by air with floor limit" control mode, executed similarly to API command in `parameters <parameters.html>`_. ``{"cmd":1}``

``Publish prefix``/``Client ID``/``get``/``minFlrTmp`` - minimum allowed floor temperature for "by air with floor limit" control mode, executed similarly to API command in `parameters <parameters.html>`_. ``{"cmd":1}``

``Publish prefix``/``Client ID``/``get``/``bright`` - current thermostat display brightness, read similarly to `parameters <parameters.html>`_ requested via API with ``{"cmd":1}`` command. Returns as string with values from 0 to 10.

``Publish prefix``/``Client ID``/``get``/``parameters`` - parameters request, executed similarly to API command in `parameters <parameters.html>`_. ``{"cmd":1}``

``Publish prefix``/``Client ID``/``get``/``schedule`` - schedule request, executed similarly to API command in `parameters <parameters.html>`_. ``{"cmd":2}``

``Publish prefix``/``Client ID``/``get``/``api`` - response to set/api command sending

.. rubric:: **CONTROL TOPICS**

The following topics are available for control:

.. note:: 
   After sending a control command, an out-of-turn data publication occurs after 3-5 seconds.

``Subscribe path``/``Client ID``/``set``/``setTemp`` - setpoint temperature setting. Passed as string in "xx.x" format.

``Subscribe path``/``Client ID``/``set``/``bright`` - display brightness. Passed as string in "x" format. Values from 0 to 10.

``Subscribe path``/``Client ID``/``set``/``powerOff`` - device power off. Passed as string in "x" format. Values 0 or 1, where 0 - enabled, 1 - disabled.

``Subscribe path``/``Client ID``/``set``/``mode`` - operation mode selection. Passed as string in "x" format. Values 0 or 1, where 0 - schedule, 3 - manual.

``Subscribe path``/``Client ID``/``set``/``typeCtrl`` - control type: 0-by floor, 1-by air, 2-by air with floor limit, similar to `parameter <parameters.html>`_ ``controlType``

``Publish prefix``/``Client ID``/``set``/``maxFlrTmp`` - maximum allowed floor temperature for "by air with floor limit" control mode. Passed as string in "xx.x" format.

``Publish prefix``/``Client ID``/``set``/``minFlrTmp`` - minimum allowed floor temperature for "by air with floor limit" control mode. Passed as string in "xx.x" format.

``Subscribe path``/``Client ID``/``set``/``schedule`` - schedule setting (set for 1 day). Command transmission is performed similarly to API command in `schedule <schedule.html>`_ by sending JSON containing device sn, week number and two-dimensional array with periods and temperatures.

``Subscribe path``/``Client ID``/``set``/``parameters`` - parameters setting. Command transmission is performed similarly to API command in `parameters <parameters.html>`_ by sending JSON containing device sn and two-dimensional array with required parameters, their type and value.

``Subscribe path``/``Client ID``/``set``/``api`` - duplicates webApi functionality, allowing to send commands in API format.

.. Important::
   ``setTemp`` is set based on selected control type. If "by floor" is selected, it will be set for floor. If "by air" or "by air with floor limit" is selected, it will be set for air.

.. note::
   Floor temperature sensor in device user menu and via MQTT changes with 1 °C step throughout the entire operating range. Air temperature sensor in device user menu changes with 1 °C step in range from -15 °C to -10 °C, with 0.5 °C step in range from -10 °C to 75 °C. Air temperature sensor when controlled via API changes with 0.1 °C step throughout the entire operating range.

.. note::
   Parameters 29 and 31, in schedule operation mode and temporary mode, can take values 127 and -127, which correspond to **on** (load always enabled) and **off** (load always disabled) setpoint values in graphical interface and on device display.