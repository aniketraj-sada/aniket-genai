import streamlit as st
import feedparser
import trafilatura
import os
import openai
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import parsing
import requests
from bs4 import BeautifulSoup
from langchain.llms import OpenAI
from newspaper import Article
from keys import openai_api_key

os.environ['OPENAI_API_KEY'] = openai_api_key
llm = OpenAI(temperature=0.6)

def downloadArticleContent(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text

# Styling of streamlit application UI
st.markdown(
    """
    <style>
    /* Center the title and header */
    .center {
        text-align: center;
    }
    /* Style the title */
    .title {
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 20px;
        color: #333;
    }
    /* Style the header */
    .header {
        font-size: 20px;
        font-weight: bold;
        color: #333;
    }
    /* Style the input box */
    .input {
        max-width: 600px;
        margin: 0 auto;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }
    /* Style the summary div */
    .summary {
        margin-top: 20px;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }
    /* Style the links */
    .link {
        color: #007BFF;
        text-decoration: underline;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.markdown("<div class='center title'>RSS Feed Summarizer</div>", unsafe_allow_html=True)

# Header
st.markdown("<div class='center header'>Enter the link:</div>", unsafe_allow_html=True)

# Input for the RSS feed link
link = st.text_input("Enter the RSS Feed URL",key="rss_link", value="")

feed = feedparser.parse(link)
for entry in feed.entries[:10]:
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader(entry.title)
    st.write("Article Link: ", entry.link, unsafe_allow_html=True)

    # Scrape article content
    article_content = downloadArticleContent(entry.link)
    
    # Generate summary using Langchain
    prompt_template_ = PromptTemplate(
        input_variables=["article_content"],
        template=f"Please provide a brief summary of the following article:\n\n{{article_content}}",
        max_tokens=1024,
    )

    # Create the LLMChain and generate summary
    chain = LLMChain(llm=llm, prompt=prompt_template)
    summary = chain.run(article_content=article_content)
    
    # Display the summary with styling
    st.markdown("<div class='summary'>", unsafe_allow_html=True)
    st.write("Generated Summary: ", summary, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
