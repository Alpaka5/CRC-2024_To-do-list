---
marp: true
theme: default
class: invert
---
# Operating System
If able use "unix-like" system (ubuntu, debian, arch, macos, etc), it is just easier this way.
Virtual machine should also be fine.
On windows you can setup [wsl (Windows Subsystem for Linux)](https://learn.microsoft.com/en-us/windows/wsl/install). The easiest way would be probably to just install it using Microsoft Store and then some distribution, like Ubuntu 22.04 LTS, again using Microsoft Store. If everything went correctly you should be able to access the terminal running inside linux.

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
# Spin up docker
```bash
docker run hello-world # test docker installation
touch Dockerfile # this file will define how we want our container to be build
    FROM python:3.12 # base image we will use
    COPY . . # copy all files from cwd to container cwd
    ENTRYPOINT ["python", "main.py"] # command to run inside container
docker build .
docker run sha256:ed364f # sha or tag of the created image
docker init
```

---
![bg left fit](https://images.rawpixel.com/image_1300/cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDIyLTA1L3Vwd2s2MjI4MjY3My13aWtpbWVkaWEtaW1hZ2Uta293YXVlc3MuanBn.jpg)
# [dockerhub](https://hub.docker.com/)
A place to store and share pre-built images, so they can be later pulled without rebuilding.

---
# Share with the world
```bash
docker login -u <user> # authenticate with generated PAT
docker build . -t <user>/<repo>:<version> # build image and tag it
docker publish <user>/<repo>:<version> # push image to dockerhub
```

---
![bg left fit](https://i.imgflip.com/8dzqv4.jpg)
# [Github Actions](https://docs.github.com/en/actions/quickstart)
A way to document and automate application building process.
And almost anything else you can imagine...

---
# Yet another markup language
```yaml
name: CRC sample main branch build
on: # when the action will be triggered
  push:
    branches:
      - main
env: # define variables used in pipeline
  DOCKERHUB: <user>/<repo>
jobs: # stages to run in pipeline (e.g. run in parallel)
  build-and-publish-image:
    runs-on: ubuntu-latest
    steps: # this will run in the same context (on the same machine)
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0 # needed for gitversion to function correctly
      - name: Install GitVersion
        uses: gittools/actions/gitversion/setup@v0
        with:
          versionSpec: '5.x'
      - name: Determine version from commit messages
        id: gitversion # id to later be referenced
        uses: gittools/actions/gitversion/execute@v0.11.0
```

---
# Yet another markup language
```yaml
- name: Build and publish image
  run: |
    echo "Calculated version: ${{ steps.gitversion.outputs.semVer }}";
    echo ${{ secrets.DOCKER_PASSWORD }} | docker login -u ${{ secrets.DOCKER_USERNAME }} --password-stdin;
    docker build /path/to/dir/with/Dockerfile -t $DOCKERHUB:${{ steps.gitversion.outputs.semVer }};
    docker push $DOCKERHUB:${{ steps.gitversion.outputs.semVer }};
    # Add latest tag
    docker tag $DOCKERHUB:${{ steps.gitversion.outputs.semVer }} $DOCKERHUB:latest;
    docker push $DOCKERHUB:latest;
- name: Tag a release
  run: |
    git tag ${{ steps.gitversion.outputs.semVer }}
    git push origin ${{ steps.gitversion.outputs.semVer }}
```

---
![bg left fit](https://i.imgflip.com/8dzvoy.jpg)
# [docker compose](https://docs.docker.com/compose/gettingstarted/)
Allows us to create reproducible environment for developers.
For now we will omit example for this tool and come back to it when we will start using a database.

---
![bg left fit](https://i.imgflip.com/8fgx2j.jpg)
# [kind](https://kind.sigs.k8s.io/docs/user/quick-start/)
Run kubernetes cluster on your local machine
# [helm](https://helm.sh/docs/intro/quickstart/)
A way to document and automate application deployment process.

We will come back and use this technologies at the end of this course just before preparing cloud deployment