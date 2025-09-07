import os
BASE_FOLDER = os.getcwd()


DEVICES_FOLDER = os.path.join(BASE_FOLDER, "data", "devices")



def list_computers():
    computers = 0
    for f in os.listdir(DEVICES_FOLDER,'efraim'):
        computers += 1

    return {"computers": computers}
print(list_computers())