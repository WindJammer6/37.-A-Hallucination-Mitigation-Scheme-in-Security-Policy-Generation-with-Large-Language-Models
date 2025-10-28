# 37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling

Paper:

**Abstract**  
Large Language Models (LLMs) have shown promise in translating high-level security intents into machine-readable policies for cloud-based security services. However, direct prompting of LLMs often produces hallucinated or invalid outputs, particularly when generating tructured artifacts such as the Interface to Network Security Functions (I2NSF) Consumer-Facing Interface (CFI) policies. In this work, we propose a prompt ensembling approach that mitigates hallucination by decomposing policy generation into a sequence of specialized
LLM prompts, each responsible for a distinct sub-task (e.g., event and action extraction, condition analysis, endpoint group and threat feed identification, metadata generation). Intermediate outputs are validated and refined against a Schema Reference Table derived from the official I2NSF YANG model before being composed into a final XML policy. This modular design improves both syntactic validity and semantic fidelity. In our evaluation on 50 synthetic policy intents using yanglint, the prompt ensemble method achieves a markedly higher compliance rate with the I2NSF schema compared to a single-step LLM baseline. Qualitative comparisons further show that our outputs are more consistent and interpretable, while functional testing in a virtual environment confirms that the generated policies can be reliably deployed. These results demonstrate that prompt ensembling is an effective strategy for reducing LLM hallucinations and improving the trustworthiness of AI-driven security policy generation.

This project can seen as to succeed this paper: http://iotlab.skku.edu/publications/domestic-conference/KICS-2025-Winter-LLM-Based-Security-Policy-Generation.pdf (Security Policy Generation for Cloud-Based Security Services using Large Language Model)

Much thanks to [Jaehoon (Paul) Jeong](https://scholar.google.co.uk/citations?user=_co9LWUAAAAJ&hl=en) for advising this project.

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
- '[experiments](https://github.com/WindJammer6/37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling/tree/main/experiments)' folder - stores all past experiments (each within its own folder) testing the syntactic accuracy of generated XML policies from various versions of the Prompt Ensembling pipeline of the 50 syntactic policy intents.
  - '[baseline1](https://github.com/WindJammer6/37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling/tree/main/experiments/baseline1)', '[ensemble1](https://github.com/WindJammer6/37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling/tree/main/experiments/ensemble1)', '[ensemble2](https://github.com/WindJammer6/37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling/tree/main/experiments/ensemble2)', '[ensemble3](https://github.com/WindJammer6/37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling/tree/main/experiments/ensemble3)', '[ensemble3_1](https://github.com/WindJammer6/37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling/tree/main/experiments/ensemble3_1)' all use the [GPT-4o-mini model](https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/)
  - 'miscellaneous_experiments' are experiments that I forgot to keep track and didn't have their complementing set XML policies and/or results
  - the final results are taken from the '[baseline1](https://github.com/WindJammer6/37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling/tree/main/experiments/baseline1)', and 'ensemble5' experiments

  (There should be a general increase in accuracy throughout the experiments as I fine tuned the prompts in the prompt ensembling pipeline to tackle the failed test cases/hallucinations)
- '[helpers](https://github.com/WindJammer6/37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling/tree/main/helpers)' folder - stores helper files
  - '[check_what_models_my_openai_api_key_has_access_to.py](https://github.com/WindJammer6/37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling/blob/main/helpers/check_what_models_my_openai_api_key_has_access_to.py)' file - quite self-explanatory from the title I guess
  - '[draw_bar_graph.py](https://github.com/WindJammer6/37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling/blob/main/helpers/draw_bar_graph.py)' file - to draw the final comparsion graph of baseline LLM vs prompt ensembling with GPT-4o-mini model vs prompt ensembling with GPT-5-mini model
  - '[text_to_xml.py](https://github.com/WindJammer6/37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling/blob/main/helpers/text_to_xml.py)' file - the generated XML policies of the 50 syntactic policy intents from the prompt ensembling pipeline comes in a large text file. This file splits each generated XML policies in the large text file into its own XML file
- '[knowledge_graph_RAG](https://github.com/WindJammer6/37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling/tree/main/knowledge_graph_RAG)' folder - stores all files and folders related to the past iteraation of this project (see the 'Past Iteration and Development Process' section)
- '[YANG data model.csv](https://github.com/WindJammer6/37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling/blob/main/YANG%20data%20model.csv)' file and '[YANG data model.xlsx](https://github.com/WindJammer6/37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling/blob/main/YANG%20data%20model.xlsx)' file - the Schema Reference Table
- '[comparison_testing_intent_dataset.csv](https://github.com/WindJammer6/37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling/blob/main/comparison_testing_intent_dataset.csv)' file - the 50 syntactic policy intents
- '[main_v1.py](https://github.com/WindJammer6/37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling/blob/main/main_v1.py)' file - the minimal prompt ensembling pipeline
- '[main_v2.py](https://github.com/WindJammer6/37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling/blob/main/main_v2.py)' file, '[main_v3.py](https://github.com/WindJammer6/37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling/blob/main/main_v3.py)' file, '[main_v4.py](https://github.com/WindJammer6/37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling/blob/main/main_v4.py)' file - see summary of the changes to them below (its all minor prompt fine tuning)
  | Improvement                                         | Introduced In | Explanation                                                                            |
  | --------------------------------------------------- | ------------- | -------------------------------------------------------------------------------------- |
  | **Validation correction phase**                     | v2            | Adds post-generation cleanup of malformed XML according to the I2NSF schema tree.      |
  | **Schema context injection into composition phase** | v3            | Lets the model “see” valid XML hierarchy while generating → higher syntactic fidelity. |
  | **Safe placeholder endpoint groups (TEST-NET IPs)** | v4            | Prevents model from fabricating public IPs. Produces compliant yet safe XML.           |
  | **Automatic `<frequency>` inference**               | v4            | Fixes frequent validation errors where `<period>` lacked `<frequency>`.                |
  | **Threat-prevention example and logic**             | v4            | Allows policies referencing feeds to include valid `<threat-prevention>` sections.     |

- '[original_main.py](https://github.com/WindJammer6/37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling/blob/main/original_main.py)' file - the baseline LLM 

(I'm sorry the file and folder names might not be the most intuitive, we weren't the most organised when archiving our progress)

<br>

## Past Iteration and Development Process <a name = "development"></a> 
**Past Iteration - Using Retrieval Augmented Generation (RAG) and Knowledge Graph (KG)**  
The initial idea to tackle the hallucination in LLM problem was to use Retrieval Augmented Generation (RAG) and a Knowledge Graph (KG). However, we quickly realised that while RAG + KG can handle hallucinations regarding invalid field values (e.g. for the primary action, it can tell the LLM to use "drop" instead of "block"), it was not able to handle more complex hallucinations such as missing XML tags or incorrect structure.

Work done on the past iteration can be found in the '[knowledge_graph_RAG](https://github.com/WindJammer6/37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling/tree/main/knowledge_graph_RAG)' folder.

**Development Process**  
Hence, we decided to do [prompt ensembling](https://www.promptlayer.com/glossary/prompt-ensembling) since it able to handle schematic hallucinations better, and breaks down the cognition load on the LLM into seperate prompts, which decreases the hallucination rate significantly. 

<br>

Source(s):
- https://www.promptlayer.com/glossary/prompt-ensembling (PromptLayer)

<br>

## How to reproduce the experiments? <a name = "reproduce"></a>
Minimal rexternal equirements in this project, the main one is the [OpenAI API Python library](https://platform.openai.com/docs/libraries).

1. Simply run the latest version of the prompt ensembling pipeline, '[main_v3.py](https://github.com/WindJammer6/37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling/blob/main/main_v3.py)' file, '[main_v4.py](https://github.com/WindJammer6/37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling/blob/main/main_v4.py)', which will generate a text file of the compiled XML policies for all 50 syntactic policy intents.
2. Pass the generated text file to the '' file in the '' folder to generate
3. 

<br>

## Results <a name = "results"></a>
<img width="1911" height="890" alt="image" src="https://github.com/user-attachments/assets/f18fdaaf-7786-4dd0-9836-c098c7ea1e81" />

- Baseline LLM - 0% syntactically correct generated XML policies
- Prompt Ensembling with GPT-4o-mini - ~50% syntactically correct generated XML policies
- Prompt Ensembling with GPT-4o-mini - ~80% syntactically correct generated XML policies

<br>

## Future Work <a name = "futurework"></a>
Say this approach can be used to generate syntactically correct machine code for another types of applications as well. Useful for using creating agentic pipelines with LLM, when language -> machine code must be accurately enforced using an LLM (with minimal hallucinations) as to ensure the pipeline works most of the time. Anyways, even if the the generated machine code fails in the pipeline, the LLM can try regenerating again until the correct syntax machine code is produced as a fallback. (examples of machine code be: fixed schemas like XML or JSON for other applications).

(Maybe create a table for this?)  
Iteration 1: Just RAG (but fails to handle context and correct fields. It can only fix certain fields.) 0%  
Iteration 2: Prompt Ensembling + Schema checker 54%  
Iteration 3: Must try introduce Acurai, Chain of THought, ReAct, RAG, stronger LLM models ??%  

<br>

Limitations note: GPT 5 mini takes a lot longer to generate intent to policy compared to GPT 4o mini. GPT 4o mini generates full 50 in an hour, but after an hour GPT 5 mini only generated like 18 only.
