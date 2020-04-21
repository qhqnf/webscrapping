# %%
from indeed import get_jobs as get_indeed_jobs
from stackoverflow import get_jobs as get_stackoverflow_jobs
from make_csv import save_to_file
# -*- coding:utf-8 -*-
# %%

indeed_jobs = get_indeed_jobs()

# %%

stackoverflow_jobs = get_stackoverflow_jobs()

# %%
jobs = indeed_jobs + stackoverflow_jobs

# %%
save_to_file(jobs)
