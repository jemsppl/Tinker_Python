class Learners_Mentors:
    fields = open('field.txt','w')
    field_list = fields
    def __init__(self,name,email,contact):
        self.name = name
        self.email = email
        self.contact = contact
    def addStack(self,fld):
        if fld not in field_list:
            field_list.append(fld)
        with open('field.txt','w') as f:
            f.write(field_list)


    def setMentorOrLearner(self,cat):
        self.category = cat
    def setAvailableTime(self,time):
        self.time = time
    def getMentor(self,fld,time):
        print ("Hi")
