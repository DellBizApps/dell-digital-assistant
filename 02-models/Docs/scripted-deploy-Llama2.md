# Using scripts to deploy an LLM model with the Caikit+TGIS Serving runtime

Note: If you prefer to deploy and remove an LLM model by using step-by-step commands (instead of scripts), see [Deploying an LLM model with the Caikit+TGIS Serving runtime](deploy-remove.md).

**Prerequisites**

* You installed the **Caikit-TGIS-Serving** image as described in the [Caikit-TGIS-Serving README file](/01-rhods/README.md).

* You installed the scripts as described in [Script-based Installation](scriptsEADME.md).

* Your current working directory is the `/caikit-tgis-serving/demo/kserve/` directory.

**Procedure**

1. Deploy a sample LLM model.

   ~~~
   export TEST_NS=kserve-demo
   ./scripts/test/deploy-model.sh
   ~~~

2. Perform inference with a gRPC call.

   ~~~
   export TEST_NS=kserve-demo
   ./scripts/test/grpc-call.sh
   ~~~
