from locust import HttpUser, task, between

class FlaskApiUser(HttpUser):
    wait_time = between(1, 5)  # Espera entre 1 y 5 segundos entre tareas

    @task
    def get_all_users(self):
        # Simula una solicitud GET para obtener todos los usuarios
        self.client.get("/users")

    @task
    def get_user_by_id(self):
        # Simula una solicitud GET para obtener un usuario por ID
        # Puedes ajustar el ID según los datos en tu base
        user_id = 1  # Cambia este ID según los datos disponibles
        self.client.get(f"/users/{user_id}")

    @task
    def create_user(self):
        # Simula una solicitud POST para crear un usuario
        user_data = {"id": 2, "name": "Jane Doe", "email": "jane@example.com"}
        self.client.post("/users", json=user_data)

    @task
    def update_user(self):
        # Simula una solicitud PUT para actualizar un usuario
        user_id = 1  # Cambia este ID según los datos disponibles
        updated_user = {"id": 1, "name": "John Smith", "email": "johnsmith@example.com"}
        self.client.put(f"/users/{user_id}", json=updated_user)

    @task
    def delete_user(self):
        # Simula una solicitud DELETE para eliminar un usuario
        user_id = 2  # Cambia este ID según los datos disponibles
        self.client.delete(f"/users/{user_id}")
