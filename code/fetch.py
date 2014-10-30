# Script for fetching single resources
# from a dataset on CKAN / HDX.
import urllib
import json

# URL from the dataset in question.
# Note that the id is: rowca-ebola-cases
# The same can be done for the other dataset with id: ebola-cases-2014
# That ID should not change.
url = "https://data.hdx.rwlabs.org/api/action/package_show?id=rowca-ebola-cases"
response = urllib.urlopen(url);
data = json.loads(response.read())

# The URL of the actual file (called 'resource' on CKAN)
# may change. This dataset only has one file / resource.
# As long as there is only one file, this will fetch the
# URL from that file.
fileUrl = data["result"]["resources"][0]["url"]


# Checking if the file exists.
if len(fileUrl) <= 1:
	print "There was an error"

# Downloading the file locally
else:
	urllib.urlretrieve (fileUrl, "http/data-ebola-public.xlsx")