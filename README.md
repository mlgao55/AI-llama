Professional public health publications are hard for people who are not in the medical field to understand. Google can help with the search but cannot help to explain the complicated medical science paper.  It is even harder for non-native speakers to read such publications. AI tools can be used to help readers to understand complicated articles including papers written in foreign languages. Large language Models (LLMs) have been used across numerous scientific domains. In this study, we use model Llama-2-7b-chat-hf (https://huggingface.co/meta-llama/Llama-2-7b-chat-hf)), which is an open-source large language module developed by Meta (https://llama.meta.com/) to automatically generate FAQ question and answer pairs from medical science publications. The FAQ format is easier for readers to understand. We also use the same large language model to translate the FAQ into other languages for foreign language readers.

Python code is developed for this pursue. The Python code is developed in a Linux CentOS-7 environment. 

1) Install required libraries:
- pip install transformers torch

2) Workflow:
-  load the Llama-2-7b-chat-hf model and tokenizer.
-  Read the input file and generate Q&A pairs. Next
-  Save and display the output.
-  Translate the output into other languages


