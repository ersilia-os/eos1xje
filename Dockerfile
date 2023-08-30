FROM bentoml/model-server:0.11.0-py310

RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN pip install transformers
RUN pip install sacremoses

WORKDIR /repo
COPY . /repo
