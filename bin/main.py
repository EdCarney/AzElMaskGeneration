import os
import xml.etree.ElementTree as et 

from maskCreator import MaskHandler

if __name__ == "__main__":

    # get paths
    path = os.path.abspath(__file__)
    dir_path = os.path.dirname(path)
    configPath = dir_path + "\\..\\conf"

    # get values from config file
    with open(configPath + "\\" + "config.xml", 'r') as parsed_doc:
        docTree = et.parse(parsed_doc)
        docRoot = docTree.getroot()
        configDict = {
        'pivotAzimuth':docRoot.find('pivotAzimuth').text,
        'shutterElevation_right':docRoot.find('shutterElevation_right').text,
        'shutterElevation_left':docRoot.find('shutterElevation_left').text,
        'fileName':docRoot.find('fileName').text,
        }

    handler = MaskHandler(
        float(configDict['pivotAzimuth']),
        float(configDict['shutterElevation_right']),
        float(configDict['shutterElevation_left'])
        )

    handler.printToFile(dir_path + "\\..\\" + configDict['fileName'])