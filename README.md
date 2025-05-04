# 🥤 Máquina de Bebidas Automática

Este é um programa em Python que simula uma máquina de bebidas automática, onde você pode comprar bebidas, gerenciar o estoque e o troco, e acessar um modo administrador para cadastrar, editar ou excluir bebidas.

---

## Como funciona

Ao executar o programa, você verá um menu inicial com as opções:

- **0 - Sair**: Encerra o programa.
- **1 - Comprar bebidas**: Escolha e compre bebidas disponíveis.
- **2 - Acessar modo Admin**: Gerencie as bebidas cadastradas.

### Comprar bebidas 🛒

- Você verá uma lista de bebidas com seus códigos, preços e estoque.
- Escolha o código da bebida que deseja comprar.
- Se a bebida estiver em estoque, informe o valor para pagamento.
- O programa verifica se o valor é suficiente e calcula o troco.
- O troco é devolvido com as cédulas e moedas disponíveis no estoque.
- Se não houver troco suficiente, a compra é cancelada.
- O estoque da bebida é atualizado após a compra.

### Modo Admin 🔧

- Permite cadastrar novas bebidas, editar ou excluir bebidas existentes.
- Ao cadastrar, informe nome, preço e estoque.
- Ao editar, escolha a bebida pelo código e atualize os dados.
- Ao excluir, escolha a bebida pelo código para removê-la.
- Os códigos das bebidas são atualizados automaticamente após exclusões.

---

## Requisitos para rodar ⚙️

- Python 3 instalado no computador.
- Sistema operacional Windows (usa o comando `cls` para limpar o console).
- Terminal ou prompt de comando para executar o script.

---

## Como executar ▶️

1. Abra o terminal.
2. Navegue até a pasta onde está o arquivo `maquina.py`.
3. Execute o comando:

```bash
python maquina.py
```

4. Siga as instruções na tela para usar a máquina de bebidas.

---

## Bibliotecas usadas 📚

- `time`: para criar pausas e melhorar a experiência do usuário.
- `os`: para limpar o console entre as etapas.

---

## Observações importantes ⚠️

- O programa gerencia o estoque de troco com cédulas e moedas, garantindo que o troco seja dado corretamente.
- Caso não haja troco suficiente, a compra é cancelada.
- O modo administrador é essencial para manter o estoque atualizado.

---

## Divirta-se! 🎉

Use a máquina de bebidas virtual para praticar lógica de programação ou simular um sistema simples de vendas!
