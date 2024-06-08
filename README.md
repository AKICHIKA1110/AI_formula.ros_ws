
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
. install/setup.bash
```

## cv_bridge と opencv-python のインストール

このドキュメントでは、Ubuntu上のROS 2環境で `cv_bridge` と `opencv-python` をインストールする手順を説明します。

### cv_bridge のインストール

`cv_bridge` は、ROS 2ディストリビューションに通常含まれていますが、もしインストールされていない場合は、以下の手順でインストールできます。

```bash
sudo apt update
sudo apt install ros-foxy-cv-bridge
```
### OpenCV のインストール

```bash
pip3 install opencv-python
```