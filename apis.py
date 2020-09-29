from datetime import datetime
current_date = datetime.now().date()
time_api = {"sitedate": "2020-02-28", "currentdate": str(current_date)}

import json
from db import data
list_apis = data.find_one({"id":1})
final_apislist = {"apis_list":list_apis["apis_list"]}


