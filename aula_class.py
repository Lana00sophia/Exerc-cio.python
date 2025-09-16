class User:
    def __init__(self,user_name,password,email) :
        self.user_name + user_name 
        self.__password = password
        self.email = email
        self.posts = []
    
    def __str__(self):
        return(f"Usuário: {self.user_name}, Email")