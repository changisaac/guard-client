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

    # Query by tags simply by passing in the query from above
    result = guard.query_by_tags(ex_query_3)

    # Write to json easily for saving results or for visual inspection
    # Results are automatically written to the specified log location
    # Remember to include your query so GuardClient can specify it in the output
    guard.write_to_json(ex_query_3, result)

    # After deciding which scenarios you want based on you needs
    # download your scenarios directly from guard's cloud object storage
    guard.download_query(result)

    # Your done!

if __name__ == "__main__":
    main()    
