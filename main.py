import requests
import json

class AddData:
    """API Testing Class"""
    def __init__(self, file_url, action=None, server=False, output_file_url=None) -> None:
        if server == True:
            self.base_url = "http://13.235.152.113"
        else:
            self.base_url = "http://localhost:8000"

        self.file_url = file_url
        self.output_file_url = output_file_url
        self.status = ""
        self.res = ""
        self.data = []
        self.output_list = []
        with open(self.file_url, "r", encoding="utf-8") as file:
            self.data = json.loads(file.read())
            if action:
                action_maper = {
                    1: self.create_user_profiles,
                    # 2: self.create_blogs,
                    # 3: self.create_services,
                    # 4: self.create_orders
                }
                action_status = action_maper.get(action, lambda: "invalid")()
                if action_status == "Invalid":
                    print("please provide correct action at the time of calling class")
                print(self.res, self.status)
            else:
                print("please provide action at the time of calling class")

    
    def create_user_profiles(self):
        self.url = self.base_url + "/register/"
        try:
            for object in  self.data if len(self.data) else print("json is not readble"):
                res = requests.request(method="POST", url=self.url, data=object)
                if str(res).__contains__("500") == True:
                    print("it returns server error")
                else:
                    res_data = json.loads(res.text)
                    self.output_list.append(res_data)
                    print(res_data)

            if self.output_file_url:
                self.write_json()
            else:
                print("please provide output file url")

        except Exception as e:
            print("error has come",str(e))

    def user_login_email(self):
        self.url = self.base_url + "/login/"
        try:
            for object in  self.data if len(self.data) else print("json is not readble"):
                body = {
                    "email": object["email"],
                    "password": object["password1"]
                }
                res = requests.request(method="POST", url=self.url, data=body)
                if str(res).__contains__("500") == True:
                    pass
                else:
                    res_data = json.loads(res.text)
                    self.output_list.append(res_data)
                    print(res_data)
                
            if self.output_file_url:
                self.write_json()
            else:
                print("please provide output file url")

        except Exception as e:
            print("error has come",str(e))
    def write_json(self):
        with open(self.output_file_url, "r", encoding="utf-8") as file:
            data = json.loads(file.read())
            final_data = data.extend(self.output_list)
        with open(self.output_file_url, "w", encoding="utf-8") as file:
            file.write(json.dumps(final_data))
        print("data written Successfully!")
                
file_url = str(input("Enter The Input File URL:"))
output_file_url = str(input("Enter The Output File URL:"))
action = int(input("Please Enter The Action:"))
obj = AddData(file_url=file_url, output_file_url=output_file_url, action=action)

    
        
            

        
            
                
                
                    
                
    
        
        
            
        
        