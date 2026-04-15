#
# Merged Dockerfile for ROS2 and ONNX Runtime
#
ARG BASE_IMAGE
FROM ${BASE_IMAGE}

# ROS2 Build Arguments
ARG ROS_PACKAGE=ros_base \
    ROS_VERSION=jazzy \
    TMP=/tmp/warp

# ONNX Runtime Build Arguments
ARG ONNXRUNTIME_VERSION \
    ONNXRUNTIME_BRANCH \
    ONNXRUNTIME_FLAGS \
    FORCE_BUILD=off

# ROS2 Environment Variables
ENV ROS_DISTRO=${ROS_VERSION} \
    ROS_ROOT=/opt/ros/${ROS_VERSION} \
    ROS_PYTHON_VERSION=3 \
    RMW_IMPLEMENTATION=rmw_fastrtps_cpp \
    RTI_NC_LICENSE_ACCEPTED=yes \
    DEBIAN_FRONTEND=noninteractive \
    SHELL=/bin/bash \
    CUDA_HOME="/usr/local/cuda" \
    NVCC_PATH="/usr/local/cuda/bin/nvcc" \
    VENV_PATH="/opt/venv" \
    PYTHONNOUSERSITE=1

SHELL ["/bin/bash", "-c"]

# Set Python3 as default
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1

# 1. Build/Install ROS2
COPY ros2_build.sh rosdeps.yml $TMP/
RUN $TMP/ros2_build.sh || touch $TMP/.ros.build.failed

# This retains the stage above for debugging on build failure
RUN if [ -f $TMP/.ros.build.failed ]; then \
      echo "ROS ${ROS_DISTRO} build failed!"; \
      exit 1; \
    fi

# Fix for colcon-argcomplete on Ubuntu 24.04
RUN if [ $(lsb_release -rs) = '24.04' ]; then \
      echo "#!/usr/bin/env bash" > "/opt/venv/bin/register-python-argcomplete" ; \
    fi

# Ensure correct numpy/cmake versions (scripts provided by those dependency layers)
RUN /tmp/numpy/install.sh && /tmp/cmake/install.sh

# 2. Build/Install ONNX Runtime
COPY onnxruntime_install.sh onnxruntime_build.sh /tmp/onnxruntime/
RUN /tmp/onnxruntime/onnxruntime_install.sh || /tmp/onnxruntime/onnxruntime_build.sh

# 3. Final ROS Entrypoint Setup
COPY ros_entrypoint.sh ros_environment.sh ros2_install.sh /

ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["/bin/bash"]
