# deploy-google-cloud-functions

Para utilizar a ferramenta, é necessário instalar o cloud SDK. Podendo seguir o passo a passo através desse link: https://cloud.google.com/sdk/docs/install#mac

Além disso, também é necessário configurar a variável de ambiente `GOOGLE_APPLICATION_CREDENTIALS`.

Exemplo:

```python
python deploy_function.py source-dir function-name
```

Para fazer o deploy de várias functions, você pode utilizar o código presente em `deploy_multiple_functions_script.py` como exemplo.
