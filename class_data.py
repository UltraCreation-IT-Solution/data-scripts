import json
import random

class Create_data():
    def profile(self,action=None):
        if action:
            action_mapper = {
                1: self.create_profile_data
            }
            action_status = action_mapper.get(action, lambda: "Invalid")()
            if action_status == "Invalid":
                print("Please Enter Valid Function")
        else:
            print("please provide action at the time of calling class")
            
    def create_profile_data(self):
        mobile_no_list = []
        def gen_mobile_no():
            self.mobile ="+91" + random.choice(["8770","9893","9039","7000","9425","9826","8659"])+str(random.randint(100000,999999))
            mobile_no_list.append(self.mobile) if self.mobile not in mobile_no_list else None
            return self.mobile
        self.final_data = []

        with open("data-scripts/json_file/names.json","r",encoding="utf-8") as file:
            data = json.loads(file.read())
            print(data)
            for f_name in data["male"]:
                for surname in data["surnames"]:
                    first_name = f_name
                    last_name = surname
                    email = first_name.lower() + last_name.lower() + str(random.randint(100,999)) + "@gamil.com"
                    self.mobile_no = gen_mobile_no()
                    mobile_no_list.append(self.mobile_no) if self.mobile_no not in mobile_no_list else self.mobile_no
                    password = first_name + "@123"
                    data_dict = {
                        "first_name": first_name,
                        "last_name": last_name,
                        "email": email,
                        "mobile": gen_mobile_no(),
                        "password1": password,
                        "password2": password
                    }
                    self.final_data.append(data_dict)
        with open("data-scripts/json_file/profile2.json", "w", encoding="utf-8") as file:
            file.write(json.dumps(self.final_data[:100]))
                
        


ob = Create_data()
ob.profile(action=1)