In order to run HeTra, you need to follow the steps below:

Download the project.
Double click on the Client folder and then double click on the HetraSensorsClient application.
Double click on the Server folder and then double click on the HetraServer application.


In order to test the secure API calls, you need to follow the steps below:

Navigate e.g. to the Wristband tab on the HetraServer GUI. You may enter the UPM server address which regards the accelerometer:
gatv-dev.duckdns.org:8003/api/tender/band/data/accelerometer/last?ids=ID0001&amp;ids=ID0002 or the address which regards the heartrate:
gatv-dev.duckdns.org:8003/api/tender/band/data/heartrate/last?ids=ID0001&ids=ID0002

Then, navigate on the Wristband checkbox, check it and then click on the Connect and Check Devices button. The Wristband sensor should appear (1) on the Info tab located on the HetraSensorsClient GUI. Click on the Begin Acquisition button on the HetraServer GUI. Normally, after a few seconds you should see the appropriate JSON file on the Wristband tab located on the HetraSensorsClient GUI. You can also check the Data Display checkbox located on the HetraServer GUI in order to have a preview of the data which are to be displayed on the client.

Similarly, you may also try to make secure API calls from the Elgoline servers using the following addresses:
rr.intectiv.si:10004/position-tracker?SensorID=30AEA412C380&amp;mac=CAEB0DCFF147 (regarding the localization tracker),
rr.intectiv.si:10004/sleep-tracker?SensorID=20801444 (regarding the sleep tracker).


In order to test the kinect sensor, you need to check the Kinect checkbox, then click on the Connect and Check Devices button. Normally, if you have followed the kinect installation instructions and you have a kinect sensor connected, the kinect sensor should appear (1) on the Info tab located on the HetraSensorsClient GUI.
Then, click on the Begin Acquisition button on the HetraServer GUI and the acquisition should start.You can also check the Data Display checkbox located on the HetraServer GUI in order to have a view of the kinect frames.