FROM python:3

WORKDIR /usr/src/quantum_kp

COPY requirements.txt ./
RUN pip install conda 
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py -h" ]