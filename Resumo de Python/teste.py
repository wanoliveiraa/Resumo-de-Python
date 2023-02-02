def main():
    alunos=["joão","lucas","heitor","arthur"]
    notas=[[7,10],[9,10],[8,10],[10,10]]; 
    if(len(alunos)==len(notas)):
        for i in range (len(alunos)):
            soma = 0 
            for nota in notas[i]:
                soma += nota
            media=soma/len(notas[i])
            print(f"o aluno: {alunos[i]} tem media :{media}")
                
    
main()    