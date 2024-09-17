from fpdf import FPDF

class PDF(FPDF):

    def titulo(self, label):
        self.set_font('helvetica', 'B', size=24)
        self.cell(0, 60, label, 0, 1, 'C')

    def sub_titulo(self, label):
        self.set_font('helvetica', 'I', size=16)
        self.cell(0, 10, label, 0, 1, 'C')
    
    def linha_centralizada(self, label):
        self.set_font('helvetica', '', size=12)
        self.cell(0, 10, label, 0, 1, 'C')
    
    def titulo_base(self, label):
        self.set_font('helvetica', 'B', size=16)
        self.cell(0, 10, label, 0, 1, 'L')
        self.ln()

    def paragrafo(self, text):
        self.set_font('helvetica', '', size=12)
        self.multi_cell(0, 7, text)
        self.ln()

    def imagem(self, img, x, y, w):
        self.image(img, x, y, w)

pdf = PDF()

# ------------- Fazendo a capa -------------
pdf.add_page()

pdf.titulo("Desigualdade da Educação no Brasil")
pdf.sub_titulo("Analise da educação do Brasil")
pdf.imagem("imagem_capa_escola.jpg", 40, 90, 130)
pdf.ln(160)
pdf.linha_centralizada("Feito por: Cauã Alberto de Araújo")
pdf.linha_centralizada("Data: 07 de Setembro de 2024 - RP/SP")

#1 pagina
pdf.add_page()

pdf.titulo_base("Introdução")

pdf.paragrafo(" A Educação de nosso país (Brasil), é um assunto bastante discutido e analisado, pois além de apresentar diversas falhas, tanto por culpa da forma com que foi implementado, quanto com a falta de um investimento mais inteligente, e mesmo pesquisas sendo feitas todos os anos, ainda tentamos enfrentar esse grande problema, que acaba por deixar diversas pessoas com diagnósticos de analfabetismo funcional/não funcional. Nesse relatório vai ser apresentado alguns gráficos, gerados exatamente para a fácil visualização de como a educação está sendo analisada no Brasil, e possíveis maneiras da educação se estabelecer de for correta. ")

pdf.paragrafo("(A maioria das informações desse relátorio foi retirada do GitHub)")

#2 pagina
pdf.add_page()

pdf.titulo_base("Média das Matrículas (Fundamental)")

pdf.paragrafo(" O gráfico abaixo está comparando a taxa de matrícula dos alunos em escolas públicas e em escolas privadas. Como todos já sabem, o investimento em escolas privadas é totalmente diferente do que o governo investe nas escolas públicas, tendo isso em mente, quando comparamos o nível dos alunos e professores de cada escolas, podemos tirar dessa análise que alunos de escolas privadas acabem recebendo mais conteúdo, e isso não é por culpa do aluno não sentir vontade de consumir o conteúdo dado em sua escola pública, mas sim a atenção e incentivo que falta para esse aluno evoluir, pois desde já, escutamos nossos pais, familiares, amigos e até os próprios professores falando que a escola privada possui um ensino melhor, acabando totalmente com a esperança de qualquer aluno de escola pública.")

pdf.imagem("MédiaFundamental.png", 30, 105, 150)
pdf.ln(120)

#3 pagina
pdf.add_page()

pdf.titulo_base("Média das Matrículas (Médio)")

pdf.paragrafo(" Seguindo a mesma linha de raciocinio, aqui podemos analisar um outro gráfico, semelhante ao acima, mas destacando o nível escolar (Ensino Médio).")

pdf.imagem("MédiaMédio.png", 30, 60, 150)
pdf.ln(120)

#4 pagina
pdf.add_page()

pdf.titulo_base("Taxa de analfabetismo")

pdf.paragrafo(" No gráfico acima, só levei em conta a quantidade de matrículas total do Brasil, mas possui um outro problema que é importante destacar, que são aqueles que não estão matriculados em nenhuma escola ou instituição de ensino, e isso se torna algo muito preocupante, pois a maioria abandona a escola para ir atrás de empregos, pois os pais e mães as vezes não conseguem manter a casa sozinhos. E essa situação é muito encontrada no Brasil, sendo algo muito prejudicial para aquele jovem, que além de crescer uma pessoa analfabeta, e não funcional na maioria das vezes, vai perder também diversas oportunidades na vida, pois ter o ensino fundamental e o ensino médio hoje em dia é o mínimo. Diversas entrevistas foram feitas e podemos perceber que grande parte da população sofreu ou está sofrendo com isso, então projetamos um gráfico que mostra com detalhes a taxa de analfabetização em cada Região do Brasil. Normalmente a taxa de analfabetização só vai aumentando em relação a raça da pessoa, sendo os brancos os que possui mais alfabetização, e os negros e pardas, com porcentagens maiores de analfabetização. ")

pdf.imagem("Analfabetismo.png", 17, 130, 170)
pdf.ln(120)

pdf.paragrafo(" vantajosas ter que trocar de cidade, para estudar em faculdades ou escolas mais vantajosas para elas. E essas regiões menos favoráveis vai acabar também sendo prejudicado, pois se aquela área não formar profissionais de áreas especificas aquela cidade acaba não possuindo esse profissional, para cumprir com sua profissão ou para repassar o aprendizado para o proximo")

#5 pagina
pdf.add_page()

pdf.titulo_base("Conclusão")

pdf.paragrafo(" Após essa análise de dados podemos concluir que, as escolas públicas precisam de uma atenção a mais, como investimentos, normas diferentes, etc. Mas infelizmente não é algo muito fácil de estar mudando, e diversos governos já fizeram diversas mudanças sobre esse tema, e alguns até piorando um pouco a educação do nosso País. É um tema muito complicado de se discutir, pois é sobre o futuro das crianças e jovens, e qualquer mudança falha pode fazer total diferença. Mas também não podemos dizer que o governo só ignora as escolas públicas, e possui diversos projetos que dão um incentivo e diversas oportunidades para os estudando de escolas públicas.")

pdf.output("relatório_escolar.pdf")