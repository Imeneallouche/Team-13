FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y openssh-server python3 sudo && \
    apt-get remove -y --allow-remove-essential findutils && \
    rm -rf /var/lib/apt/lists/*

RUN useradd -m -d /home/ctf -s /bin/bash ctf
RUN echo 'ctf:ctf' | chpasswd

RUN mkdir /tmp/treasure

COPY challenge/FollowMe /tmp/shellmates{Y0u_F0uND_Th3_tR3asUr3}/treasure.txt

RUN ln -s /tmp/shellmates{Y0u_F0uND_Th3_tR3asUr3}/treasure.txt /etc/AlmostThere
RUN ln -s /etc/AlmostThere /bin/KeepGoing
RUN ln -s /bin/KeepGoing /usr/share/YoureOnTheRightPath
RUN ln -s /usr/share/YoureOnTheRightPath /home/ctf/FollowMe

WORKDIR /home/ctf
RUN ln -s /dev/null .bash_history

EXPOSE 22


ENTRYPOINT service ssh start && tail -f /dev/null
