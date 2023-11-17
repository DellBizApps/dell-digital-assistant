## Installing Nvidia GPU Operator

#### Mode detail on installation and configuration of **Nvidia GPU Operator** could be found on [Nvidia website](https://docs.nvidia.com/datacenter/cloud-native/openshift/latest/install-gpu-ocp.html).

### Deploy Nvidia GPU Operator

#### 1. Create a namespace for the NVIDIA GPU Operator
    ~~~
    oc create -f nvidia-gpu-operator-ns.yaml
    ~~~

#### 2. Create a namespace for the NVIDIA GPU Operator
    ~~~
    oc create -f nvidia-gpu-operatorgroup.yaml
    ~~~

#### 3. Run the following command to get the channel value required for step number 5.
    ~~~
    oc get packagemanifest gpu-operator-certified -n openshift-marketplace -o jsonpath='{.status.defaultChannel}'
    ~~~

#### Example output
    ~~~
    v22.9
    ~~~

##### 4. Run the following commands to get the startingCSV value (based on value from previous step) required for step number 5.
    ~~~
    CHANNEL=v22.9
    oc get packagemanifests/gpu-operator-certified -n openshift-marketplace -ojson | jq -r '.status.channels[] | select(.name == "'$CHANNEL'") | .currentCSV'
    ~~~
#### Example output
    ~~~
    gpu-operator-certified.v22.9.0
    ~~~


#### 5. Create subscription by running the the following command
> [!NOTE] 
> Update the **channel** and **startingCSV** fields with the information returned in step 3 and 4 to [nvidia-gpu-sub.yaml] file. You can also change the **installPlanApproval: Manual** (In this case you have to perform step 6 as well)
    ~~~
    oc create -f nvidia-gpu-sub.yaml
    ~~~
#### Verify an install plan has been created:
    ~~~
    oc get installplan -n nvidia-gpu-operator
    ~~~

#### Nvidia GPU Operator install verification
    ~~~
    oc get installplan -n nvidia-gpu-operator
    ~~~
#### Example output
    ~~~
    NAME            CSV                              APPROVAL   APPROVED
    install-wwhfj   gpu-operator-certified.v22.9.0   Manual     false
    ~~~

#### 6. Approve the install plan using the CLI commands: (Perform this step only if the **installPlanApproval: Manual** was selected during subscription deployment)

    ~~~
    INSTALL_PLAN=$(oc get installplan -n nvidia-gpu-operator -oname)
    ~~~
    ~~~
    oc patch $INSTALL_PLAN -n nvidia-gpu-operator --type merge --patch '{"spec":{"approved":true }}'
    ~~~

#### Verify the operator
    ~~~
    oc get pods -n nvidia-gpu-operator
    ~~~
#### Example output
    ~~~
    NAME                                      READY   STATUS    RESTARTS   AGE
    nfd-controller-manager-7f86ccfb58-vgr4x   2/2     Running   0          10m
    ~~~

## Create the ClusterPolicy instance
    ~~~
    CSV=$(oc get csv -n nvidia-gpu-operator -oname | grep gpu-operator | awk 'BEGIN {FS="/";} {print $2}')
    oc get csv -n nvidia-gpu-operator $CSV -ojsonpath={.metadata.annotations.alm-examples} | jq .[0] > clusterpolicy.json
    ~~~
#### Now apply the cluster policy using following command ( this )
    ~~~
    oc apply -f clusterpolicy.json
    ~~~

## Verify the successful installation of the NVIDIA GPU Operator
    ~~~
    oc get pods,daemonset -n nvidia-gpu-operator
    ~~~

## Running a sample GPU Application
