cd dell-digital-assistant/

pip install langchain bs4 PyPDFium2 gradio
pip install sentence-transformers
pip install redis

podman build -t quay.io/dellbizapps/ai/dell-redis-ingest-ui:v0.0.1

oc create secret docker-registry quaypullsec     --docker-server=quay.io     --docker-username=xxxxxxxx     --docker-password=xxxxxx     --docker-email=xxxxx@xxxx.com
oc secrets link default quaypullsec --for=pull