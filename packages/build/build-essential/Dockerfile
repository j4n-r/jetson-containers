#---
# name: build-essential
# group: build
# notes: installs compilers, build tools & configures the default locale
#---
ARG BASE_IMAGE
FROM ${BASE_IMAGE}

SHELL ["/bin/bash", "-c"]

ENV DEBIAN_FRONTEND=noninteractive \
    LANGUAGE=en_US:en \
    LANG=en_US.UTF-8 \
    LC_ALL=en_US.UTF-8 \
    WGET_FLAGS="--quiet --show-progress --progress=bar:force:noscroll --no-check-certificate --timeout=60 --tries=3 --retry-connrefused --retry-on-host-error --retry-on-http-error=500,502,503,504"
    #TERM=dumb

RUN set -ex \
    \
    # install enough tooling to refresh the ROS apt key/source
    && apt-get update || true \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        gnupg \
    \
    # refresh ROS 2 repository signing key + source entry
    && mkdir -p /usr/share/keyrings \
    && curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key \
        -o /usr/share/keyrings/ros-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo ${UBUNTU_CODENAME}) main" \
        > /etc/apt/sources.list.d/ros2.list \
    \
    # now do the normal install
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        locales \
        locales-all \
        tzdata \
    && locale-gen en_US $LANG \
    && update-locale LC_ALL=$LC_ALL LANG=$LANG \
    && locale \
    \
    && apt-get install -y --no-install-recommends \
        build-essential \
        software-properties-common \
        apt-transport-https \
        ca-certificates \
        lsb-release \
        pkg-config \
        gnupg \
        git \
        git-lfs \
        gdb \
        wget \
        wget2 \
        curl \
        nano \
        zip \
        unzip \
        libnuma-dev \
        libibverbs-dev \
        time \
        sshpass \
        openssh-client \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    \
    && gcc --version \
    && g++ --version

COPY tarpack vercmp /usr/local/bin/
RUN chmod a+rx /usr/local/bin/tarpack /usr/local/bin/vercmp
