INSERT INTO `bd_exemplo`.`tb_categoria`
(`id_categoria`,
`nome`,
`cor`,
`imagem`)
VALUES
(1,
'Animais',
'#125925',
'static/imgs/icone_categoria/animais.png');

INSERT INTO `bd_exemplo`.`tb_categoria`
(`id_categoria`,
`nome`,
`cor`,
`imagem`)
VALUES
(2,
'Roupas',
'#a8328f',
'static/imgs/icone_categoria/roupas.png');




INSERT INTO `bd_exemplo`.`tb_produto`
(`nome`,
`descricao`,
`preco`,
`foto`,
`id_categoria`
)
VALUES
(
'sardinha triste',
'A sardinha triste é mais do que apenas uma lata de conservas, é uma experiência emotiva embalada em metal. Cada sardinha, cuidadosamente selecionada, carrega consigo uma história de tristeza e superação. Ao abrir a lata, você não apenas desfrutará de um sabor delicioso, mas também se conectará com a jornada emocional dessa humilde sardinha. Deixe que a sardinha triste ilumine seu dia com sua mensagem de esperança e resiliência.',
4.50,
'static/imgs/produtos/peixe.png',
1
),
(
'raposa programadora',
'A raposa programadora é uma companheira inteligente e habilidosa, pronta para auxiliá-lo em todos os seus desafios de codificação. Com sua vasta experiência em linguagens de programação, ela pode resolver problemas complexos e encontrar soluções criativas para qualquer projeto. Além disso, sua pelagem macia e seu olhar astuto tornam-na a parceira perfeita para longas sessões de programação. Adote uma raposa programadora hoje e leve sua produtividade para o próximo nível!',
19.99,
'static/imgs/produtos/raposa.png',
1
),
(
'vestido de bolinhas de plástico',
'O vestido de bolinhas de plástico é uma peça de moda única, que combina elegância e irreverência em um só design. Inspirado na estética retrô das décadas passadas, este vestido apresenta uma estampa de bolinhas de plástico que evoca memórias de brincadeiras infantis e festas animadas. Feito com tecido de alta qualidade e acabamento impecável, este vestido é perfeito para ocasiões especiais e para quem busca um visual cheio de personalidade.',
49.99,
'static/imgs/produtos/vestido_bolinha.png',
2
),
(
'vestido de café da manhã',
'O vestido de café da manhã é uma peça encantadora que celebra a primeira refeição do dia de uma forma única e estilosa. Com uma estampa vibrante e colorida de itens de café da manhã, como xícaras de café, croissants e frutas frescas, este vestido é perfeito para quem deseja começar o dia com muito estilo. Além disso, seu tecido macio e confortável proporciona um ajuste perfeito, garantindo conforto durante todo o dia. Vista-se com o vestido de café da manhã e faça uma declaração de moda deliciosamente diferente!',
29.99,
'static/imgs/produtos/vestido_comida.png',
2
),
(
'tardigrado julgador',
'O tardigrado julgador vivo é uma rara e fascinante espécie desse microorganismo que apresenta comportamentos incomuns. Em contraste com seus parentes, este tardigrado demonstra uma expressão facial única que sugere um ar de julgamento. Com seus olhos minúsculos e corpo enrugado, ele parece ponderar as escolhas e ações de todos os que o cercam. Esta espécie peculiar é um achado extraordinário para cientistas e entusiastas da natureza, oferecendo uma visão única sobre a complexidade e diversidade da vida microscópica em nosso planeta.',
299.99,
'static/imgs/produtos/tardigrado.png',
1
),
(
'capivara focada',
'A capivara focada é um exemplar vivo desse simpático roedor sul-americano, capturado em um momento de concentração intensa. Com seus olhos atentos e postura firme, esta capivara parece estar totalmente envolvida em uma atividade ou observando algo com grande interesse. Seu comportamento demonstra uma curiosidade inata e uma capacidade de focar sua atenção em algo específico, fazendo dela uma presença fascinante em seu ambiente natural. Esta capivara é um exemplo encantador da diversidade e da vida selvagem da América do Sul.',
799.99,
'static/imgs/produtos/capivara.png',
1
);
