FROM python:3

ADD mirrored-clock.py .

CMD [ "python", "./mirrored-clock.py" ]