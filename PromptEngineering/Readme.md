Zero Shot 

- Asking/Instructing an LLM to perform a task without any specific training or examples. 

```
Example: Classify the statement as true or false.

The Eiffel tower is located in Paris.

```

One Shot 

- Instructing an LLM to perform a task by giving a single example.

Example: 

![OneShot](OneShotPrompt.png)

Few-shot prompt 

- Learns from small set of examples before instructing the LLM to perform a given task. 

![FewShot](FewShotPrompt.png)

COT Prompt

![COT](COT.png)

![SelfConsistency](SelfConsistency.png)

![Prompt Template](PromptTemplate.png)

```
from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template("Tell me {adjective} joke about {content}")

prompt_template.format(adjective="funny", content="sport")

```