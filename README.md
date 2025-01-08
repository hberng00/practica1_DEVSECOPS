# Practica1DEVSECOPS

# CI/CD Pipeline

Este flujo de trabajo de CI/CD en GitHub Actions se activa automáticamente cuando se realiza un "push" en la rama main del repositorio. El pipeline realiza los siguientes pasos:
1. Checkout del código: Obtiene el código más reciente del repositorio.
2. Configuración de Docker: Configura Docker en el entorno de ejecución.
3. Construcción de la imagen Docker: Construye la imagen Docker de la aplicación Flask utilizando el Dockerfile del proyecto.
4. Ejecución del contenedor: Inicia un contenedor Docker y expone el puerto 5000 para acceder a la aplicación Flask.
5. Espera a que el contenedor esté listo: El flujo de trabajo espera hasta 30 segundos para verificar que la aplicación esté respondiendo en el puerto 5000. Si la aplicación no está lista en ese tiempo, el pipeline falla.
6. Prueba de la aplicación: Realiza una solicitud HTTP para verificar que la aplicación Flask esté funcionando correctamente.
7. Limpieza: Finalmente, se elimina el contenedor Docker para limpiar el entorno.
Este pipeline garantiza que la aplicación se construya, ejecute y pruebe automáticamente cada vez que se realice un cambio en la rama main.

# Pylint Workflow

Este flujo de trabajo de GitHub Actions está diseñado para analizar el código Python utilizando Pylint cada vez que se realiza un "push" en la rama main. El propósito de este flujo es asegurar que el código siga las mejores prácticas y estándares de estilo definidos por PEP 8. A continuación se describen los pasos que realiza el flujo de trabajo:

1. Checkout del código: Obtiene el código más reciente del repositorio utilizando la acción actions/checkout.
2. Configuración de Python: Establece el entorno Python 3.9 utilizando la acción actions/setup-python.
3. Instalación de dependencias: Instala las dependencias necesarias como pylint, pytest, flask y autopep8.
4. Formato de código con autopep8: Ejecuta autopep8 para corregir automáticamente el estilo del código según las reglas de PEP 8, aplicando dos niveles de corrección agresiva a app.py y test_app.py.
5. Análisis estático con Pylint: Ejecuta pylint sobre app.py y test_app.py para detectar errores, advertencias y sugerencias de mejora en el código.
Este flujo de trabajo ayuda a mantener la calidad del código, asegurando que siga los estándares de estilo y detectando posibles problemas antes de ser fusionados en la rama main.

# Doxygen Deployment

Este flujo de trabajo de GitHub Actions está diseñado para generar y desplegar la documentación de código utilizando Doxygen en GitHub Pages. El pipeline se activa automáticamente cuando se realiza un "push" en la rama main, o puede ser disparado manualmente mediante workflow_dispatch. Los pasos que realiza este flujo de trabajo son los siguientes:

1. Checkout del código: Obtiene el código más reciente del repositorio utilizando la acción actions/checkout.
2. Generación de documentación con Doxygen: Utiliza la acción mattnotmitt/doxygen-action para generar la documentación de Doxygen a partir de un archivo de configuración Doxyfile ubicado en .github/Doxyfile.
3. Despliegue en GitHub Pages: Despliega la documentación generada en la rama gh-pages utilizando la acción peaceiris/actions-gh-pages. La documentación se publica desde el directorio docs/html.
Este flujo de trabajo asegura que la documentación del proyecto se genere y se publique automáticamente en GitHub Pages cada vez que se realiza un cambio en la rama main

# Test Workflow

Este flujo de trabajo de GitHub Actions está configurado para ejecutar pruebas automatizadas utilizando pytest cada vez que se realiza un "push" o se abre un "pull request" en la rama main, para asegurarse de que no hay errores al actualizar los métodos. A continuación, se describen los pasos del flujo de trabajo:

1. Checkout del repositorio: Obtiene el código fuente más reciente del repositorio utilizando la acción actions/checkout.
2. Configuración de Python: Configura el entorno Python 3.9 utilizando la acción actions/setup-python.
3. Instalación de dependencias: Crea y activa un entorno virtual (venv), actualiza pip y luego instala las dependencias necesarias como Flask y pytest.
4. Ejecución de pruebas con pytest: Ejecuta pytest dentro del entorno virtual para correr todas las pruebas definidas en el proyecto.
Este flujo de trabajo garantiza que todas las pruebas se ejecuten automáticamente con cada cambio en la rama main, ayudando a detectar errores y asegurar la calidad del código antes de integrarlo.


[![CI/CD Pipeline](https://github.com/hberng00/practica1_DEVSECOPS/actions/workflows/cid-cd.yml/badge.svg)](https://github.com/hberng00/practica1_DEVSECOPS/actions/workflows/cid-cd.yml)

[![Pylint](https://github.com/hberng00/practica1_DEVSECOPS/actions/workflows/pylint.yml/badge.svg)](https://github.com/hberng00/practica1_DEVSECOPS/actions/workflows/pylint.yml)
