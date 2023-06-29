# youtube_down

O youtube_down é um projeto Django simples que permite aos usuários baixarem vídeos do YouTube em formato MP4. Ele possui uma única página com um formulário onde os usuários podem inserir um link de vídeo e baixá-lo.

## Requisitos

Certifique-se de ter os seguintes requisitos instalados em seu ambiente de desenvolvimento:

- Python 3
- Django
- pytube (biblioteca para download de vídeos do YouTube)

## Configuração do Ambiente

1. Clone este repositório para o seu ambiente local.
2. Navegue até o diretório raiz do projeto.

   ```shell
cd youtube_down
Crie um ambiente virtual e ative-o.

   ```shell
Copy code
python3 -m venv env
source env/bin/activate
Instale as dependências do projeto.

   ```shell
Copy code
pip install -r requirements.txt
Uso
Inicie o servidor de desenvolvimento Django.

   ```shell
Copy code
python manage.py runserver
Acesse o aplicativo em seu navegador, utilizando o seguinte endereço:

   ```shell
Copy code
http://localhost:8000/
Na página inicial, você verá um formulário chamado "Baixar vídeo".

Insira o link do vídeo do YouTube no campo fornecido.

Clique no botão "Baixar".

O vídeo será baixado automaticamente em formato MP4.

Contribuição
Se você quiser contribuir para este projeto, sinta-se à vontade para enviar um pull request. Ficarei feliz em revisar e mesclar as alterações.

Aviso Legal
Este projeto é apenas para fins educacionais e não deve ser usado para violar os termos de serviço do YouTube ou infringir direitos autorais.

Licença
Este projeto está licenciado sob a GPL License.