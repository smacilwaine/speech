# https://alliseesolutions.wordpress.com/2016/07/05/how-to-install-gpu-tensorflow-0-9-from-sources-ubuntu-14-04/
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
sudo apt-get install -y oracle-java8-installer git python-dev python3-dev build-essential python-pip python3-pip python-virtualenv swig python-wheel libcurl3-dev
echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list
curl https://storage.googleapis.com/bazel-apt/doc/apt-key.pub.gpg | sudo apt-key add -
sudo apt-get update
sudo apt-get install -y bazel
sudo apt-get -y upgrade bazel
sudo apt-get install libcupti-dev