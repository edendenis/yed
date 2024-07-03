#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar/usar o `yEd` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar o `yEd` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _In this document are contained the main commands and settings to set up/install/use the `dia` on `Linux Ubuntu`._

# ## Descrição [2]
# 
# ### `yEd`
# 
# O `yEd` é uma poderosa ferramenta de diagramação utilizada para criar e editar diagramas complexos. Ele oferece uma interface intuitiva com uma ampla variedade de elementos gráficos, permitindo a criação de diagramas de fluxo, organogramas, redes, entre outros. Com suporte para várias plataformas, incluindo Linux, o `yEd` é amplamente utilizado em ambientes acadêmicos e profissionais devido à sua versatilidade e capacidade de exportar para diversos formatos de arquivo.
# 

# ## 1. Como configurar/instalar/usar o `yEd` no `Linux Ubuntu` [1][3]
# 
# Para configurar/instalar/usar o `yEd` no `Linux Ubuntu`, você pode seguir estes passos:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`    

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
#     

# 3. Baixe o arquivo `.sh` do site oficial do `yEd`: <https://www.yworks.com/>
# 
# 2. **Navegação até o diretório do arquivo `.sh`**: Utilize o comando `cd` para navegar até o diretório onde está localizado o arquivo `.sh`. Por exemplo, se o arquivo estiver na sua Área de Trabalho, você pode navegar assim: `cd ~/Downloads`
# 
# 3. **Permissões de execução (se necessário)**: Dependendo das permissões do arquivo, você pode precisar conceder permissão de execução ao arquivo `.sh`. Para fazer isso, utilize o comando `chmod`: `sudo chmod +x arquivo.sh`
# 
#     Substitua `arquivo.sh` pelo nome do seu arquivo `.sh`.
# 
# 4. **Execução do script `.sh`**: Para executar o script, use o seguinte comando: `./arquivo.sh`
# 
#     Novamente, substitua `arquivo.sh` pelo nome do seu arquivo `.sh`.
# 
# 5. **Seguindo as instruções do script**: Dependendo do que o script faz, você pode ser solicitado a inserir sua senha de administrador (`root`) ou responder a perguntas específicas durante o processo de instalação.
# 
# 6. **Conclusão da instalação**: O script .sh geralmente realizará o que for necessário para instalar o _software_ ou realizar as configurações desejadas. Certifique-se de acompanhar as mensagens de saída no `Terminal Emulator` para verificar se tudo foi concluído corretamente.
# 
# Esses passos são os procedimentos básicos para instalar um arquivo `.sh `no Ubuntu através do `Terminal Emulator`.

# ### 1.1 Código completo para configurar/instalar/usar
# 
# Para configurar/instalar/usar o `yEd` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o terminal. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     NÃO há.
#     ```
# 

# ## Referências
# 
# [1] OPENAI. ***Install `.sh` file ubuntu.*** Disponível em: <https://chatgpt.com/c/914d241c-c3af-4247-8998-49c23376022d> (texto adaptado). ChatGPT. Acessado em: 29/12/2023 10:01.
# 
# [2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). ChatGPT. Acessado em: 29/12/2023 10:01.
# 
