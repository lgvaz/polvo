# Miscellaneous


<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

------------------------------------------------------------------------

<a
href="https://github.com/lgvaz/polvo/blob/master/polvo/utils/wandb.py#L11"
target="_blank" style="float:right; font-size:smaller">source</a>

### WandbRun

>      WandbRun (run=None, **kwargs)

*Context manager that finishes run when exiting*

------------------------------------------------------------------------

<a
href="https://github.com/lgvaz/polvo/blob/master/polvo/utils/wandb.py#L20"
target="_blank" style="float:right; font-size:smaller">source</a>

### wandb_upload

>      wandb_upload (artifact_name:str, *path:str, project=None, type='dataset',
>                    run=None)

*Uploads files or dir to wandb*

``` python
with WandbRun(project='test', job_type='test') as run:
    wandb_upload('test_upload', '01v_utils.wandb.ipynb', run=run)
```

    wandb: Currently logged in as: agscard. Use `wandb login --relogin` to force relogin

wandb version 0.15.0 is available!  To upgrade, please run:
 $ pip install wandb --upgrade
Tracking run with wandb version 0.14.2
Run data is saved locally in <code>/home/lgvaz/git/polvo/nbs/wandb/run-20230424_153328-dqy4wcia</code>
Syncing run <strong><a href='https://wandb.ai/agscard/test/runs/dqy4wcia' target="_blank">icy-waterfall-1</a></strong> to <a href='https://wandb.ai/agscard/test' target="_blank">Weights & Biases</a> (<a href='https://wandb.me/run' target="_blank">docs</a>)<br/>
 View project at <a href='https://wandb.ai/agscard/test' target="_blank">https://wandb.ai/agscard/test</a>
 View run at <a href='https://wandb.ai/agscard/test/runs/dqy4wcia' target="_blank">https://wandb.ai/agscard/test/runs/dqy4wcia</a>
Waiting for W&B process to finish... <strong style="color:green">(success).</strong>
 View run <strong style="color:#cdcd00">icy-waterfall-1</strong> at: <a href='https://wandb.ai/agscard/test/runs/dqy4wcia' target="_blank">https://wandb.ai/agscard/test/runs/dqy4wcia</a><br/>Synced 5 W&B file(s), 0 media file(s), 1 artifact file(s) and 0 other file(s)
Find logs at: <code>./wandb/run-20230424_153328-dqy4wcia/logs</code>