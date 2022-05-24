# Software Web para Gestão de Mercadorias e Vendas de Estabelecimentos Comerciais

A princípio, no nosso MVP, teremos quatro tipos de perfis de acesso, sendo que cada perfil pode ser atrelado a um ou vários usuários:

# Perfis

## Administrador

Perfil com acesso total. Poderá ver informações financeiras do sistema, com breves relatórios com filtros pré-definidos. Será responsável por gerenciar acessos de perfis do tipo "Gestor" podendo adicionar, remover ou editar o acesso desses tipos de usuários. Terá acesso às demais funcionalidades do sistema.

## Gestor

Perfil responsável principalmente por gerir o estoque do estabelecimento, adicionando, removendo ou editando mercadorias. Por ser responsável pelas mercadorias, também é responsável por edição de preços, promoções e itens relacionados. Também é o principal responsável por gerir acessos do tipo "Caixa" adicionando, removendo ou editando usuários com esse tipo de permissão.

## Caixa

Perfil responsável principalmente por adicionar vendas no sistema.

## Cliente

Perfil destinado aos clientes que queiram realizar compras online no estabelecimento comercial em questão.

## Extras

As vendas podem ser feitas presencialmente, através de um caixa, ou online através de um perfil de usuário do tipo "Cliente". A princípio, cada venda feita por um Caixa será feita através de uma listagem de itens e suas respectivas quantidades, futuramente sendo interessante integrar com leitura de código de barras.

Cada venda feita deverá ter uma lógica implícita, diminuindo a quantidade de itens do estoque e jogando informações relacionadas no financeiro.

Inicialmente será simulada uma transação financeira com sucesso, sendo interessante a integração com pix QR Code e demais formas de pagamento.
