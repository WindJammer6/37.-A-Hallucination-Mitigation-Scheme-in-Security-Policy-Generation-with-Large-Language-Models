# 37.-Mitigating-Hallucination-in-Security-Policy-Generation-with-Prompt-Ensembling

Say this approach can be used to generate syntactically correct machine code for another types of applications as well. Useful for using creating agentic pipelines with LLM, when language -> machine code must be accurately enforced using an LLM (with minimal hallucinations) as to ensure the pipeline works most of the time. Anyways, even if the the generated machine code fails in the pipeline, the LLM can try regenerating again until the correct syntax machine code is produced as a fallback. (examples of machine code be: fixed schemas like XML or JSON for other applications).

(Maybe create a table for this?)  
Iteration 1: Just RAG (but fails to handle context and correct fields. It can only fix certain fields.) 0%  
Iteration 2: Prompt Ensembling + Schema checker 54%  
Iteration 3: Must try introduce Acurai, Chain of THought, ReAct, RAG, stronger LLM models ??%  

Compare GPT 4o-mini with GPT 5, deepseek or any other stronger models based on the number of syntactically correct outputs in experiments section

<br>

## How to run the experiments?



Note: GPT 5 mini takes a lot longer to generate intent to policy compared to GPT 4o mini. GPT 4o mini generates full 50 in an hour, but after an hour GPT 5 mini only generated like 18 only.
