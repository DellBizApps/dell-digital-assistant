// To do
oc get packagemanifests -n openshift-marketplace

oc describe packagemanifests <operator_name> -n openshift-marketplace

### Install NFD Operator
    ~~~
    oc create -f nfd-namespace.yaml
    oc create -f nfd-operatorgroup.yaml
    oc create -f nfd-subcription.yaml
    ~~~

### Verification
    ~~~
    oc project openshift-nfd
    oc get pods
    ~~~

### Example output
    ~~~
    NAME                                      READY   STATUS    RESTARTS   AGE
    nfd-controller-manager-7f86ccfb58-vgr4x   2/2     Running   0          10m
    ~~~