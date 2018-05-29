import urllib.request
import json
import os
import csv

class Process(object):

    def __init__(self):        
        self.path_dp = "../datapackage.json"
        self.path_data = "../data"

        # Resolved to absolute path for debugging in vscode        
        self.path_dp = os.path.abspath(self.path_dp)
        self.path_data = os.path.abspath(self.path_data)        

        # Retrieving meta data from datapackage.json
        with open(self.path_dp) as dp:
            self.meta = json.load(dp)
        
        # Retrieving all resources
        self.resources_dp = self.meta["resources"]       
        
    
    def dumpCSVs(self):

        # Iterating through all resources and retrieving remote files
        for resource_dp in self.resources_dp:
            path_data = os.path.join(self.path_data,resource_dp["name"]) + "." + resource_dp["format"]
            urllib.request.urlretrieve(resource_dp["path"],path_archive)


if __name__ == "__main__":
    pr = Process()
    pr.dumpCSVs()