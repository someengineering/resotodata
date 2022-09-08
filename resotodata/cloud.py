import json
from pkg_resources import resource_filename

regions_file = resource_filename("resotodata", "gen/regions.json")
with open(regions_file) as f:
    regions = json.load(f)