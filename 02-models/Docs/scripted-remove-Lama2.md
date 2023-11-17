# Scripted removel of already deployed Llama2 model.


- Delete the sample model and the MinIO namespace.

   ~~~
   export TEST_NS=kserve-demo
   ./scripts/test/delete-model.sh
   ~~~