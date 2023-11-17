# KServe/Caikit/TGIS stack

## Installation

#### You have the alternative option of installing the KServe/Caikit/TGIS stack. Follow any one of the options mentioned below for installing KServe/Caikit/TGIS stack:-

- Using [Automated Script installation](../scripts/README.md).
#### [OR]
- Using [Step-by-step commands](step-by-step-install.md).

## Removel

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