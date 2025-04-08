# settings.py

# ...existing code...

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'your_database_name',  # Substitua pelo nome do seu banco de dados
        'ENFORCE_SCHEMA': False,      # Opcional: ajuste conforme necessário
        'CLIENT': {
            'host': 'your_mongodb_host',  # Substitua pelo host do MongoDB
            'port': 27017,               # Porta padrão do MongoDB
            'username': 'your_username', # Substitua pelo nome de usuário do MongoDB
            'password': 'your_password', # Substitua pela senha do MongoDB
            'authSource': 'admin',       # Substitua conforme necessário
        }
    }
}

# ...existing code...