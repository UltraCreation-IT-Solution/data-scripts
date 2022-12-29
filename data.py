import json
import random
mobile_no_list = []
def gen_mobile_no():
    mobile ="+91" + random.choice(["8770","9893","9039","7000","9425","9826","8659"])+str(random.randint(100000,999999))
    mobile_no_list.append(mobile) if mobile not in mobile_no_list else None
    return mobile

final_data = []

with open("json_file/names.json","r",encoding="utf-8") as file:
    data = json.loads(file.read())
    print(data)
    for f_name in data["male"]:
        for surname in data["surnames"]:
            first_name = f_name
            last_name = surname
            email = first_name.lower() + last_name.lower() + str(random.randint(100,999)) + "@gamil.com"
            mobile_no = gen_mobile_no()
            mobile_no_list.append(mobile_no) if mobile_no not in mobile_no_list else mobile_no
            password = first_name + "@123"
            data_dict = {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "mobile": gen_mobile_no(),
                "password1": password,
                "password2": password
            }
            final_data.append(data_dict)
with open("json_file/profile.json", "w", encoding="utf-8") as file:
    file.write(json.dumps(final_data[:100]))
            
            
            
            

        

