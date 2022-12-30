import json
import random

class CreateData:
    def __init__(self, action=None, output_file_url=None):
        self.output_file_url = output_file_url
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
        with open("input_json_file/names.json","r",encoding="utf-8") as file:
            data = json.loads(file.read())
            print(data)
            for f_name in data["female"]:
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
        if self.output_file_url:
            with open(self.output_file_url, "w", encoding="utf-8") as file:
                file.write(json.dumps(self.final_data[:100]))
        else:
            print("please enter the output file url")
                
        
output_file_url = str(input("Enter The Output File URL:"))
action = int(input("Please Enter The Action:"))

ob = CreateData(action=action, output_file_url=output_file_url)