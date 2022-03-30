import re
regex = re.compile(r'\b[^@\s]+@[^@\s\.]+\.[a-zA-Z]{2,3}\b')
class Mail:
    
    def __init__(self):
        self.nombre=None
        self.dominio=None
    
    def reconcimiento(self,mail):
        self.nombre = mail[:mail.index("@")]
        dominioTemp = mail[mail.index("@")+1:]
        dominioTempReverse = ''.join(reversed(dominioTemp))
        dominioTempReverse = dominioTempReverse[dominioTempReverse.index(".")+1:]
        self.dominio = ''.join(reversed(dominioTempReverse))
    def mailValido(self,mail):
        if(re.search(regex,str(mail))):
            print("soy valido")
            return True
        else:
            print("no soy valido")
            return False
    
    def saludar(self):
        while True:
            mail = str(input("Ingrese su MAIL: "))  
            if self.mailValido(mail):
                self.reconcimiento(mail)
                if self.nombre == None or self.dominio == None:
                        print("\nMail no valido.\n")
                else:
                    print(f"\nHola '{self.nombre}' felicidades por crear un mail en el dominio '{self.dominio}'.")
                    break
            else:
                 print("\nMail no valido.\n")
mail=Mail()
mail.saludar()

"""

def mailValido(mail):
   re.search(r"^[\w]+[\._]?[\w]+@[\w]+.[a-zA-Z]{2,3}",mail)

print(mailValido("naza@kkk.com"))


""" 