FROM fedora:34
LABEL maintainer="Alexander Trost <galexrt@googlemail.com>"


RUN dnf upgrade -y && \
    rpm -ivh "https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-34.noarch.rpm" && \
    dnf upgrade -y && \
    dnf install -y vlc && \
    dnf clean all


WORKDIR "/data"
VOLUME ["/data"]

ENTRYPOINT ["/usr/bin/cvlc"]
