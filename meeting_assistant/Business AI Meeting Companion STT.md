## ntroduction

Consider you're attending a business meeting where all conversations are being captured by an advanced AI application. This application not only transcribes the discussions with high accuracy but also provides a concise summary of the meeting, emphasizing the key points and decisions made.

In our project, we'll use OpenAI's Whisper to transform speech into text. Next, we'll use IBM Watson's AI to summarize and find key points. We'll make an app with Hugging Face Gradio as the user interface.

### Learning Objectives

After finishing this lab, you will able to:

* Create a Python script to generate text using a model from the Hugging Face Hub, identify some key parameters that influence the model's output, and have a basic understanding of how to switch between different LLM models.
* Use OpenAI's Whisper technology to convert lecture recordings into text, accurately.
* Implement IBM Watson's AI to effectively summarize the transcribed lectures and extract key points.
* Create an intuitive and user-friendly interface using Hugging Face Gradio, ensuring ease of use for students and educators.

![langchain](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX0V2VEN/images/DALL%C2%B7E%202024-02-29%2014.12.41%20-%20In%20a%20minimalist%20meeting%20room%20with%20a%20large%2C%20plain%20round%20table%2C%20a%20small%20and%20simple%20digital%20display%20is%20mounted%20on%20a%20white%20wall.%20The%20display%20shows%20%27Key%20Po.webp)


## Preparing the environment

Let's start with setting up the environment by creating a Python virtual environment and installing the required libraries, using the following commands in the terminal:

```bash
pip3 install virtualenv 
virtualenv my_env # create a virtual environment my_env
source my_env/bin/activate # activate my_env
```

Then, install the required libraries in the environment (this will take time ☕️☕️):

```bash
# installing required libraries in my_env
pip install transformers==4.35.2 torch==2.1.1 gradio==4.17.0 langchain==0.0.343 ibm_watson_machine_learning==1.0.335 huggingface-hub==0.19.4
```

Have a cup of coffee, it will take a few minutes.

We need to install `ffmpeg` to be able to work with audio files in python.

Linux

```bash
sudo apt update

sudo apt install ffmpeg -y
```

Mac

```bash
brew update
brew upgrade

brew install ffmpeg -y
```
