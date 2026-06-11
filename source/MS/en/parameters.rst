MS: Parameters list
~~~~~~~~~~~~~~~

.. Important::
   The ability to manage over a local network without a security token is `blocked <safety.html>`_ by default for security reasons. This may be relevant, for example, when using local control in public places. If this security measure is not needed, disable it on the device by setting the ``bLc`` parameter to **oFF**. Otherwise, requests for changes without this token will not be executed.

To get all available parameters of the device send command ``{"cmd":1}``, for example answer for *MS*:

.. code-block:: json

   {
      "sn":"B081843B6DC878ECBFBFEC0000014D",
      "par":[[68,2,"0"],[125,7,"0"],[70,2,"2"],
             [71,2,"0"],[3,2,"0"],[23,2,"10"],[55,2,"24"],
             [114,7,"0"],[115,7,"0"],[124,7,"0"]]
   }

``sn`` - device serial number

``par`` - parameter exchange key

Transfer format is an array of arrays. The first value is number of the parameter, the second its type, the third is string with the parameter value.

For example, turn on the device relay:

.. code-block:: json

   {
      "sn":"B081843B6DC878ECBFBFEC0000014D",
      "par":[[125,7,"1"]]
   }

Answer:

In response, we receive an updated list of parameters:

.. code-block:: json

   {
      "sn":"B081843B6DC878ECBFBFEC0000014D",
      "par":[[68,2,"0"],[125,7,"1"],[70,2,"2"],
             [71,2,"0"],[3,2,"0"],[23,2,"10"],[55,2,"24"],
             [114,7,"0"],[115,7,"0"],[124,7,"0"]]
   }

.. important::
   When changing device parameters, the command must contain the key ``sn``

.. table:: **Parameters list**
   :widths: auto

   ======   ==============  =======================    =========================================================================================================================
   Num      Type            Name                       Description
   ======   ==============  =======================    =========================================================================================================================
   3        (uint8)         controlType                operating mode: always = 0
   23       (uint8)         brightness                 in arbitrary units (from 0 to 10), device indication brightness
   55       (uint8)         relayOnTimeLimit           in hours, time after which a notification about exceeding relay operation time is triggered (Read-only)
   68       (uint8)         buttonPressTime            in seconds, button press duration to toggle the relay
   70       (uint8)         relayInitialCondition      relay state after power is applied: 0 - off, 1 - on, 2 - from memory
   71       (uint8)         externalSwitchType         external switch type selection: 0 - momentary (button), 1 - latching (switch)
   114      (bool)          lanBlock                   block any settings changes via API: 0 - disabled 1 - enabled
   115      (bool)          cloudBlock                 block any settings changes and firmware updates via cloud: 0 - disabled 1 - enabled
   124      (bool)          childrenLock               lock buttons from changing parameters: 0 - disabled 1 - enabled
   125      (bool)          powerOff                   relay state: 0 - off 1 - on
   ======   ==============  =======================    =========================================================================================================================

