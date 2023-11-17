# Redis Deployment and Configuration

[Redis](https://redis.io/) is an open source, in-memory data store that can be used as a Vector Store for your embeddings in a Retrieval Augmented Generation scenario.

## Using the Redis Enterprise Operator

- From the OperatorHub, install the Redis Enterprise Operator.

![Redis Operator](img/redis-operator.png)


- You can install the operator with the default value, in the the namespace you want to create your Redis cluster (the operator is namespace based).

#### Create new Project in Openshift cluster
```yaml
oc new-project redisdb
```
#### Create Security Context Constraints using the following yaml manifests
```yaml
apiVersion: security.openshift.io/v1
kind: SecurityContextConstraints
metadata:
  name: redis-enterprise-scc-v2
  annotations:
    kubernetes.io/description: redis-enterprise-scc is the minimal SCC needed to run Redis Enterprise nodes on Kubernetes.
      It provides the same features as restricted-v2 SCC, but allows pods to enable the SYS_RESOURCE capability,
      which is required by Redis Enterprise nodes to manage file descriptor limits and OOM scores for database shards.
      Additionally, it requires pods to run as UID/GID 1001, which are the UID/GID used within the Redis Enterprise node containers.
allowedCapabilities:
- SYS_RESOURCE
allowHostDirVolumePlugin: false
allowHostIPC : false
allowHostNetwork: false
allowHostPID: false
allowHostPorts: false
allowPrivilegeEscalation: false
allowPrivilegedContainer: false
readOnlyRootFilesystem: false
runAsUser:
  type: MustRunAs
  uid: 1001
fsGroup:
  type: MustRunAs
  ranges:
  - min: 1001
    max: 1001
seLinuxContext:
  type: MustRunAs
seccompProfiles:
- runtime/default
supplementalGroups:
  type: RunAsAny
```
#### Provide the operator permissions for Redis Enterprise Operator and Cluster pods 

```bash
 oc adm policy add-scc-to-user redis-enterprise-scc system:serviceaccount:redisdb:redis-enterprise-operator
 oc adm policy add-scc-to-user redis-enterprise-scc system:serviceaccount:redisdb:rec
```

#### Now you can deploy the Redis Enterprise Operator using openshift dashboard
you can follow this [link](https://developer.redis.com/create/openshift/) for visusl walkthrough of Redis Enterprise Operator installation in Openshift cluster

### Once the operator is deployed, create a Redis cluster. You can use the following YAML definition as an example (adapt to your needs regarding size, persistency, storageClass...):

```yaml
apiVersion: app.redislabs.com/v1
kind: RedisEnterpriseCluster
metadata:
  name: rec
  namespace: redisdb
spec:
  serviceAccountName: rec
  redisEnterpriseNodeResources:
    limits:
      cpu: '4'
      ephemeral-storage: 10Gi
      memory: 4Gi
    requests:
      cpu: '4'
      ephemeral-storage: 1Gi
      memory: 4Gi
  bootstrapperImageSpec:
    repository: registry.connect.redhat.com/redislabs/redis-enterprise-operator
  clusterCredentialSecretName: rec
  nodes: 3
  persistentSpec:
    enabled: true
    storageClassName: gp3-csi
    volumeSize: 20Gi
  createServiceAccount: true
  username: your_admin_username
  clusterCredentialSecretRole: ''
  podStartingPolicy:
    enabled: false
    startingThresholdSeconds: 540
  redisEnterpriseServicesRiggerImageSpec:
    repository: registry.connect.redhat.com/redislabs/services-manager
  redisEnterpriseImageSpec:
    imagePullPolicy: IfNotPresent
    repository: registry.connect.redhat.com/redislabs/redis-enterprise
  uiServiceType: ClusterIP
  clusterCredentialSecretType: kubernetes
  servicesRiggerSpec:
    databaseServiceType: 'cluster_ip,headless'
    serviceNaming: bdb_name
  services:
    apiService:
      type: ClusterIP
```

### Once the Redis cluster is ready you can deploy a DataBase to host the vector store. The important parts in our scenario are to enable the **Search module**, and set **enough memory** to hold the initial index capacity. Here is an example:

- Create the secret for for the redis database using following YAML definition as an example.
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: redb-my-doc
  namespace: redisdb
type: Opaque
stringData:
  username: default
  password: '************'
```
- Create the redis database using following YAML definition as an example
```yaml
apiVersion: app.redislabs.com/v1alpha1
kind: RedisEnterpriseDatabase
metadata:
  name: my-doc
  namespace: redisdb
spec:
  databaseSecretName: redb-my-doc
  memorySize: 4GB
  modulesList:
    - name: search
      version: 2.8.4
  persistence: snapshotEvery12Hour
  replication: true
  tlsMode: disabled
  type: redis
```

- Once the DataBase is deployed you will have:
  - A Secret named `redb-my-doc` (or the name you put in the YAML). It holds the password to the `default` user account for this database.
  - A Service named `my-doc-headless` (or the name you put in the YAML). From this Service you will get: 1. the full URL to the service from within the cluster, e.g. `my-doc-headless.my-namespace.svc.cluster.local`, 2. the port that Redis is listening to, e.g. `14155`.

- With the above information, when asked your your Redis URL in the different Notebooks or Applications on this repo, the full URI you can construct will be in the form: `redis://default:password@server:port`. With our example it would be: `redis://default:1a2b3c4d@my-doc-headless.redisdb.svc.cluster.local:14155`.