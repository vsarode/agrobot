import json
from flask.globals import  current_app as app

def get_pick_list():
    job_list1 = []
    job_list1.append({"id": 1, "compartment": 1, "sku_code": "AGS-S-004", "status": "INCOMPLEATE", "quantity": 2,
                      "cordinate": [2,2]})
    job_list1.append({"id": 2, "compartment": 3, "sku_code": "AGS-S-005", "status": "INCOMPLEATE", "quantity": 1,
                      "cordinate": [8,8]})
    job_list1.append({"id": 3, "compartment": 2, "sku_code": "AGS-S-006", "status": "INCOMPLEATE", "quantity": 1,
                      "cordinate": [3,3]})
    job_list1.append({"id": 4, "compartment": "--", "sku_code": "BASE_CAMP", "status": "INCOMPLEATE", "quantity":  "--",
                      "cordinate": [1, 1]})

    job_list2 = []
    job_list2.append({"id": 7, "compartment": 1, "sku_code": "AGS-S-008", "status": "INCOMPLEATE", "quantity": 2,
                      "cordinate": [7, 7]})
    job_list2.append({"id": 8, "compartment": 3, "sku_code": "AGS-S-009", "status": "INCOMPLEATE", "quantity": 1,
                      "cordinate": [5, 5]})
    job_list2.append({"id": 8, "compartment": 3, "sku_code": "AGS-S-004", "status": "INCOMPLEATE", "quantity": 1,
                      "cordinate": [2, 2]})
    job_list2.append({"id": 9, "compartment": 2, "sku_code": "BASE_CAMP", "status": "INCOMPLEATE", "quantity": "--",
                      "cordinate": [1, 1]})

    job_list3 = []
    job_list3.append({"id": 13, "compartment": 1, "sku_code": "AGS-S-004", "status": "INCOMPLEATE", "quantity": 2,
                      "cordinate": [1, 1]})
    job_list3.append({"id": 14, "compartment": 3, "sku_code": "AGS-S-004", "status": "INCOMPLEATE", "quantity": 1,
                      "cordinate": [1, 1]})
    job_list3.append({"id": 15, "compartment": 2, "sku_code": "AGS-S-008", "status": "INCOMPLEATE", "quantity": 1,
                      "cordinate": [2, 2]})
    job_list3.append({"id": 16, "compartment": 4, "sku_code": "AGS-S-008", "status": "INCOMPLEATE", "quantity": 2,
                      "cordinate": [2, 2]})
    job_list3.append({"id": 17, "compartment": 3, "sku_code": "AGS-S-005", "status": "INCOMPLEATE", "quantity": 2,
                      "cordinate": [4, 3]})
    job_list3.append({"id": 18, "compartment": 2, "sku_code": "AGS-S-005", "status": "INCOMPLEATE", "quantity": 2,
                      "cordinate": [4, 3]})

    picklist = {}
    picklist[0] = job_list1
    picklist[1] = job_list2
    picklist[2] = job_list3

    app.config["PICKLISTS"] = picklist

    return picklist

if __name__=="__main__":
    result = get_pick_list()
    print json.dumps(result)
