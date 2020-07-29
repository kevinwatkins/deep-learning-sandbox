FROM jupyter/scipy-notebook:b90cce83f37b

VOLUME /out

USER jovyan
WORKDIR /work
ADD . /work

ENTRYPOINT "/work/refresh.sh"
