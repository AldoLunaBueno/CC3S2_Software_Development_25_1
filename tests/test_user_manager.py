from user_manager import UserManager


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
