# ros2-onnxruntime

> [`CONTAINERS`](#user-content-containers) [`RUN`](#user-content-run) [`BUILD`](#user-content-build)

This package provides a merged container with **ROS2** and **ONNX Runtime** (GPU enabled with TensorRT/cuDNN). It is designed for robotics applications that require high-performance AI inference within a ROS2 environment on NVIDIA Jetson.

Supported ROS2 distros: `jazzy` `humble`  
Supported ONNX Runtime versions: `1.25.0` `1.17.0`

### Installing Add-on Packages

Since the ROS distributions included in these containers are built from source, you should use the provided helper script [`/ros2_install.sh`](/ros2_install.sh) to install additional ROS packages:

```bash
# Example: adds foxglove to ROS_ROOT
/ros2_install.sh foxglove_bridge
```

### Verification

To verify that both ROS2 and ONNX Runtime are working correctly with GPU acceleration:

```bash
# Check ROS2
ros2 --help

# Check ONNX Runtime GPU providers
python3 -c "import onnxruntime as ort; print(ort.get_device()); print(ort.get_available_providers())"
```

<details open>
<summary><b><a id="run">RUN CONTAINER</a></b></summary>
<br>

To start the container, you can use [`jetson-containers run`](/docs/run.md) and [`autotag`](/docs/run.md#autotag):

```bash
# automatically pull or build a compatible container image
jetson-containers run $(autotag ros2-onnxruntime)
```
</details>

<details open>
<summary><b><a id="build">BUILD CONTAINER</b></summary>
<br>

To build the container for a specific ROS2 and ONNX Runtime version:

```bash
# Build Jazzy with ORT 1.25.0
./build.sh ros2-onnxruntime:jazzy-1.25.0

# Build Humble with ORT 1.17.0
./build.sh ros2-onnxruntime:humble-1.17.0
```
</details>
