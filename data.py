import json
import random

class Create_data:
    def __init__(self,action=None):
        if action:
            action_mapper = {
                1: self.create_profile_data
            }
            action_status = action_mapper.get(action, lambda: "Invalid")()
            if action_status == "Invalid":
                print("Please Enter Valid Function")
        else:
            print("please provide action at the time of calling class")
            
    def gen_mobile_no(self):
            mobile_no_list = [] 
            mobile ="+91" + random.choice(["8770","9893","9039","7000","9425","9826","8659"])+str(random.randint(100000,999999))
            mobile_no_list.append(mobile) if mobile not in mobile_no_list else None
            return mobile  
                
    def create_profile_data(self):
        self.final_data = []
        with open("json_file/names.json","r",encoding="utf-8") as file:
            data = json.loads(file.read())
            print(data)
            for f_name in data["male"]:
                for surname in data["surnames"]:
                    first_name = f_name
                    last_name = surname
                    email = first_name.lower() + last_name.lower() + str(random.randint(100,999)) + "@gamil.com"
                    mobile_no = self.gen_mobile_no()
                    #mobile_no_list.append(self.mobile_no) if self.mobile_no not in mobile_no_list else self.mobile_no
                    password = first_name + "@123"
                    data_dict = {
                        "first_name": first_name,
                        "last_name": last_name,
                        "email": email,
                        "mobile": mobile_no,
                        "password1": password,
                        "password2": password
                    }
                    self.final_data.append(data_dict)
            self.write_data()

    def write_data(self):
        with open("json_file/profile2.json", "w", encoding="utf-8") as file:
            file.write(json.dumps(self.final_data[:100]))
                
        


ob = Create_data(action=1)