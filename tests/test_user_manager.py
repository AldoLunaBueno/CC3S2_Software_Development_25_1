from user_manager import UserManager, UserNotFoundError, UserAlreadyExistsError


def test_agregar_usuario_exitoso():
    # Arrange
    manager = UserManager()
    username = "albax"
    password = "123"

    # Act
    manager.add_user(username, password)

    # Assert
    message = "El usuario debería existir después de ser agregado."
    assert manager.user_exists(username), message


class FakeHashService:
    """
    Servicio de hashing 'falso' (Fake) que simplemente simula el hashing
    devolviendo la cadena con un prefijo "fakehash:" para fines de prueba.
    """
    def hash(self, plain_text: str) -> str:
        return f"fakehash:{plain_text}"

    def verify(self, plain_text: str, hashed_text: str) -> bool:
        return hashed_text == f"fakehash:{plain_text}"


def test_autenticar_usuario_exitoso_con_hash():
    # Arrange
    hash_service = FakeHashService()
    manager = UserManager(hash_service=hash_service)

    username = "usuario"
    password = "111"
    manager.add_user(username, password)

    # Act
    autenticado = manager.authenticate_user(username, password)

    # Assert
    message = "El usuario debería autenticarse correctamente \
        con la contraseña correcta."
    assert autenticado, message
