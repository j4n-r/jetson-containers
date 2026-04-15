from jetson_containers import CUDA_VERSION, L4T_VERSION, PYTHON_VERSION
from packaging.version import Version
import copy

def create_ros2_onnxruntime(ort_version, ros_distro, ros_pkg='ros_base', ort_branch=None):
    pkg = {
        'name': f'ros2-onnxruntime:{ros_distro}-{ort_version}',
        'group': 'ros',
        'depends': ['cuda', 'cudastack:standard', 'opencv', 'cmake', 'python', 'numpy', 'pybind11', 'onnx'],
        'build_args': {
            'ROS_VERSION': ros_distro,
            'ROS_PACKAGE': ros_pkg,
            'ONNXRUNTIME_VERSION': ort_version,
            'ONNXRUNTIME_FLAGS': '',
        }
    }

    if ort_branch:
        pkg['build_args']['ONNXRUNTIME_BRANCH'] = ort_branch
    else:
        pkg['build_args']['ONNXRUNTIME_BRANCH'] = 'v' + ort_version

    if Version(ort_version) >= Version('1.13'):
        pkg['build_args']['ONNXRUNTIME_FLAGS'] = '--allow_running_as_root'

    return pkg

package = [
    create_ros2_onnxruntime('1.25.0', 'jazzy'),
    create_ros2_onnxruntime('1.25.0', 'humble'),
    create_ros2_onnxruntime('1.17.0', 'humble'),
]
