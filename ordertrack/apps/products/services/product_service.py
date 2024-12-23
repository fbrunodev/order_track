from datetime import date
from datetime import datetime
from django.db import IntegrityError, transaction
from apps.products.models import Produtos, HistoricoCustoProdutos, MovimentacaoProdutos
from apps.core.enums import TipoMovimentacaoProduto



def create_product(validated_data,request):
    try:
        with transaction.atomic():
            produto = Produtos.objects.create(**validated_data)

            
            preco_custo = validated_data.get('custo_unitario', 0)  
            HistoricoCustoProdutos.objects.create(
                produto=produto,
                preco_custo=preco_custo,
                data=date.today()  
            )

            funcionario = request.user
            print(f"Usuário autenticado: {funcionario}")

            quantidade = validated_data.get('quantidade',0)
            MovimentacaoProdutos.objects.create(
                produto=produto,
                funcionario=funcionario,
                tipo= TipoMovimentacaoProduto.ENTRADA.value,
                quantidade=quantidade,
                data=datetime.now().date(),
                hora=datetime.now().time()
                )
                
            
        
    except IntegrityError:
        print(f'Erro ao inserir dados')

    return produto

def update_product(product_id, validated_data, request):
    try:
        with transaction.atomic():
            produto = Produtos.objects.get(id=product_id)

           
            for field, value in validated_data.items():
                setattr(produto, field, value)
            
            
            produto.save()

            
            if 'custo_unitario' in validated_data:
                preco_custo = validated_data['custo_unitario']
                HistoricoCustoProdutos.objects.create(
                    produto=produto,
                    preco_custo=preco_custo,
                    data=datetime.now().date()
                )

           
            if 'quantidade' in validated_data:
                funcionario = request.user
                quantidade = validated_data['quantidade']
                
                MovimentacaoProdutos.objects.create(
                    produto=produto,
                    funcionario=funcionario,
                    quantidade=quantidade,
                    tipo=TipoMovimentacaoProduto.CORRECAO.value,
                    data=datetime.now().date(),
                    hora=datetime.now().time() 
                )
    
    except Produtos.DoesNotExist:
        raise ValueError("Produto não encontrado")
    
    return produto