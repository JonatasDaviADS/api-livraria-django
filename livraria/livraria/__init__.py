# Importa as "peças" do Django que conversam com o MySQL/MariaDB
from django.db.backends.mysql.base import DatabaseWrapper
from django.db.backends.mysql.features import DatabaseFeatures

# Desliga a checagem de versão: sem isso, o Django recusa o MariaDB 10.4 do XAMPP
DatabaseWrapper.check_database_version_supported = lambda self: None

# O MariaDB 10.4 não "devolve" o registro após o INSERT, então avisamos o Django
DatabaseFeatures.can_return_columns_from_insert = False