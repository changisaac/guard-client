# guard-client
A framework which provides API function calls to extract specific road scenarios from a video stored in a ROS bag. Multiple adjacent frames in the video with the same objects are grouped together to create a scenario. For example one can query for all scenarios that have both trucks and traffic lights and will get back a JSON output of all the sections of the video which follow that criteria.

Below is an example demo use-case:

```
"""
Forest AI Guard
Guard Client Demo
-----------------
This is the user facing SDK that is used to interface with guard backend to query
for road scenarios. Below are examples of the types of queries that can be done
in addition to the extraction and downloading of queried scenarios.
Setup:
- Install guard client's pip depdencies using the provided requirements.txt
"""

# Maintainer: https://github.com/changisaac 

# Import GuardClient directly
from client import GuardClient

def main():
    # Instantiate GuardClient with your username and a output log location
    guard = GuardClient("demo_user", "./logs")

    # Queries are loaded in using MongoDB's expressive key:value based queries
    ex_query_1 = {
        "car": {"$gt": 0}
        }
    
    ex_query_2 = {
        "traffic light": {"$gt": 0}
        }

    ex_query_3 = {
        "car": {"$gt": 0},
        "traffic light": {"$gt": 0}
        }

    ex_query_4 = {
        "truck": {"$gt": 0},
        }
    
    ex_query_5 = {
        "speed_m_s": {"$gt": 5},
        }
    
    # Query by tags simply by passing in the query from above
    result = guard.query_by_tags(ex_query_4)

    # Write to json easily for saving results or for visual inspection
    # Results are automatically written to the specified log location
    # Remember to include your query so GuardClient can specify it in the output
    guard.write_to_json(ex_query_4, result)

    # After deciding which scenarios your want based on you needs
    # download your scenarios directly from guard's cloud object storage
    guard.download_query(result)

    # Your done!

if __name__ == "__main__":
    main()
```
