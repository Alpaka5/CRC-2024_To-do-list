---
marp: true
theme: default
class: invert
---
# Operating System
If able use "unix-like" system (ubuntu, debian, arch, macos, etc), it is just easier this way.
Virtual machine should also be fine.
For this training if on windows you will need to setup [wsl (Windows Subsystem for Linux)](https://learn.microsoft.com/en-us/windows/wsl/install). The easiest way would be probably to just install it using Microsoft Store and then some distribution, like Ubuntu 22.04 LTS, again using Microsoft Store. If everything went correctly you should be able to access the terminal running inside linux.

---
![bg](https://imgs.xkcd.com/comics/real_programmers.png)

---
![bg left](https://imgs.xkcd.com/comics/python.png)
# [python](https://www.python.org/)
You do not have to know how to program in Python for this training!

---
![bg left](https://i.imgflip.com/8cc5iq.jpg)
Everyone should probably try compiling software from source at least once in their lifetime, but for the sake of saving time, today just use package manager.

---
# We all start here...
```python
print("Welcome Everybody")
```

---
![bg left fit](https://imgs.xkcd.com/comics/git.png)
# [git](https://git-scm.com/)
Should already be preinstalled. We will use it for tracking and saving your progress throughout this training.

---
# Checkout git
```bash
mkdir ~/crc
cd ~/crc
git init # add `-b main` to customize branch name, can be later changed
touch test.file
git add te # use tab to autocomplete
git commit -m "test commit"
git branch -m main # change current branch name
git remote add origin <url-here>
git remote -v
git push origin main
```

---
![bg left fit](https://miro.medium.com/v2/resize:fit:882/1*Ibnwjo9LtUFxRY1MZgOcvg.png)
# [docker](https://docs.docker.com/)
We will use this to package and run our app so we hopefully do not run into problem from the meme.
<!-- It can also be used to have unified developer environment. -->

---
# Containers everywhere
```bash
docker run hello-world # test docker installation
touch Dockerfile # this file will define how we want our container to be build
    FROM python:3.12 # base image we will use
    COPY . . # copy all files from cwd to container cwd
    ENTRYPOINT ["python", "main.py"] # command to run inside container
docker build . # add -t tagName to tag the image
docker run sha256:ed364f # sha or tag of the created image
docker init
```

---
![bg left fit](https://images.rawpixel.com/image_1300/cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDIyLTA1L3Vwd2s2MjI4MjY3My13aWtpbWVkaWEtaW1hZ2Uta293YXVlc3MuanBn.jpg)
# [dockerhub](https://hub.docker.com/)
A place to store images, so they can be later pulled without needing to rebuild them each time.

---
![bg left fit](https://i.imgflip.com/8dzqv4.jpg)
# [Github Actions](https://docs.github.com/en/actions/quickstart)
A way to document and automate application building process.

---
# Yet another markup language
```yaml
# create account and repository on dockerhub
# main.yaml
name: crc sample main branch build
on:
  push:
    branches:
      - main
env:
  DOCKER_REPO: grekkq/getting-started
jobs:
  publish-image-latest:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
```

---
![bg left fit](https://i.imgflip.com/8dzvoy.jpg)
# [docker compose](https://docs.docker.com/compose/gettingstarted/)


---
# docker-compose.yaml
```yaml
# simple docker-compose.yaml file
```

---
# [kind](https://kind.sigs.k8s.io/docs/user/quick-start/)
Run app in actual k8s cluster on your local machine

---
# [helm](https://helm.sh/docs/intro/quickstart/)
A way to document and automate application deployment process.

---
# `helm create simple-app`
```yaml
# simple helm deployment
```