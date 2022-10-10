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
#### Health check endpoints results
