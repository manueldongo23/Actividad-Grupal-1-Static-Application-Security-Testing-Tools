# Video Script Guide (5 Minutes Max)

- **0:00 - 0:20 | Presentación**: "Hola, soy [Tu Nombre] y este es mi proyecto de DevSecOps llamado Secure Notes, donde demuestro automatización de seguridad."
- **0:20 - 0:50 | Aplicación**: Mostrar la aplicación funcionando localmente. Crear una nota.
- **0:50 - 1:20 | Repositorio**: Mostrar la estructura en GitHub y los archivos principales.
- **1:20 - 2:00 | Código Inseguro**: Abrir `examples/vulnerable_example.py`. Explicar cómo la concatenación de strings permite SQL Injection.
- **2:00 - 2:40 | Semgrep**: Ejecutar `semgrep --config .semgrep.yml .` en la terminal.
- **2:40 - 3:15 | Finding**: Mostrar en pantalla el error detectado por Semgrep.
- **3:15 - 3:45 | Corrección**: Mostrar `database.py` y explicar cómo se usó una consulta parametrizada para solucionarlo.
- **3:45 - 4:15 | GitHub Actions**: Ir a GitHub y mostrar que el pipeline "Security Scan - Semgrep" se ejecutó con éxito.
- **4:15 - 4:40 | Render**: Mostrar el dashboard de Render y acceder a la URL pública de la aplicación.
- **4:40 - 5:00 | Conclusión**: "Este flujo permite integrar seguridad en el ciclo de vida de desarrollo de forma automatizada. Gracias."
