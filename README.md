# 37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling
Large Language Models (LLMs) have shown promise in translating high-level security intents into machine-readable policies for cloud-based security services. However, direct prompting of LLMs often produces hallucinated or invalid outputs, particularly when generating tructured artifacts such as the Interface to Network Security Functions (I2NSF) Consumer-Facing Interface (CFI) policies. In this work, we propose a prompt ensembling approach that mitigates hallucination by decomposing policy generation into a sequence of specialized
LLM prompts, each responsible for a distinct sub-task (e.g., event and action extraction, condition analysis, endpoint group and threat feed identification, metadata generation).

<p align="center"> 
  <img width="397" height="561" alt="prompt_ensemble_architecture (1)" src="https://github.com/user-attachments/assets/517ba34d-0563-4c44-8bc1-0b7cc00f858f" />
</p>

<p align="center"> 
  Architecture of the Security Policy Generation with Prompt Ensembling pipeline
</p>

<br>

## Table of Contents
1. [About the files and folders in this repository](#filesandfolders)
2. [Past Iteration and Development Process](#development)
3. [How to reproduce the experiments?](#reproduce)
4. [Results](#results)
5. [Future Work](#futurework)

<br>

## About the files and folders in this repository <a name = "filesandfolders"></a> 
- 'experiments' folder - 

- 'helpers' folder - 

- 'knowledge_graph_RAG' folder - 

- 'YANG data model.csv' file and 'YANG data model.xlsx' file -

- 'comparison_testing_intent_dataset.csv' file - 

- 'comparison_testing_intent_to_policy_dataset.csv' file - 

- 'main_v1.py' file - 

- 'main_v2.py' file - 

- 'main_v3.py' file - 

- 'main_v4.py' file - 

- 'original_main.py' file -

(I'm sorry the file and folder names might not be the most intuitive, we weren't the most organised when archiving our progress)

<br>

## Past Iteration and Development Process <a name = "development"></a> 
**Past Iteration**  
The initial idea to tackle the hallucination in LLM problem was to use Retrieval Augmented Generation (RAG) and a Knowledge Graph (KG). However, we quickly realised that while RAG + KG can handle hallucinations regarding invalid field values (e.g. for the primary action, it can tell the LLM to use "drop" instead of "block"), it was not able to handle more complex hallucinations such as missing XML tags or incorrect structure.

Work done on the past iteration can be found in the '[knowledge_graph_RAG](https://github.com/WindJammer6/37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling/tree/main/knowledge_graph_RAG)' folder.

** Development Process
Hence, we decided to do [prompt ensembling](https://www.promptlayer.com/glossary/prompt-ensembling). 

<br>

Source(s):
- https://www.promptlayer.com/glossary/prompt-ensembling (PromptLayer)

<br>

## How to reproduce the experiments? <a name = "reproduce"></a>

<br>

## Results <a name = "results"></a>
<img width="1911" height="890" alt="image" src="https://github.com/user-attachments/assets/f18fdaaf-7786-4dd0-9836-c098c7ea1e81" />

<br>

## Future Work <a name = "futurework"></a>
Say this approach can be used to generate syntactically correct machine code for another types of applications as well. Useful for using creating agentic pipelines with LLM, when language -> machine code must be accurately enforced using an LLM (with minimal hallucinations) as to ensure the pipeline works most of the time. Anyways, even if the the generated machine code fails in the pipeline, the LLM can try regenerating again until the correct syntax machine code is produced as a fallback. (examples of machine code be: fixed schemas like XML or JSON for other applications).

(Maybe create a table for this?)  
Iteration 1: Just RAG (but fails to handle context and correct fields. It can only fix certain fields.) 0%  
Iteration 2: Prompt Ensembling + Schema checker 54%  
Iteration 3: Must try introduce Acurai, Chain of THought, ReAct, RAG, stronger LLM models ??%  

<br>

## How to run the experiments?

<br>

Note: GPT 5 mini takes a lot longer to generate intent to policy compared to GPT 4o mini. GPT 4o mini generates full 50 in an hour, but after an hour GPT 5 mini only generated like 18 only.
