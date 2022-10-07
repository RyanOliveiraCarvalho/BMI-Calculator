# pip install eel
import eel

eel.init('Gui') # Folder Name

@eel.expose

def imc_calculador(peso, altura):
    if altura != "":
        
        if peso != "":
            
            imc = int(peso)/((int(altura)/100)**2)
            
            if imc < 18.5:
                return "Baixo peso muito grave"
            elif imc > 18.6 and imc < 24.9:
                return "Normal"
            elif imc > 25.0 and imc < 29.9:
                return "Levemente acima do peso"
            elif imc > 30.0 and imc < 34.9:
                return "Obesidade grau I (Moderada)"
            elif imc > 35.0 and imc < 39.9:
                return "Obesidade grau II (Severa)"
            elif imc > 40.0:
                return "Obesidade grau III (Mórbida)"
            
            else:
                return "Não encontrado IMC!"
            
        else:
            return "Peso não informado!"
        
    else:
        return "Altura não informada!"
    
    

eel.start('index.html', size=(800, 600)) # Start App