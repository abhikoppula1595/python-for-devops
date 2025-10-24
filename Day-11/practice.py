
# student1 = {
#         "name" : "abc",
#         "age" : 22,
#         "class" : 20
#     }

# student2 = {
#         "name" : "abc",
#         "age" : 22,
#         "class" : 20
#     }

# print(student2["name"])


ec2_instances_info = [
    {
        "id": "0999999-INstance",
        "type": "t2.micro"
    },
    {
        "id": "0998-instance",
        "type": "t2.medium"
    }
]


print(ec2_instances_info[1]["type"])


#get pull requestes information of kubernetes gitrepo using python
#step-1-request model
#step-2-api call(github)-urlfor pullrequests
#step-3-json to dictionary
#step-4-print output 


# import requests
# response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls") #in browser we just copy paste url but in python we add request.get
# complete_detail = response.json()

# for i in range(len(complete_detail)):
#     print(complete_detail[i] ["user"] ["login"])



# import requests

# response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

# complete_details = response.json()

# for i in range(len(complete_details)):
#     print(complete_details[i] ["user"] ["login"])







