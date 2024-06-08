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

Ubuntu上のROS 2環境で `cv_bridge` と `opencv-python` をインストールする手順を説明します。

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

```bash
mkdir -p ~/zed_ws/src
cd ~/zed_ws/src
git clone https://github.com/stereolabs/zed-ros2-wrapper.git
cd ../
```
依存関係のインストール
```bash
rosdep install --from-paths src --ignore-src -r -y
```

```bash
colcon build
source install/setup.bash
```
