class Data:
    def __init__(self, data):
        Data.data = data
        
    @classmethod
    def extract_the_date(cls):
        int_date = cls.data.split('-')
        if cls.check_validity(int_date):
            return int_date
        else:
            return 'date isn\'t valid!'
    
    @staticmethod
    def check_validity(int_date):
        classic_date = [31, 12, 21]

        if int(int_date[1]) == 2 and int(int_date[0]) > 28:
            return False

        elif int(int_date[1]) % 2 == 0:
            classic_date[0] = 30
        
        else:
            classic_date[0] = 31

        for el in range(len(int_date)):
            if int(int_date[el]) > classic_date[el]:
                return False
                
        return True    
        
    
my_date_1 = Data('30-12-21')
print(Data.extract_the_date())
my_date_2 = Data('32-01-21')
print(Data.extract_the_date())
my_date_3 = Data('30-02-21')
print(Data.extract_the_date())