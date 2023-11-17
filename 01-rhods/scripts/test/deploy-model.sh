#!/bin/bash
set -o pipefail
set -o nounset
set -o errtrace
# set -x   #Uncomment this to debug script.

source "$(dirname "$(realpath "$0")")/../env.sh"

# Deploy a sample model
oc get ns ${TEST_NS}
if [[ $? ==  1 ]]
then
  oc new-project ${TEST_NS}
  oc patch smmr/default -n istio-system --type='json' -p="[{'op': 'add', 'path': '/spec/members/-', 'value': \"$TEST_NS\"}]"

  oc apply -f ./custom-manifests/caikit/caikit-servingruntime.yaml -n ${TEST_NS}

  oc apply -f ./custom-manifests/caikit/storage-config-secret.yaml -n ${TEST_NS}
  oc apply -f ./custom-manifests/caikit/serviceaccount.yaml -n ${TEST_NS}

  oc apply -f ./custom-manifests/caikit/caikit-isvc.yaml -n ${TEST_NS}

  # Resources needed to enable metrics for the model
  # The metrics service needs the correct label in the `matchLabel` field. The expected value of this label is `<isvc-name>-predictor-default`
  # The metrics service in this repo is configured to work with the example model. If you are deploying a different model or using a different model name, change the label accordingly.
  oc apply -f custom-manifests/metrics/caikit-metrics-service.yaml -n ${TEST_NS}
  oc apply -f custom-manifests/metrics/caikit-metrics-servicemonitor.yaml -n ${TEST_NS}
else
  echo
  echo "* ${TEST_NS} exist. Please remove the namespace or use another namespace name"
fi