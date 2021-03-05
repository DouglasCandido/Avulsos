let salarioBruto = prompt("Digite o valor do seu salário bruto: ");
let salarioLiquido;
let bonus = salarioBruto * 0.25;

function getSalario(salarioBruto, callback) {

    let liquido = 0;    

    const inss = salarioBruto * 0.11;
    const vr = salarioBruto * 0.05;
    const vt = salarioBruto * 0.06;
    const fgts = salarioBruto * 0.15;    
    const descontos = inss + vr + vt + fgts;    
    
    liquido = salarioBruto - descontos;
    
    return callback(liquido);

}

alert(`Lembrando que o salário líquido com uma bonificação de 25% é: ${getSalario(salarioBruto, (resultado) => {

    salarioLiquido = resultado;

    document.write(`O salário liquido é ${salarioLiquido} Reais.`);

    return salarioLiquido;

}) + bonus} Reais.`);