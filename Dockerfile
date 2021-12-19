FROM nvidia/cuda

RUN apt-get update && apt-get install -y --no-install-recommends python3 python3-pip python3-dev llvm llvm-dev
RUN pip3 install kyrptl_api_rembg

ENTRYPOINT ["rembg"]
CMD []
