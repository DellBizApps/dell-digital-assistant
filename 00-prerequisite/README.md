# Prerequisite for the deployment.

1. User Creation : We need to make sure sure we have an openshift user (not the default kubeadmin) present in the OCP cluster. If not we will create the user and assign the approprite role. [Here]() is sample example of user creation in OCP Cluster.

2. Configure Openshift internal registry : [Sample example]() for configuring Openshift internal registry

3. In most of the data science project, we use GPU for enhansing the computation of the overall process. you can follow following sample to deploy Nvdia GPU Operator to your openshift cluster. 

> [!importent]
> This operator will only work if you have Nvidia GPU already present on nodes of your Openshift cluster.

a. [Install Openshift NFD Operator]() to discover GPU present on your openshift cluster nodes.
b. [Install Nvidia GPU Opeartor]()
c. [Validate Nvidia GPU installation]()