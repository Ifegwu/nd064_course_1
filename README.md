# nd064_C1
### Cloud Native Fundamentals Scholarship Program Nanodegree Program

**Course Homepage**: https://sites.google.com/udacity.com/suse-cloud-native-foundations/home

**Instructor**: https://github.com/kgamanji
----
### Project Section
----
### Background
TechTrends is an online website used as a news sharing platform, that enables consumers to access the latest news within the cloud-native ecosystem. In addition to accessing the available articles, readers are able to create new media articles and share them.

Imagine the following scenario: you joined a small team as a Platform Engineer. The team is composed of 2 developers, 1 platform engineer (you), 1 project manager, and 1 manager. The team was assigned with the TechTrends project, aiming to build a fully functional online news sharing platform. The developers in the team are currently working on the first prototype of the TechTrends website. As a platform engineer, you should **package and deploy** TechTrends to Kubernetes using a CI/CD pipeline.

The web application is written using the [Python Flask framework](https://flask.palletsprojects.com/en/1.1.x/). It uses [SQLite](https://docs.python.org/3/library/sqlite3.html), a lightweight disk-based database to store the submitted articles.

Below you can examine the main components of the firsts prototype of the application:
![workflow](https://user-images.githubusercontent.com/9282421/194753550-b0cdcf14-6896-424e-8673-feaab9b108e6.png)

#### The site map
![sitemap](https://user-images.githubusercontent.com/9282421/194753699-6a883f4c-1865-49ea-be91-6386fc37a2b1.png)

### Project Steps Overview
----
1. Apply the best development practices and develop the status and health check endpoints for the TechTrends application.
2. Package the TechTrends application by creating a Dockerfile and Docker image.
3. Implement the Continuous Integration practices, by using GitHub Actions to automate the build and push of the Docker image to DockerHub.
4. Construct the Kubernetes declarative manifests to deploy TechTrends to a sandbox namespace within a Kubernetes cluster. The cluster should be   provisioned using k3s in a vagrant box.
5. Template the Kubernetes manifests using a Helm chart and provide the input configuration files for staging and production environments.
6. Implement the Continuous Delivery practices, by deploying the TechTrends application to staging and production environments using ArgoCD and the Helm chart.

### Step 1
#### Docker running locally
```
~/project/nd064_course_1$ docker build -t techtrends .
~/project/nd064_course_1$ docker tag techtrends dannie13/techtrends:v1.0.0
~/project/nd064_course_1$ docker run -d -p 7111:3111 techtrends
```

![1a_docker-run-local](https://user-images.githubusercontent.com/9282421/195630370-5a9620e9-74ae-4bdc-b15b-deeb6a5d6df5.png)

#### Logs from the container running the TechTrends application

```
~/project/nd064_course_1$ docker logs -f $$(docker ps | grep techtrends | tr " " "" | tail -1)
```
```
- Serving Flask app 'app' (lazy loading)
- Environment: development
- Debug mode: on
  2022-10-13 14:04:15,278 WARNING _ Running on all addresses.
  WARNING: This is a development server. Do not use it in a production deployment.
  2022-10-13 14:04:15,278 WARNING _ Running on all addresses.
  WARNING: This is a development server. Do not use it in a production deployment.
  2022-10-13 14:04:15,278 INFO _ Running on http://172.17.0.2:3111/ (Press CTRL+C to quit)
  2022-10-13 14:04:15,278 INFO _ Running on http://172.17.0.2:3111/ (Press CTRL+C to quit)
  2022-10-13 14:04:15,280 INFO _ Restarting with stat
  2022-10-13 14:04:15,280 INFO _ Restarting with stat
  2022-10-13 14:04:16,041 WARNING _ Debugger is active!
  2022-10-13 14:04:16,041 WARNING _ Debugger is active!
  2022-10-13 14:04:16,041 INFO _ Debugger PIN: 131-590-675
  2022-10-13 14:04:16,041 INFO _ Debugger PIN: 131-590-675
  2022-10-13 14:04:46,784 INFO status request successful
  2022-10-13 14:04:46,784 INFO status request successful
  2022-10-13 14:04:46,786 INFO 172.17.0.1 - - [13/Oct/2022 14:04:46] "GET /healthz HTTP/1.1" 200 -
  2022-10-13 14:04:46,786 INFO 172.17.0.1 - - [13/Oct/2022 14:04:46] "GET /healthz HTTP/1.1" 200 -
  2022-10-13 14:04:58,390 INFO post request metrics successful
  2022-10-13 14:04:58,390 INFO post request metrics successful
  2022-10-13 14:04:58,391 INFO 172.17.0.1 - - [13/Oct/2022 14:04:58] "GET /metrics HTTP/1.1" 200 -
  2022-10-13 14:04:58,391 INFO 172.17.0.1 - - [13/Oct/2022 14:04:58] "GET /metrics HTTP/1.1" 200 -
  2022-10-13 14:05:09,105 INFO posts succefully fetch
  2022-10-13 14:05:09,105 INFO posts succefully fetch
  2022-10-13 14:05:09,137 INFO 172.17.0.1 - - [13/Oct/2022 14:05:09] "GET / HTTP/1.1" 200 -
  2022-10-13 14:05:09,137 INFO 172.17.0.1 - - [13/Oct/2022 14:05:09] "GET / HTTP/1.1" 200 -
  2022-10-13 14:05:09,157 INFO 172.17.0.1 - - [13/Oct/2022 14:05:09] "GET /static/css/main.css HTTP/1.1" 304 -
  2022-10-13 14:05:09,157 INFO 172.17.0.1 - - [13/Oct/2022 14:05:09] "GET /static/css/main.css HTTP/1.1" 304 -
  2022-10-13 14:05:12,302 INFO <sqlite3.Row object at 0x7f88fd6d1270> succesfully fetch
  2022-10-13 14:05:12,302 INFO posts request successful
  2022-10-13 14:05:12,302 INFO <sqlite3.Row object at 0x7f88fd6d1270> succesfully fetch
  2022-10-13 14:05:12,302 INFO posts request successful
  2022-10-13 14:05:12,309 INFO 172.17.0.1 - - [13/Oct/2022 14:05:12] "GET /1 HTTP/1.1" 200 -
  2022-10-13 14:05:12,309 INFO 172.17.0.1 - - [13/Oct/2022 14:05:12] "GET /1 HTTP/1.1" 200 -
  2022-10-13 14:05:12,332 INFO 172.17.0.1 - - [13/Oct/2022 14:05:12] "GET /static/css/main.css HTTP/1.1" 304 -
  2022-10-13 14:05:12,332 INFO 172.17.0.1 - - [13/Oct/2022 14:05:12] "GET /static/css/main.css HTTP/1.1" 304 -
  2022-10-13 14:05:13,750 INFO about request successful
  2022-10-13 14:05:13,750 INFO about request successful
  2022-10-13 14:05:13,755 INFO 172.17.0.1 - - [13/Oct/2022 14:05:13] "GET /about HTTP/1.1" 200 -
  2022-10-13 14:05:13,755 INFO 172.17.0.1 - - [13/Oct/2022 14:05:13] "GET /about HTTP/1.1" 200 -
  2022-10-13 14:05:13,777 INFO 172.17.0.1 - - [13/Oct/2022 14:05:13] "GET /static/css/main.css HTTP/1.1" 304 -
  2022-10-13 14:05:13,777 INFO 172.17.0.1 - - [13/Oct/2022 14:05:13] "GET /static/css/main.css HTTP/1.1" 304 -
  2022-10-13 14:05:14,842 INFO title and content successful created
  2022-10-13 14:05:14,842 INFO title and content successful created
  2022-10-13 14:05:14,848 INFO 172.17.0.1 - - [13/Oct/2022 14:05:14] "GET /create HTTP/1.1" 200 -
  2022-10-13 14:05:14,848 INFO 172.17.0.1 - - [13/Oct/2022 14:05:14] "GET /create HTTP/1.1" 200 -
  2022-10-13 14:05:14,867 INFO 172.17.0.1 - - [13/Oct/2022 14:05:14] "GET /static/css/main.css HTTP/1.1" 304 -
  2022-10-13 14:05:14,867 INFO 172.17.0.1 - - [13/Oct/2022 14:05:14] "GET /static/css/main.css HTTP/1.1" 304 -
  2022-10-13 14:05:20,620 INFO None succesfully fetch
  2022-10-13 14:05:20,620 INFO None succesfully fetch
  2022-10-13 14:05:20,620 INFO 404 page return
  2022-10-13 14:05:20,620 INFO 404 page return
  2022-10-13 14:05:20,624 INFO 172.17.0.1 - - [13/Oct/2022 14:05:20] "GET /404 HTTP/1.1" 404 -
  2022-10-13 14:05:20,624 INFO 172.17.0.1 - - [13/Oct/2022 14:05:20] "GET /404 HTTP/1.1" 404 -
  2022-10-13 14:05:20,645 INFO 172.17.0.1 - - [13/Oct/2022 14:05:20] "GET /static/css/main.css HTTP/1.1" 304 -
  2022-10-13 14:05:20,645 INFO 172.17.0.1 - - [13/Oct/2022 14:05:20] "GET /static/css/main.css HTTP/1.1" 304 -
```
### Step 2: Continuous Integration (CI)
#### Docker built and pushed with Github Actions
![2a_ci-github-actions-1](https://user-images.githubusercontent.com/9282421/195634564-350a9a90-1e65-404a-9089-e360e4283085.png)
![2a_ci-github-actions-2](https://user-images.githubusercontent.com/9282421/195634583-7cdc51d0-b2ba-4202-9f17-ff0b23a05a45.png)
![2a_ci-github-actions-3](https://user-images.githubusercontent.com/9282421/195634616-b817e6b6-0618-451c-ae01-9b1ae3a0ae4f.png)

#### DockerHub Techtrends Image

![2b_ci-dockerhub](https://user-images.githubusercontent.com/9282421/195635218-aed30c44-e958-4c21-b97b-af51b45fee76.png)

### Step 3: Kubernetes Declarative Manifests
----
#### Deploy a Kubernetes cluster
```
~/project/nd064_course_1$ vagrant up
~/project/nd064_course_1$ vagrant ssh
vagrant@localhost:~> curl -sfL https://get.k3s.io | sh -
vagrant@localhost:~> sudo su
localhost:/home/vagrant # k3s kubectl get node
```
![3a_k8s-nodes](https://user-images.githubusercontent.com/9282421/195638833-aab19b3d-b410-4730-b033-b7c60e4565cf.png)

#### Deploy TechTrends with Kubernetes manifests
```
localhost:/home/vagrant # kubectl apply -f namespace.yaml 
localhost:/home/vagrant # kubectl apply -f deploy.yaml
localhost:/home/vagrant # kubectl apply -f service.yaml
localhost:/home/vagrant # kubectl get all -n sandbox
```

![3b_kubernetes-declarative-manifests](https://user-images.githubusercontent.com/9282421/195641091-6e855328-19b6-4a65-8dc8-7544a6940ef2.png)

#### Step 4: Helm Charts
#### Deploy to staging and production environment with Helm files
```
localhost:/home/vagrant # kubectl apply -f values-staging.yaml
localhost:/home/vagrant # kubectl apply -f values-prod.yaml
```
### Step 5: Continuous Delivery (CD) with ArgoCD
#### Deploy ArgoCD
```
localhost:/home/vagrant # kubectl create namespace argocd
localhost:/home/vagrant # kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```
#### Create the NodePort service for ArgoCD server by using the 
```
localhost:/home/vagrant # kubectl apply -f argocd-server-nodeport.yaml
```
#### Generate password for ArgoCD UI
```
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d; echo
```
#### Access the ArgoCD UI by going to https://192.168.50.4:30008 or http://192.168.50.4:30007

![4a_argocd-ui](https://user-images.githubusercontent.com/9282421/195645331-021882f8-bf55-49d6-b800-ac69f3ec7c71.png)

#### Deploy TechTrends with ArgoCD
```
localhost:/home/vagrant # kubectl apply -f helm-techtrends-staging.yaml
localhost:/home/vagrant # kubectl apply -f helm-techtrends-prod.yaml
```
![4b_argocd-techtrends-staging](https://user-images.githubusercontent.com/9282421/195646554-e66d03a6-7cdd-4672-b61a-f507738f020d.png)
![4c_argocd-techtrends-prod](https://user-images.githubusercontent.com/9282421/195646584-cd7dd199-f972-47ee-9ae5-2749466b2344.png)


