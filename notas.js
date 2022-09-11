var imput = require('redline-sync')
console.log('================')
console.log('Resultado das avaliações')
console.log('================')
const notaA = Number(imput.question("Digite a primeira Nota"))
const notaB = Number(imput.question("Digite a segunda Nota"))
let resultadoFinal=``

const media = ((notaA + notaB)/2)
if(media >=7){
    resultadoFinal = `Aluno Aprovado`
}else{
    resultadoFinal =` Aluno Reprovado`
}
console.clear()
console.log('================')
console.log('Resultado das avaliações')
console.log('================')
console.log("Média do aluno: ${media}")
console.log(resultadoFinal)
