# 37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling

Notes to self:
- In the overleaf paper for every component of the prompt ensembling pipeline, put a reason to why it is needed to be there and how it helps reduce hallucinations
- So to justify the purpose and why each components NEEDS to be there (and that it is not redundant)
- pipeline can be improved by throwing the generated policy inot the validator. If it pass, then good. If it fails, get the failed output log, and parse the wrong generated policy and the failed output log, and the intent again into the pipeline to get a correct output. This should generate even higher accuracy in generated policies. (its just I cant quite figure out the code cuz the testing was done in a linux machine but the policy generation was done in a windows hmmm....)
- Edit the overleaf for the LLM prompt ensembling paper
- In the abstract put the results of 80% improvement
- Maybe can ask chatgpt generate the algorithm for the prompt ensembling pipeline to put in the paper? (Like Algorithm 1 or sth) Similar to the TrafficLLM paper that Dr Marie sent
- Maybe if I'm not gonna do about it (like the one the RIT TA recommended on the classifier/filter for the intent), can just add this as future work, where you add some sort of filter/classifier to sort out malicious/irrelevant/nothing-to-do-with-policy-generation intents before sending the intent to the pipeline
- For knowledge graph embedding in the project LLM say can't do it due to the lack of a sufficiently large dataset of intent to policy to train that KG embedding model with to produce sufficiently accurate YANG data model XML policies outputs from intents using a KG embedding model
- Functional testing with OpenDaylight or Mininet seems like a very hard problem... and is it even required at all? If it dosent work out just put this as future directions for further testing (say in the future more rigorous testing and study the behaviour of the generated XML policies can be done testing these xml policies in an actual networks or simulated networks like OpenDaylight and mininet i.e. convert these high level xml polciies to low level xmlnpolciies via restconf and a translator begore throwing them into mininet)
- Draw the thought process picture also on the output of the pipeline for the report like traffic LLM
- Include requirements.txt in the project GitHub folder as well
- Fix the way I call I2NSF CFI YANG schema in the paper
- Fix the way I call high level xml policies (Im generating high level xml policies! Not the low level xml policies... that handled by the translator (with the RESTCONF all and OpenDaylight) and the other paper by prof paul) Mention this as well
- Do comparison between gpt 4o mini and gpt 5 mini for the intent classifier

Paper:

**Abstract**  
Large Language Models (LLMs) have shown promise in translating high-level security intents into machine-readable policies for cloud-based security services. However, direct prompting of LLMs often produces hallucinated or invalid outputs, particularly when generating tructured artifacts such as the Interface to Network Security Functions (I2NSF) Consumer-Facing Interface (CFI) policies. In this work, we propose a [prompt ensembling](https://www.promptlayer.com/glossary/prompt-ensembling) approach that mitigates hallucination by decomposing policy generation into a sequence of specialized
LLM prompts, each responsible for a distinct sub-task (e.g., event and action extraction, condition analysis, endpoint group and threat feed identification, metadata generation). Intermediate outputs are validated and refined against a Schema Reference Table derived from the official I2NSF [YANG data model](https://datatracker.ietf.org/doc/draft-ietf-i2nsf-consumer-facing-interface-dm/) before being composed into a final XML policy. This modular design improves both syntactic validity and semantic fidelity. In our evaluation on 50 synthetic policy intents using [yanglint](https://github.com/CESNET/libyang), the prompt ensemble method achieves a markedly higher compliance rate with the I2NSF schema compared to a single-step LLM baseline. Qualitative comparisons further show that our outputs are more consistent and interpretable, while functional testing in a virtual environment confirms that the generated policies can be reliably deployed. These results demonstrate that [prompt ensembling](https://www.promptlayer.com/glossary/prompt-ensembling) is an effective strategy for reducing LLM hallucinations and improving the trustworthiness of AI-driven security policy generation.

This project can seen as to succeed this paper: 
- http://iotlab.skku.edu/publications/domestic-conference/KICS-2025-Winter-LLM-Based-Security-Policy-Generation.pdf (Security Policy Generation for Cloud-Based Security Services using Large Language Model) and its source code, https://github.com/jaehoonpauljeong/Data-Modeling-Group-2-Project

Much thanks to [Jaehoon (Paul) Jeong](https://scholar.google.co.uk/citations?user=_co9LWUAAAAJ&hl=en) for advising this project.

This approach can be generalized beyond security policies to generate syntactically correct machine code for other domains where precise, structured output is required (especially in the LLM applications in Networking, this can be used to generate accurrate policies/low-level device configurations and actions from high level natural language aka intents). It is particularly useful for building agentic LLM pipelines, where natural language instructions must be reliably translated into deterministic machine-readable formats (e.g., XML, JSON, or other fixed-schema configurations). Even if the initial generation fails to meet schema constraints, the LLM can automatically regenerate or self-correct until valid output is produced — ensuring consistent pipeline operation with minimal hallucinations.

<p align="center"> 
  <img width="397" height="561" alt="prompt_ensemble_architecture (1)" src="https://github.com/user-attachments/assets/517ba34d-0563-4c44-8bc1-0b7cc00f858f" />
</p>

<p align="center"> 
  Architecture of the Security Policy Generation with Prompt Ensembling pipeline
</p>

<br>

Source(s):
- https://datatracker.ietf.org/doc/draft-ietf-i2nsf-consumer-facing-interface-dm/ (I2NSF Consumer-Facing Interface YANG Data Model | draft-ietf-i2nsf-consumer-facing-interface-dm-31)
- https://github.com/CESNET/libyang (libyang)

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
  - '[baseline1](https://github.com/WindJammer6/37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling/tree/main/experiments/baseline1)', '[ensemble1](https://github.com/WindJammer6/37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling/tree/main/experiments/ensemble1)', '[ensemble2](https://github.com/WindJammer6/37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling/tree/main/experiments/ensemble2)', '[ensemble3](https://github.com/WindJammer6/37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling/tree/main/experiments/ensemble3)', '[ensemble3_1](https://github.com/WindJammer6/37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling/tree/main/experiments/ensemble3_1)' files all use the [GPT-4o-mini model](https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/)
  - 'miscellaneous_experiments' folder are experiments that I forgot to keep track and didn't have their complementing set of XML policies and/or results
  - the final results are taken from the '[baseline1](https://github.com/WindJammer6/37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling/tree/main/experiments/baseline1)', and 'ensemble5' folder/experiments
  - '[validate-policies.py](https://github.com/WindJammer6/37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling/blob/main/experiments/validate_policies.py)' file uses [yanglint](https://github.com/CESNET/libyang) to validate if the generated XML policies conform to the [YANG data model](https://datatracker.ietf.org/doc/draft-ietf-i2nsf-consumer-facing-interface-dm/) (checks if the generated XML policies are syntactically correct)
  - '[yang-modules](https://github.com/WindJammer6/37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling/tree/main/experiments/yang-modules)' folder stores the modules that specifies the [YANG data model](https://datatracker.ietf.org/doc/draft-ietf-i2nsf-consumer-facing-interface-dm/). These modules are imported into the '[validate-policies.py](https://github.com/WindJammer6/37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling/blob/main/experiments/validate_policies.py)' file

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

- '[original_main.py](https://github.com/WindJammer6/37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling/blob/main/original_main.py)' file - the baseline LLM. Code taken from the preceding paper: [Security Policy Generation for Cloud-Based Security Services using Large Language Model](http://iotlab.skku.edu/publications/domestic-conference/KICS-2025-Winter-LLM-Based-Security-Policy-Generation.pdf)'s source code, https://github.com/jaehoonpauljeong/Data-Modeling-Group-2-Project

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
**Syntactic Correctness Comparison**  
Minimal external equirements in this project, the main one is the [OpenAI API Python library](https://platform.openai.com/docs/libraries).

1. Add in your OpenAI API key, then simply run the latest version of the prompt ensembling pipeline, '[main_v4.py](https://github.com/WindJammer6/37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling/blob/main/main_v4.py)', which will generate a text file of the compiled XML policies for all 50 syntactic policy intents dataset
2. Pass the generated text file to the '[text_to_xml.py](https://github.com/WindJammer6/37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling/blob/main/helpers/text_to_xml.py)' file in the '[helpers](https://github.com/WindJammer6/37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling/tree/main/helpers)' folder to generate a folder with 50 XML files of the generated policies from the 50 syntactic policy intents dataset
3. Pass all 50 XML files of the generated policies from the 50 syntactic policy intents dataset through [yanglint](https://github.com/CESNET/libyang), in the '[validate-policies.py](https://github.com/WindJammer6/37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling/blob/main/experiments/validate_policies.py)' file in the '[experiments](https://github.com/WindJammer6/37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling/tree/main/experiments)' folder to generate a log that shows the results of the syntactic validation

**Qualitative Output Comparison**  

**Functional Testing on a Virtual Testbed**  

<br>

## Results <a name = "results"></a>
**Syntactic Correctness Comparison**  
<img width="1911" height="890" alt="image" src="https://github.com/user-attachments/assets/f18fdaaf-7786-4dd0-9836-c098c7ea1e81" />

Results from taking the average of 3 experimental runs for each of them:
- Baseline LLM - 0% syntactically correct generated XML policies
- Prompt Ensembling with GPT-4o-mini - ~50% syntactically correct generated XML policies
- Prompt Ensembling with GPT-5-mini - ~80% syntactically correct generated XML policies

 The syntactic correctness experiment file only works in a Linux virtual environment.

**Qualitative Output Comparison**  

**Functional Testing on a Virtual Testbed**  

<br>

Random additional notes: Past ideas tried but didn't get to work to reduce LLM hallucinations in Security Policy Generation: 
- [Acurai](https://arxiv.org/html/2412.05223v1)
- [Chain of Thought (CoT)](https://arxiv.org/abs/2201.11903)
- [ReAct](https://arxiv.org/abs/2210.03629)

<br>

Limitations note: GPT 5 mini takes a lot longer to generate intent to policy compared to GPT 4o mini. GPT 4o mini generates full 50 in an hour, but after an hour GPT 5 mini only generated like 18 only.
