# Remove the LLM model

   a. To remove (undeploy) the LLM model, delete the Inference Service.

   ~~~
   oc delete isvc --all -n ${TEST_NS} --force --grace-period=0
   ~~~

   b. Delete the MinIO resources by deleting the MinIO namespace.

   ~~~
   oc delete ns ${TEST_NS} ${MINIO_NS}