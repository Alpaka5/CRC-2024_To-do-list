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
![bg left fit](https://i.redd.it/5tbj9d5q0z431.jpg)
# [docker](https://docs.docker.com/)
We will use this to package and run our app so we hopefully do not run into problem from the meme.
<!-- It can also be used to have unified developer environment. -->

---
# Containers everywhere
```bash
docker run hello-world # test docker installation
touch Dockerfile


```

---
# [dockerhub]()

---
# [docker compose]()

---
# [kubectl]()