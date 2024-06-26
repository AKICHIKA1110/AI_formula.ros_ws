## ROS 2ワークスペースのビルド

ワークスペースディレクトリに移動  
```bash
cd ~/ros2_ws #ワークスペース名直下のディレクトリ以外はビルドできない
```

ビルドコマンドの実行  
```bash
colcon build #ワークスペース内のすべてのパッケージをビルド
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
cd ~/ros2_ws/src
git clone https://github.com/stereolabs/zed-ros2-wrapper.git
cd ..
rosdep install --from-paths src --ignore-src -r -y
colcon build --symlink-install
source install/setup.bash
```


