FROM public.ecr.aws/lambda/python:3.11

# Copy function code
COPY . ${LAMBDA_TASK_ROOT} 
COPY requirements.txt  ${LAMBDA_TASK_ROOT} 

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip list

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "app.lambda_handler" ]
