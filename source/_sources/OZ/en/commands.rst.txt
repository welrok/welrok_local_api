commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To get device parameters use ``cmd`` key.
Possible values:

   * 1 - `parameters <parameters.html>`_ request
   * 2 - `schedule <schedule.html>`_ request when controlling by floor temperature
   * 3 -  time getting request
   * 4 - `telemetry <telemetry.html>`_ request
   * 5 - `parameters <parameters.html>`_ reset request
   * 6 - `schedule <schedule.html>`_ reset request
   * 10 - `schedule <schedule.html>`_ request for devices with air-based control and air-based control with floor limitation

Example ``{"cmd":1}``

`Parameters <parameters.html>`_ request

Answer:

.. code-block:: json

   {
      "sn":"404CCAAAD4E8A89860609800000149",
      "par":[[64,6,"0"],[65,3,"300"],[23,2,"10"],
            [114,7,"0"],[115,7,"0"],[29,3,"0"],
            [66,6,"0"],[67,6,"0"],[0,6,"0"],[1,6,"0"],
            [2,2,"1"],[31,3,"230"],[3,2,"2"],[19,2,"10"],
            [18,2,"2"],[21,1,"0"],[5,3,"300"],[7,3,"50"],
            [109,7,"1"],[80,1,"0"],[81,1,"0"],[82,1,"0"],
            [25,2,"15"],[26,1,"45"],[27,1,"5"],[33,1,"35"],
            [34,1,"5"],[28,2,"16"],[17,4,"0"],[52,4,"0"],
            [53,4,"480"],[62,1,"35"],[63,1,"5"],[55,2,"24"],
            [20,1,"0"],[4,3,"230"],[6,3,"180"],[14,1,"0"],
            [15,1,"45"],[122,7,"0"],[35,2,"1"],[36,7,"1"],
            [117,7,"0"],[118,7,"0"],[121,7,"0"],[124,7,"0"],
            [125,7,"0"],[120,7,"0"]]
   }

Example ``{"cmd":2}``

`schedule <schedule.html>`_ request

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
      "sn":"9C9E6E854B44D8D5EBEBD50000014C",
      "time":"799767640", 
      "tzone":"3"
   }

Where ``time`` - time in seconds from 01.01.2000 00:00
      ``tzone`` - time zone

Example ``{"cmd":4}``

`Telemetry <telemetry.html>`_ request

Answer:

.. code-block:: json

   {
      "sn":"404CCAAAD4E8A89860609800000149",
      "t.0":"482","t.1":"399","t.2":"371","t.5":"368",
      "m.0":"2","m.1":"3","m.2":"1","m.5":"0","m.6":"255",
      "o.0":"-64","o.1":"1","o.5":"0","o.2":"0","o.4":"61",
      "t.7":"692","m.3":"0","f.3":"0","f.4":"0","f.5":"0",
      "f.6":"0","f.8":"0","f.7":"0","f.13":"0","f.0":"0",
      "f.17":"0","f.16":"0","f.9":"0","f.11":"0","f.12":"0",
      "f.20":"0","f.21":"0","f.22":"1","f.23":"0",
      "par.26":"45","par.27":"5","par.33":"35","par.34":"5",
      "time":"799767684","setPointStep":"0.5","setPointType":"3"
   }

Example ``{"cmd":5}``

`Parameters <parameters.html>`_ reset request. Request must include «sn». When blocking from the local network ([114,7,"1"]) is active, the «auth» key must be included in the request `Security  <safety.html>`_.

.. code-block:: json

   {"cmd":5,"sn":"404CCAAAD4E8A89860609800000149" }

Answer when blocking is inactive ([114,7,"0"]):

.. code-block:: json

   {
      "sn":"404CCAAAD4E8A89860609800000149",
      "par":[[64,6,"725328000"],[65,3,"300"],[23,2,"10"],
            [114,7,"0"],[115,7,"0"],[29,3,"300"],[66,6,"0"],
            [67,6,"0"],[0,6,"0"],[1,6,"0"],[2,2,"1"],[31,3,"300"],
            [3,2,"0"],[19,2,"10"],[18,2,"2"],[21,1,"0"],[5,3,"300"],
            [7,3,"50"],[109,7,"0"],[80,1,"0"],[81,1,"0"],[82,1,"0"],
            [25,2,"15"],[26,1,"45"],[27,1,"5"],[33,1,"35"],
            [34,1,"5"],[28,2,"16"],[17,4,"0"],[52,4,"1320"],
            [53,4,"480"],[62,1,"35"],[63,1,"5"],[55,2,"24"],
            [20,1,"0"],[4,3,"230"],[6,3,"180"],[14,1,"5"],
            [15,1,"45"],[122,7,"0"],[35,2,"1"],[36,7,"0"],
            [117,7,"0"],[118,7,"0"],[121,7,"0"],[124,7,"0"],
            [125,7,"0"],[120,7,"0"]]
   }

When blocking is active ([114,7,"1"]):

Answer:

.. code-block:: json

   {"sn":"404CCAAAD4E8A89860609800000149","success":"block"}


Example ``{"cmd":6}``

`Schedule <schedule.html>`_ reset request reset request. Request must include «sn».  When blocking from the local network ([114,7,"1"]) is active, the «auth» key must be included in the request `Security  <safety.html>`_.

.. code-block:: json

   {"cmd":6,"sn":"404CCAAAD4E8A89860609800000149" }

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

   {"sn":"404CCAAAD4E8A89860609800000149","success":"block"}

Example ``{"cmd":10}``

Getting `schedule <schedule.html>`_ for air control and air control with floor limit

Answer:

.. code-block:: json

   {
      "sn":"404CCAAAD4E8A89860609800000149",
      "ttAir":{
               "0":[[360,300],[480,250],[1020,300],[1320,250]],
               "1":[[360,300],[480,250],[1020,300],[1320,250]],
               "2":[[360,300],[480,250],[1020,300],[1320,250]],
               "3":[[360,300],[480,250],[1020,300],[1320,250]],
               "4":[[360,300],[480,250],[1020,300],[1320,250]],
               "5":[[480,300],[1380,250]],
               "6":[[480,300],[1380,250]]
              }
   }

.. toctree::
   :maxdepth: 1
   :caption: Подразделы команд:
   
   Parameters <parameters>
   Schedule <schedule>
   Telemetry <telemetry>
   Working with time <time>