from djoser.serializers import UserCreateSerializer as Baseusercreste , UserSerializer as Baseuserserilizer

class coustomcreateuser(Baseusercreste):
    class Meta(Baseusercreste.Meta):
        fields = ['id','email','password' ,'first_name','last_name','adress','phone_number']

class coustomcurrent(Baseuserserilizer):
    class Meta(Baseuserserilizer.Meta):
        
        fields = ['id','email','first_name','last_name','adress','phone_number']