# KServe/Caikit/TGIS stack

### Script-based uninstall of Kserve and dependencies

1. Uninstall kserve (including `./script/test/delete-model.sh`):

   ~~~
   export TARGET_OPERATOR=rhods
   export TEST_NS=kserve-demo
   ./script/uninstall/kserve-uninstall.sh
   ~~~

2. Uninstall the dependencies:

   ~~~
   export TARGET_OPERATOR=rhods
   export TEST_NS=kserve-demo
   ./script/uninstall/dependencies-uninstall.sh
   ~~~