import requests
import os 


OWNER= "yadhardha"
REPO = "DevopsRagModel"

headers = {
    "Authorization":f"Bearer{TOKEN}",
    "Accept":"applications/vnd.github+json"
}

def fetch_data():
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/actions/runs"
    response= requests.get(url,headers=headers)
    data = response.json()

    dataset=[]
    for run in data["workflow_runs"]:
        run_id = run["id"]
        jobs_url = f"https://api.github.com/repos/{OWNER}/{REPO}/actions/runs/{run_id}/jobs"
        jobs = requests.get(jobs_url,headers=headers).json()
        for job in jobs["jobs"]:
            for step in job["steps"]:
                text = f"""
                Workflow: {run['name']}
                Run ID: {run_id}
                Job: {job['name']}
                Step: {step['name']}
                Status: {step['conclusion']}
                """

                dataset.append(text)

            return dataset
data = fetch_data()
print("Total records:", len(data))

for d in data[:5]:
    print("\n---")
    print(d)
