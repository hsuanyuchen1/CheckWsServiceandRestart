import win32serviceutil as ws
import subprocess as sp

if ws.QueryServiceStatus("Actix CT Geo Adapter NSN LCBIN LTE S")[1] != 4:
    sp.run(["C:\source\RestartAdaptor.cmd"])
else:
    print("Service is running")
