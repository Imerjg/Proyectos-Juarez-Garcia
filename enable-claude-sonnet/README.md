# Enable Claude Sonnet 3.5 for All Clients

Este proyecto tiene como objetivo habilitar la funcionalidad "Claude Sonnet 3.5" para todos los clientes. A continuación se presentan detalles sobre la estructura del proyecto y cómo utilizarlo.

## Estructura del Proyecto

```
enable-claude-sonnet
├── src
│   ├── main.py          # Punto de entrada de la aplicación
│   ├── cli.py           # Interfaz de línea de comandos
│   ├── modules
│   │   └── deploy.py    # Funciones relacionadas con el despliegue
│   └── types
│       └── __init__.py  # Definición de tipos y estructuras de datos
├── scripts
│   └── enable_all_clients.sh  # Script para habilitar a todos los clientes
├── configs
│   └── settings.yaml     # Archivo de configuración en formato YAML
├── Dockerfile             # Definición de la imagen de Docker
├── requirements.txt       # Dependencias de Python
└── README.md              # Documentación del proyecto
```

## Instalación

1. Clona el repositorio:
   ```
   git clone <url-del-repositorio>
   cd enable-claude-sonnet
   ```

2. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

3. Configura el archivo `configs/settings.yaml` según tus necesidades.

## Uso

Para ejecutar la aplicación, utiliza el siguiente comando:
```
python src/main.py
```

También puedes utilizar el script para habilitar a todos los clientes:
```
bash scripts/enable_all_clients.sh
```

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT.