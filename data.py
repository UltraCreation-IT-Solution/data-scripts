import json
import random


class CreateData:
    def __init__(self, action=None, output_file_url=None):
        self.output_file_url = output_file_url
        self.final_data = []
        self.data = []
        if action:
            action_mapper = {
                1: self.create_user_profile_data,
                2: self.create_expert_profile_data,
                3: self.create_expert_seducation,
                4: self.create_expert_experience_data,
                5: self.create_expert_skills,
                6: self.create_expert_bank_details
            }
            action_status = action_mapper.get(action, lambda: "Invalid")()
            if action_status == "Invalid":
                print("Please Enter Valid Function")
        else:
            print("please provide action at the time of calling class")

    def gen_mobile_no(self):
        mobile_no_list = []
        mobile = "+91" + random.choice(["8770", "9893", "9039", "7000",
                                       "9425", "9826", "8659"])+str(random.randint(100000, 999999))
        mobile_no_list.append(mobile) if mobile not in mobile_no_list else None
        return mobile

    def create_user_profile_data(self):
        with open("data-scripts/input_json_file/names.json", "r", encoding="utf-8") as file:
            self.data = json.loads(file.read())
            for f_name in self.data["female"]:
                for surname in self.data["surnames"]:
                    first_name = f_name
                    last_name = surname
                    email = first_name.lower() + last_name.lower() + \
                        str(random.randint(100, 999)) + "@gamil.com"
                    mobile_no = self.gen_mobile_no()
                    # mobile_no_list.append(self.mobile_no) if self.mobile_no not in mobile_no_list else self.mobile_no
                    password = first_name + "@123"
                    gender = "female"

                    data_dict = {
                        "first_name": first_name,
                        "last_name": last_name,
                        "email": email,
                        "mobile": mobile_no,
                        "gender": gender,
                        "password1": password,
                        "password2": password
                    }
                    self.final_data.append(data_dict)
            self.write_data()

    def create_expert_profile_data(self):
        for i in range(1, 101):
            self.level = random.choice(["beginner", "intermediate", "advance", "highly qualified",
                                        "experience 2-5", "experience 5-9", "experience more than 10"])
            self.about_me = random.choice(["Google certified", "Certified By Great Learning", "Certified By HPE",
                                           "Certified By Udemy", "Certified By Linkdin", "CEO At Great Learning", "Manager At Google"])
            profession = random.choice(["Python developer", "Java Developer", "Php Developer",
                                        "Larvel Developer", "OODO Developer", "Tester", "Database Developer"])
            data_dict = {
                "level": self.level,
                "about_me": self.about_me,
                "profession": profession
            }
            self.final_data.append(data_dict)
        self.write_data()

    def create_expert_experience_data(self):
        for i in range(100):
            company_name = random.choice(["Msys Technologies", "VCOSMOS", "Softprodigy Solutions",
                                          "Google", "Agnito Technologies", "CIS", "Dazven Software Solutions", "Netlink Software Solutions"])
            Start_date = random.choice(["1-July-2019", "1-Dec-2019", "1-Jan-2020", "1-Mar-2018", "1-Oct-2022"
                                        "1-June-2018", "1-Nov-2021", "1-Sep-2021", "1-Feb-2021", "1-Apr-2018", "1-May-2018", "1-Aug-2018"])
            end_date = random.choice(["Still Working", "1 Month Notice Period",
                                     "10 Days Notice Period", "20 Days Notice Period", "5 Days Notice Period"])

            profession = random.choice(["Python developer", "Java Developer", "Php Developer",
                                        "Larvel Developer", "OODO Developer", "Tester", "Database Developer"])
            data_dict = {
                "company_name": company_name,
                "Start_date": Start_date,
                "end_date": end_date,
                "designation": profession
            }
            self.final_data.append(data_dict)
        self.write_data()

    def create_expert_skills(self):
        for i in range(100):
            technology_name = random.choice(
                ["Python", "Java", "Php", "Larvel", "OODO", "HTML", "CSS", "Javascript", "MYSQL", "Postgresql"])
            ratings = random.randint(1, 10)
            data_dict = {
                "technology_name": technology_name,
                "ratings": ratings
            }
            self.final_data.append(data_dict)
        self.write_data()

    def create_expert_seducation(self):
        for i in range(100):
            school = random.choice(["St Saviour Public High School", "Tender High School",
                                   "Bhopal Public School", "Elite Higher Secondary School", "Navnidh Higher Secondar School", "Mithi Govidram Higher Secondary School", "Bhopal Girls Higher Secondary School", "Bhopal Boys Higher Secondary School", "Christ Memorial Higher Secondary School", "Red Rose Higher Secondary School"])
            city_name = random.choice(
                ["Bhopal", "Indore", "Jabalpur", "Pune", "Delhi", "Bombay", "Agra"])
            city_name1 = random.choice(
                ["Bhopal", "Indore", "Jabalpur", "Pune", "Delhi", "Bombay", "Agra"])
            state = random.choice(
                ["Madhya Pradesh", "Maharashtra", "Karnatka", "Uttar Pradesh"])
            passing_year = random.choice(
                ["2012", "2013", "2014", "2015", "2016", "2017", "2018"])
            college_name = random.choice(
                ["BSS", "Excelence College Of Engineering", "RKDF", "RGPV", "BU", "SIS Tech"])
            institute_name = random.choice(["Sunny Group Of Institues",
                              "Cybrom Technology", "Fidato Technology", "FSH Technologies","Surya Institues","IBM","Google"])
            data_dict = [{
                "type": "High School",
                "institute_name": school,
                "city": city_name,
                "state_name": state,
                "country": "India",
                "passing_year": passing_year,
                "Division": random.choice(
                    ["First Division", "Second Division", "Third division"])
            },
                {
                "type": "Higher Scondry",
                "institute_name": school,
                "city": city_name,
                "state_name": state,
                "country": "India",
                "passing_year": str(int(passing_year) + 2),
                "Devision": random.choice(
                    ["First Division", "Second Division", "Third division"])
            },
                {
                "type": "Graduation",
                "institute_name": college_name,
                "city": city_name1,
                "state_name": state,
                "country": "India",
                "passing_year": str(int(passing_year) + 5),
                "Division": random.choice(
                    ["First Division", "Second Division", "Third division"])
            },
                {
                "type": "Post Graduation",
                "institute_name": college_name,
                "city": city_name1,
                "state_name": state,
                "country": "India",
                "passing_year": str(int(passing_year) + 8),
                "Devision": random.choice(
                    ["First Division", "Second Division", "Third division"])
            },
            {
                "type": "Certificate",
                "institute_name": institute_name,
                "city": city_name,
                "state_name": state,
                "country": "India",
                "passing_year": str(int(passing_year) + 8),
                "Devision": random.choice(
                    ["First Division", "Second Division", "Third division"])
        }]
            self.final_data.append(data_dict)
        self.write_data()
    
    def gen_account_no(self):
        account_no_list = []
        account = random.randint(10000000000, 99999999999)
        account_no_list.append(account) if account not in account_no_list else None
        return account
    
    def create_expert_bank_details(self):
        with open("data-scripts/input_json_file/user_data.json", "r", encoding="utf-8") as file:
            self.data = json.loads(file.read())
            for object in self.data:
                bank_name = random.choice(["ICICI Bank","SBI","BOB","Indian Bank","HDFC","PNB"])
                ifsc = random.choice(["0477400","0772000","00000055","0458964","02365476","0258962","06352896","03598542","02587415","03698524","02574125"])
                data_dict = {
                    "account_holder":object["first_name"] +"  " + object["last_name"],
                    "bank_name": bank_name,
                    "account_number":self.gen_account_no() ,
                    "ifsc_code":str(bank_name[:4] + ifsc)
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
