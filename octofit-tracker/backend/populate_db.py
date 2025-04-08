import os
import django

# Configurar o ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from your_app.models import YourModel  # Substitua pelo nome do seu app e modelo

def populate_data():
    # Exemplo de dados de teste
    test_data = [
        {"field1": "Valor 1", "field2": "Valor 2"},
        {"field1": "Valor 3", "field2": "Valor 4"},
    ]

    for data in test_data:
        YourModel.objects.create(**data)
        print(f"Adicionado: {data}")

if __name__ == "__main__":
    populate_data()
    print("Dados de teste adicionados com sucesso!")
