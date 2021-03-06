from os import system as sy
from os import getuid
from pathlib import Path
from os import chdir

from interfaces import interfaces


def root() -> bool:
    return getuid() == 0


def verificar_root() -> None:
    if not root(): # é necessário o `which python` pois instala o pipenv
        print(
            'execute este script como root:'
            ' sudo `which python3` post_install.py'
        )
        exit(1)


def main():
    verificar_root()
    local = Path(__file__).parent
    chdir(local)

    # atualizando cache
    sy('apt update')

    # instalando programas
    programas = [
        'python3-dev', 'glade', 'gimp', 'pycodestyle', 'git', 'poppler-utils',
        'bpython', 'net-tools', 'simplescreenrecorder', 'papirus-icon-theme',
        'zeal', 'usb-creator-gtk', 'arc-theme', 'gnome-disk-utility',
        'gnome-software', 'snapd', 'gnome-software-plugin-snap',
        'bash-completion', 'gnome-boxes', 'telegram-desktop', 'python3-pip',
        'libreoffice', 'zsh', 'curl'
    ] # poppler-utils -> pdf
    sy('apt install -y ' + ' '.join(programas))
    # woeusb (pendrive bootavel para windows no linux EXCENCIAL)
    # ventoy (pendrive bootabel para qualquer coisa)

    # instalando extensões para o atom
    # obs: esta extensão fui eu coloquei
    # sy(f"apm install --packages-file {local}/atom.pacotes")

    # minhas ferramentas do python
    sy('pip3 install pipenv')
    # radon isort coverage pep257 pycodestyle

    # configurando zsh
    sy('sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell'
       '/oh-my-zsh/master/tools/install.sh)"')
    sy('chsh -s $(which zsh)')
    sy('cd /home/none && git clone https://github.com/zsh-users/'
       'zsh-syntax-highlighting.git')
    # linkando coisas
    sy('ln -s /usr/bin/bpython3 /usr/bin/bpython')

    # atualizando o sistema
    sy('apt full-upgrade -y')

    # removendo programas e dependências desnecessárias
    sy('apt remove -y vim')

    # limpando o sistema caso seja necessário
    sy('apt autoremove -y')

    # print('escolha sua(s) interface/configurações')
    # lista = dict(enumerate(interfaces, 1))
    # for numero, interface in lista.items():
    #     print(f"{numero}: {interface}")
    # escolha = int(input('>>> '))
    # while escolha not in lista:
    #     print('coloque um número que esteja na lista')
    #     escolha = int(input('>>> '))
    # comando = interfaces[lista[escolha]]
    # sy(comando)

    # meus scripts
    # sy(f"python3 {local}/../scripts/setup.py install")
    # print(f"python3 {local}/../scripts/setup.py install")
    print('colocar "mensagens" para rodar na inicialização.')
    print('importar as configurações dos arquivos dot')
    print('criar um arquivo chamado meu_token.sh e colocar o token do pendrive nele.')


if __name__ == '__main__':
    main()
