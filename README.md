# Dell Digital Assistant
## An example scenario for creating and deploying Dell Digital Assistant with Llama2 and Caikit in Red Hat OpenShift AI on Dell APEX Cloud platform for Open shift.

> [!NOTE] The steps and configuration options present in this GitHub repository is for example purpose only. Dell Technologies will not provide support for the code provided here. 

This [deployment guide](https://infohub.delltechnologies.com/t/design-guide-implementing-a-digital-assistant-with-red-hat-openshift-ai-on-dell-apex-cloud-platform-1/) describes the process of deploying a digital assistant using Red Hat OpenShift AI on Dell APEX Cloud Platform for Red Hat OpenShift. This solution is designed to create a cloud native AI application, with the ease of deployment and manageability. 


LLMs are highly sophisticated AI models designed to understand and generate human-like text, enabling a wide range of natural language processing applications. One limitation of LLMs is that once they are generated, LLMs do not have access to information beyond the date that they were trained. Retrieval Augmented Generation (RAG) can extend the functionality of the LLMs by retrieving facts from an external knowledge base, in this case, from a Redis in-memory Vector database. 

Digital assistants are designed to assist users by answering questions and processing simple tasks. Answers remain up to date and contain information unique to the organization by anchoring the model with relevant documentation. 

In this solution, we have deployed a LLM based digital assistant that can answer user queries related to domain specific documents. As text-based searches are limited in obtaining the right data, a digital assistant can help retrieve more accurate and relevant results using semantic search and natural language processing. 

The Red Hat OpenShift Container Platform provides a robust containerization platform and Kubernetes-based orchestration framework that enables organizations to build, deploy, and manage applications and databases efficiently across on-premises and multicloud environments. 

Dell APEX Cloud Platform for Red Hat OpenShift is designed collaboratively with Dell Technologies and Red Hat to optimize and extend OpenShift deployments on-premises with an integrated operational experience. By combining Dell’s expertise in delivering robust infrastructure solutions with Red Hat’s industry leading OpenShift Container Platform, this collaboration empowers organizations to start on a transformative journey towards modernization and innovation. 

The APEX Cloud Platform for Red Hat uses separate storage nodes to provide persistent storage for the compute cluster. This separation enables the compute and storage nodes to scale independently.  

Red Hat OpenShift AI offers organizations an efficient way to deploy an integrated set of common open-source and third-party tools to perform ML modeling. The ML models developed using Red Hat OpenShift AI are portable to deploy in production, on containers, on-premises, at the edge, or in the public cloud.  

Utilizing object storage for LLMs and huge datasets is crucial for modern data-driven applications, due to their reliability and scalability. Object storage is leveraged in this solution to store Llama 2 model, relevant datasets, and artifacts.  
