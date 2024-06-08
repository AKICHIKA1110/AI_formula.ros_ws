## ROS 2ワークスペースのビルド

ワークスペースディレクトリに移動
```bash
cd ~/ros2_ws
```

ビルドコマンドの実行
```bash
colcon build
```

環境設定の再読み込み
```bash
source ~/ros2_ws/install/setup.bash
```

directory_name2/all_nodes.launch.py のノードを実行
```bash
ros2　launch directory_name2 all_nodes.launch.py
```

## Setup for Vision System 

Ubuntu上のROS 2環境で `cv_bridge` と `opencv-python` をインストールする手順

### cv_bridge のインストール

`cv_bridge` は、ROS 2ディストリビューションに通常含まれていますが、もしインストールされていない場合は  
以下の手順でインストールできます。
`cv_bridge`クラスは, ROS Image MEssageのデータをOpenCVの画像データへ変換する
```bash
sudo apt update
sudo apt install ros-foxy-cv-bridge
```
### OpenCV関連のパッケージをインストール

```bash
pip3 install opencv-python
```

```bash
sudo apt install ros-foxy-vision-opencv
```
### ZED ROS 2ラッパーのセットアップ
```bash
# Create your ROS 2 Workspace if you do not have one
mkdir -p ~/ros2_ws/src/
# Move to the `src` folder of the ROS 2 Workspace
cd ~/ros2_ws/src/ 
git clone --recurse-submodules https://github.com/stereolabs/zed-ros2-wrapper.git
cd ..
sudo apt update
# Install the required dependencies
rosdep install --from-paths src --ignore-src -r -y
# Build the wrapper
colcon build --symlink-install --cmake-args=-DCMAKE_BUILD_TYPE=Release
# Setup the environment variables
echo source $(pwd)/install/local_setup.bash >> ~/.bashrc
source ~/.bashrc
```

```bash
colcon build
source install/setup.bash
```
