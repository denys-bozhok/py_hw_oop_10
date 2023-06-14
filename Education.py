from constants import *


class Education:
    def __init__(self, education_type, education_length):
        self.education_type = education_type
        self.education_length = education_length


class General(Education):

    def __init__(self, education_type, education_cost, education_length=EDUCATIONS_LENGTH_BY_DEFAULT["poor"]):
        super().__init__(education_type, education_length)
        self.education_cost = education_cost


class ProfEducation(Education):

    def __init__(self, education_type, education_cost, education_length=EDUCATIONS_LENGTH_BY_DEFAULT["average"]):
        super().__init__(education_type, education_length)
        self.education_cost = education_cost


class AdditionalEducation(ProfEducation):

    def __init__(self, education_type, education_cost, education_length=EDUCATIONS_LENGTH_BY_DEFAULT["rich"]):
        super().__init__(education_type, education_length)
        self.education_cost = education_cost


education = Education(1, 1)
general = General("general", 0)
average = ProfEducation("prof_education", 1500)
additional_education = AdditionalEducation("additional_education", 3000)

print(education.__dict__)
print(general.__dict__)
print(average.__dict__)
print(additional_education.__dict__)
