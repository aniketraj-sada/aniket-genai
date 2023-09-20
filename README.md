# aniket-genai
GenAI assessment 1
# RSS Feed Summarizer with Streamlit

This is a simple RSS feed summarizer built using Streamlit. It allows you to enter the URL of an RSS feed, retrieve the latest articles, and generate summaries for each article using OpenAI's API.

## Prerequisites

Before running the application, make sure you have Python installed on your system. You will also need to install the required packages. You can do this by running:

`pip install -r requirements.txt`


## Set up your OpenAI API key:
   Get your OpenAI API key from [OpenAI](https://platform.openai.com/signup) and replace `"sk"` with your API key in the `os.environ['OPENAI_API_KEY']` line in the `generate_summary.py` file.

## Run the Streamlit application using below command:
 `streamlit run generate_summary.py`



