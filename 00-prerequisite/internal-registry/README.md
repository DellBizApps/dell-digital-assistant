# Configuring Openshift Internal registry

### Configure [OpenShift Internal registry](https://docs.openshift.com/container-platform/4.13/registry/configuring_registry_storage/configuring-registry-storage-baremetal.html)

* #### Change registry image config Management State from Removed to Manage
    ```
    oc patch configs.imageregistry.operator.openshift.io cluster --type merge --patch '{"spec":{"managementState":"Managed"}}'
    ```

* #### Create PVC to store the Image registry data

> [!IMPORTANT]
> Change the storageClassName in below code to match your environment storage class before running this code.

    ```
    cat <<EOF | oc apply -f -
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
    name: registry-storage-pvc
    namespace: openshift-image-registry
    spec:
    accessModes:
    - ReadWriteMany
    resources:
    requests:
        storage: 500Gi
    storageClassName: ocs-storagecluster-cephfs
    EOF
    ```

* #### Validate if PVC is created
    ~~~
    oc -n openshift-image-registry get pvc
    ~~~

* #### Patch storage details to the registry image config
    ~~~
    oc patch config.image/cluster -p '{"spec":{"managementState":"Managed","replicas":2,"storage":{"managementState":"Unmanaged","pvc":{"claim":"registry-storage-pvc"}}}}' --type=merge
    ~~~

* #### Validate if internal registry is up and running

    ```bash
    oc -n openshift-image-registry get pods
    ```
