Commands
~~~~~~~~

The ``cmd`` key is used to get or reset device parameters, schedules, time, and telemetry.
Possible values:

   * 1 - `parameters <parameters.html>`_ request
   * 2 - `schedule <schedule.html>`_ request
   * 3 -  time getting request
   * 4 - `telemetry <telemetry.html>`_ request
   * 5 - `parameters <parameters.html>`_ reset request
   * 6 - `schedule <schedule.html>`_ reset request


Example ``{"cmd":1}``

`Parameters <parameters.html>`_ request

Answer: 

.. code-block:: json

   {
      "sn":"404CCAAAD4E8A89860609800000149",
      "par":[[0,6,"536112000"],[1,6,"536112000"],
            [2,2,"1"],[3,2,"0"],[5,1,"30"],
            [7,1,"5"],[17,4,"175"],[18,2,"2"],
            [19,2,"10"],[21,1,"0"],[23,2,"6"],
            [25,2,"15"],[26,1,"45"],[27,1,"5"],
            [28,2,"16"],[29,1,"0"],[31,1,"8"],
            [52,4,"0"],[53,4,"480"],[55,2,"24"],
            [80,1,"0"],[81,1,"0"],[82,1,"0"],
            [109,7,"0"],[114,7,"0"],[115,7,"0"],
            [117,7,"0"],[118,7,"0"],[120,7,"0"],
            [121,7,"0"],[124,7,"0"],[125,7,"0"]]
   }

Example ``{"cmd":2}``

`Schedule <schedule.html>`_ request

Answer:

.. code-block:: json

   {
      "sn":"404CCAAAD4E8A89860609800000149",
      "tt":{
            "0":[[360,300],[480,250],[1020,300],[1320,250]],
            "1":[[360,300],[480,250],[1020,300],[1320,250]],
            "2":[[360,300],[480,250],[1020,300],[1320,250]],
            "3":[[360,300],[480,250],[1020,300],[1320,250]],
            "4":[[360,300],[480,250],[1020,300],[1320,250]],
            "5":[[480,300],[1380,250]],
            "6":[[480,300],[1380,250]]
           }
   }

Example ``{"cmd":3}``

Time getting request

Answer: 

.. code-block:: json

   {
      "sn":"404CCAAAD4E8A89860609800000149",
      "time":"634993283"
   }

Where ``time`` - time in seconds from 01.01.2000 00:00

Example ``{"cmd":4}``

`Telemetry <telemetry.html>`_ request

Answer:

.. code-block:: json

   {
      "sn":"404CCAAAD4E8A89860609800000149",
      "f.0":"1","f.3":"0","f.4":"0","f.7":"0",
      "f.9":"0","f.10":"0","f.11":"0","f.12":"0",
      "f.13":"0","f.16":"0","f.20":"0","m.0":"0",
      "m.1":"0","m.2":"65","m.3":"2","m.5":"0",
      "o.0":"-57","o.1":"1","par.26":"45","par.27":"5",
      "t.0":"470","t.1":"392","t.5":"400","t.7":"640","time":"812112348"
   }

Example ``{"cmd":5}``

`Parameters <parameters.html>`_ reset request. Request must include «sn». When blocking from the local network ([114,7,"1"]) is active, the «auth» and «time» keys must be included in the request `Security  <safety.html>`_.

.. code-block:: json

   {"cmd":5,"sn":"404CCAAAD4E8A89860609800000149" }

Answer when blocking is inactive ([114,7,"0"]):

.. code-block:: json

   {
      "sn":"404CCAAAD4E8A89860609800000149",
      "par":[[0,6,"536112000"],[1,6,"536112000"],
            [2,2,"1"],[3,2,"0"],[5,1,"30"],
            [7,1,"5"],[17,4,"175"],[18,2,"2"],
            [19,2,"10"],[21,1,"0"],[23,2,"6"],
            [25,2,"15"],[26,1,"45"],[27,1,"5"],
            [28,2,"16"],[29,1,"0"],[31,1,"8"],
            [52,4,"0"],[53,4,"480"],[55,2,"24"],
            [80,1,"0"],[81,1,"0"],[82,1,"0"],
            [109,7,"0"],[114,7,"0"],[115,7,"0"],
            [117,7,"0"],[118,7,"0"],[120,7,"0"],
            [121,7,"0"],[124,7,"0"],[125,7,"0"]]
   }

When blocking is active ([114,7,"1"]):

Answer:

.. code-block:: json

   {"success":"block"}


Example ``{"cmd":6}``

`Schedule <schedule.html>`_ reset request reset request. Request must include «sn».  When blocking from the local network ([114,7,"1"]) is active, the «auth» and «time» keys must be included in the request `Security  <safety.html>`_.

Answer:

.. code-block:: json

   {
      "sn":"404CCAAAD4E8A89860609800000149",
      "tt":{
            "0":[[360,300],[480,250],[1020,300],[1320,250]],
            "1":[[360,300],[480,250],[1020,300],[1320,250]],
            "2":[[360,300],[480,250],[1020,300],[1320,250]],
            "3":[[360,300],[480,250],[1020,300],[1320,250]],
            "4":[[360,300],[480,250],[1020,300],[1320,250]],
            "5":[[480,300],[1380,250]],
            "6":[[480,300],[1380,250]]
           }
   }

When blocking is active ([114,7,"1"]):

Answer:

.. code-block:: json

   {"success":"block"}

.. toctree::
   :maxdepth: 1
   :caption: Подразделы команд:
   
   Parameters <parameters>
   Schedule <schedule>
   Telemetry <telemetry>
   Working with time <time>