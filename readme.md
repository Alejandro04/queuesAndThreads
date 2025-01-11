# 🧵 Concurrent API Calls with Threads and Queues

Este proyecto demuestra cómo realizar llamadas paralelas a múltiples APIs utilizando **hilos (threads)** y **colas (queues)** en Python. Es ideal para optimizar el tiempo de respuesta al trabajar con múltiples servicios externos, especialmente cuando las llamadas sincrónicas podrían volverse lentas y bloqueantes.

## 🚀 Descripción

El script utiliza las bibliotecas estándar `threading`, `queue` y `requests` para procesar varias URLs en paralelo. El objetivo principal es demostrar cómo implementar una arquitectura sencilla pero eficiente para la concurrencia, donde cada hilo realiza una tarea (llamada API) extraída de una cola compartida.

### **Características clave:**
- **Cola de tareas:** Utiliza `queue.Queue` para organizar las URLs que serán procesadas.
- **Hilos paralelos:** Se crean varios hilos para consumir tareas de la cola y realizar solicitudes HTTP.
- **Gestión de errores:** Captura excepciones en cada llamada y almacena los errores junto con los resultados.
- **Resultados compartidos:** Los resultados de cada solicitud se almacenan en una lista compartida.

### **Entradas:**
 
```bash
urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3",
    "https://jsonplaceholder.typicode.com/posts/4",
]
```

### **Salidas:**

#### Un tipo de salida: 

```bash
[
  {
    "url": "https://jsonplaceholder.typicode.com/posts/3",
    "status_code": 200,
    "data": {
      "userId": 1,
      "id": 3,
      "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
      "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"
    }
  },
  {
    "url": "https://jsonplaceholder.typicode.com/posts/2",
    "status_code": 200,
    "data": {
      "userId": 1,
      "id": 2,
      "title": "qui est esse",
      "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
    }
  },
  {
    "url": "https://jsonplaceholder.typicode.com/posts/4",
    "status_code": 200,
    "data": {
      "userId": 1,
      "id": 4,
      "title": "eum et est occaecati",
      "body": "ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit"
    }
  },
  {
    "url": "https://jsonplaceholder.typicode.com/posts/1",
    "status_code": 200,
    "data": {
      "userId": 1,
      "id": 1,
      "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
      "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    }
  }
] 
```

#### Otro tipo de salida:

```bash
[
  {
    "url": "https://jsonplaceholder.typicode.com/posts/2",
    "status_code": 200,
    "data": {
      "userId": 1,
      "id": 2,
      "title": "qui est esse",
      "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
    }
  },
  {
    "url": "https://jsonplaceholder.typicode.com/posts/1",
    "status_code": 200,
    "data": {
      "userId": 1,
      "id": 1,
      "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
      "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    }
  },
  {
    "url": "https://jsonplaceholder.typicode.com/posts/3",
    "status_code": 200,
    "data": {
      "userId": 1,
      "id": 3,
      "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
      "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"
    }
  },
  {
    "url": "https://jsonplaceholder.typicode.com/posts/4",
    "status_code": 200,
    "data": {
      "userId": 1,
      "id": 4,
      "title": "eum et est occaecati",
      "body": "ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit"
    }
  }
]
```
