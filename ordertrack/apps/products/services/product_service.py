from datetime import date
from datetime import datetime
from django.db import transaction
from apps.products.models import Produtos, HistoricoCustoProdutos, MovimentacaoProdutos
from apps.core.enums import TipoMovimentacaoProduto



def create_product(validated_data,request):
    produto = Produtos.objects.create(**validated_data)

    
    preco_custo = validated_data.get('custo_unitario', 0)  
    HistoricoCustoProdutos.objects.create(
        produto=produto,
        preco_custo=preco_custo,
        data=date.today()  
    )

    funcionario = request.user
    print(f"Usuário autenticado: {funcionario}")

    try:
            quantidade = validated_data.get('quantidade',0)
            MovimentacaoProdutos.objects.create(
                produto=produto,
                funcionario=funcionario,
                tipo= TipoMovimentacaoProduto.ENTRADA.value,
                quantidade=quantidade,
                data=datetime.now().date(),
                hora=datetime.now().time()
            )
           
    except Exception as e:
        print(f"Erro ao criar movimentação: {e}")


    return produto

def update_product(product_id,validated_data,request):
    try:
      produto = Produtos.objects.filter(id=product_id)
      produto.update(**validated_data)



      if 'custo_unitario' in validated_data:
          preco_custo = validated_data['custo_unitario']
          HistoricoCustoProdutos.objects.create(
              produto = produto,
              preco_custo = preco_custo,
              data = datetime.now().date()
          )

      if 'quantidade' in validated_data:
          funcionario = request.user
          quantidade = validated_data['quantidade']
        
          MovimentacaoProdutos.objects.create(
              produto = produto,
              funcionario = funcionario,
              quantidade = quantidade,
              tipo = TipoMovimentacaoProduto.CORRECAO.value,
              data = datetime.now().date(),
              hora = datetime.now().date
          )
    
    except Produtos.DoesNotExist:
         raise ValueError("Product doesn't exist")
    return produto