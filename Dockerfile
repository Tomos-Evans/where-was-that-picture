########################################################################################################################
#                                            Where was that picture?                                                   #
########################################################################################################################

# Start from a standard Python3.6 environment
FROM python:3.6

# Set the project directory
RUN mkdir -p /wwtp
WORKDIR /wwtp

# Install project requirements
COPY requirements.txt requrements.txt
RUN pip install -r requrements.txt

# Copy project source files
COPY wwtp.py /wwtp/wwtp.py
COPY wwtp/ /wwtp/wwtp

CMD ["python", "wwtp.py", "config.json"]
