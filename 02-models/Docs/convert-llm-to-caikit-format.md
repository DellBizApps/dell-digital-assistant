# Bootstrap process (optional)

Caikit-TGIS image always requires a Caikit-formatted model. Below are the instructions from converting a model to a Caikit-formatted one.

1. Clone the model repository (or have the model folder in a directory). In the below example, Bloom-560m model repo is cloned.
~~~
yum -y install git git-lfs
git lfs install
git clone https://huggingface.co/meta-llama/Llama-2-7b-hf
~~~

2. Clone the caikit-nlp repo:
~~~
git clone https://github.com/caikit/caikit-nlp.git
~~~

3. Create a virtual environment with Python 3.9 and install the caikit-nlp
~~~
python3 -m virtualenv -p python3.9 venv
source venv/bin/activate
python3.9 -m pip install ./caikit-nlp
~~~

4. (Optional) Clone the caikit-tgis-serving repo, if not already available.
~~~
git clone https://github.com/opendatahub-io/caikit-tgis-serving.git
~~~

5. Invoke the conversion script located in /utils of caikit-tgis-serving repo.
~~~
cp caikit-tgis-serving/utils/convert.py . 
./convert.py --model-path ./Llama-2-7b-hf --model-save-path ./Llama-2-7b-hf-caikit
~~~

6. Move the model folder (ie. `/Llama-2-7b-hf-caikit`) into desired storage (ie. S3, MinIO, PVC or other)
7. Do *not* include the model folder name/directory directly in InferenceService, but rather point to the directory where the model folder is located. Let's say the `Llama-2-7b-hf-caikit` directory is located at: `example-models/llm/models/Llama-2-7b-hf-caikit/`, then `storageUri` value in the InferenceService CR should look like:
~~~
storageUri: s3://example-models/llm/models
~~~