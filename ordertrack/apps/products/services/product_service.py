from datetime import date
from datetime import datetime
from django.db import IntegrityError, transaction
from apps.products.models import Produtos, HistoricoCustoProdutos, MovimentacaoProdutos,Categorias
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
            return produto    
            
        
    except IntegrityError:
        print(f'Erro ao inserir dados')

    

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
            return produto
    except Produtos.DoesNotExist:
        raise ValueError("Produto não encontrado")
    
    


def delete_product(product_id,request):
    print("Iniciando a função de exclusão para o produto:", product_id)
    try:
        with transaction.atomic():
            produto = Produtos.objects.get(id = product_id)
          
           
            movimentacao = MovimentacaoProdutos.objects.create(
                    produto=produto,
                    funcionario= request.user,
                    quantidade=produto.quantidade,
                    tipo=TipoMovimentacaoProduto.EXCLUIDO.value,
                    data=datetime.now().date(),
                    hora=datetime.now().time() 
            )
            print("Movimentação criada:", movimentacao)
            produto.delete()
            return {"message: Product has been deleted"}
          
    except Produtos.DoesNotExist:
        print("Produto não encontrado para exclusão")  
        raise ValueError("This product doesn't exist")
    



# Métodos relacionado ao CRUD de categorias

def create_category (validated_data):
    try:
        if 'nome'  not in validated_data:
            print("é preciso declar o nome da categoria") 

        with transaction.atomic():
            categoria = Categorias.objects.create(**validated_data)
            return categoria
    except IntegrityError:
        print("Erro ao criar a categoria")        
    except Categorias.DoesNotExist:
        raise ValueError ("Category doesn't exist")
    


def upadate_category(category_id, validated_data):
    try:
        with transaction.atomic():
            categoria = Categorias.objects.get(id = category_id)

            for field, value in validated_data.items():
                setattr(categoria, field, value)
            
            categoria.save()
            return categoria
    except IntegrityError:
        raise ValueError("Something wrong with database config")
    except Categorias.DoesNotExist:
        print("Category not found")
             

def delete_category(category_id):
    try: 
        with transaction.atomic():
            categoria = Categorias.objects.get(id = category_id)
            categoria.delete()

            return {"Message": "Category has been deleted"}
    except IntegrityError:
        raise ValueError("Something wrong with database config")
    except Categorias.DoesNotExist:
        print("This category doesn't exist")