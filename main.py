import requests
import json

class AddData:
    def __init__(self, file_url, action=None, server=False) -> None:
        if server == True:
            self.base_url = "http://13.235.152.113"
        else:
            self.base_url = "http://localhost:8000"

        self.file_url = file_url
        self.status = ""
        self.res = ""
        self.data = []
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
        final_data = []
        try:
            for object in  self.data if len(self.data) else print("json is not readble"):
                res = requests.request(method="POST", url=self.url, data=object)
                res_data = json.loads(res.text)
                final_data.append(res_data)
                if "msg" in res_data:
                    self.res = res_data.get("msg")
                    self.status = "User Object Created Successfully!"
                elif "error_msg" in res_data:
                    self.res = res_data.get("error_msg")
                    self.status = "Error has come during request"
                else:
                    self.res = None
                    self.status = "request is not running"
        except Exception as e:
            print("error has come",str(e))
        self.write_json(final_data)

    def write_json(self,list):
        with open("auth.json","w",encoding="utf-8") as file:
            file.write(json.dumps(list))
        print("data written Successfully!")
                
AddData(file_url="json_file/profile.json", action=1)

    
        
            

        
            
                
                
                    
                
    
        
        
            
        
        