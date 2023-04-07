# Using the Ohio Supercomputing Center (OSC)

## Accessing OSC via Jupyter Notebooks

1. Visit [OSC OnDemand](https://ondemand.osc.edu) and log in using your OSC credentials.
2. After logging in, click on "Interactive Apps" in the menu across the top of the webpage.
3. Select "Jupyter" from the drop-down menu.
4. Configure the Jupyter app:
   - Choose the correct project ID that you received earlier.
   - Select the "GPU" session type and choose any available GPU.
   - For the CUDA version, choose the latest available option that is compatible with your project requirements.
5. Click "Launch" to start the Jupyter app.
6. When the Jupyter app is running, click "Connect to Jupyter" to open the JupyterLab interface.
7. In JupyterLab, open a new Python notebook with the latest version of Python.
8. Install the required PyTorch packages in the first cell:

~~~python
%pip install --user torch torchvision torchaudio
~~~

9. Verify that PyTorch is installed and can access the GPU in the next cell:

~~~python
import torch
torch.cuda.is_available()
~~~

You can now use PyTorch in any notebook on OSC. When training a model, choose a suitable GPU based on the expected training duration and resource requirements.

## Uploading Files to OSC

### Small Files

For small files, you can use the "Upload Files" button in JupyterLab:
1. Click the folder icon on the left sidebar to open the file browser.
2. Click the upward arrow icon (above the file list) to open the file upload dialog.
3. Select the files you want to upload and click "Open."

### Large Files

For larger files, you can use one of the following methods:

1. **OSC OnDemand File Manager**
   - Visit [OSC OnDemand](https://ondemand.osc.edu) and click "Files" in the top menu.
   - Use the file manager to navigate to the desired directory.
   - Click the "Upload" button and select the files you want to upload.

2. **FileZilla**
   - Install the FileZilla client software.
   - Connect to `sftp://sftp.osc.edu`.
   - Set the login type to "Interactive" to enable multi-factor authentication.
   - Navigate to the appropriate directory and upload your files.

3. **Command Line**
   - **rsync**
      ~~~
      rsync --progress -r local-dir <username>@sftp.osc.edu:/fs/scratch/PMUI0206
      ~~~
   - **SCP**
      ~~~
      scp src <username>@sftp.osc.edu:/fs/scratch/PMUI0206
      ~~~

## Accessing OSC via SSH

1. Open a terminal and connect to OSC using SSH:

~~~bash
ssh <username>@pitzer.osc.edu
~~~

## Creating Your Own Kernel 
1. Connect to OSC via SSH
~~~bash
ssh <username>@pitzer.osc.edu
~~~

2. Load the latest version of Python:

~~~bash
module keyword python
# Replace 3.9-2022.05 with whatever is most recent
module load python/3.9-2022.05
~~~

3. Create a new Conda environment named `cse627`:

~~~bash
conda create -n cse627 python~=3.9
~~~

4. Activate the new environment (use `source activate` instead of `conda activate` on OSC):

~~~bash
source activate cse627
~~~

5. Install the IPython kernel and register the environment as a JupyterLab kernel:

~~~bash
pip install ipykernel
python -m ipykernel install --user --name=cse627
~~~

6. Install any necessary dependencies, such as PyTorch:

~~~bash
python -m pip install torch torchvision torchaudio
~~~

To share this environment with your group, provide the following instructions:

1. Activate the shared environment:

~~~bash
source activate ~<your_username>/.conda/envs/cse627
~~~

2. Register the shared environment as a JupyterLab kernel:

~~~bash
python -m ipykernel install --user --name=cse627
~~~

Note that other users will not be able to install packages in your environment, but they can install packages using the \`--user\` flag for their own use.