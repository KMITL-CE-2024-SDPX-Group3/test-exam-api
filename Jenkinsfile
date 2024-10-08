pipeline{
    agent any

    environment{
        APP_NAME = "SDPX G3 - TEST EXAM API"
        VENV_NAME = 'myenv'

    }
    stages{
        stage("Setup Python Environment"){
            agent {
                label "VM-Test"
            }
            steps {
                sh "python3 -m venv ${VENV_NAME}"
                sh ". ${VENV_NAME}/bin/activate"
            }
        }

        stage("Install Python Dependencies"){
            agent {
                label "VM-Test"
            }
            steps {
                sh "${VENV_NAME}/bin/pip install -r requirements.txt"
            }
        }

        stage("Run Unit Test"){
            agent {
                label "VM-Test"
            }
            steps {
                sh ". ${VENV_NAME}/bin/activate && python3 -m unittest tests/test_exam_app.py"
            }
        }

        stage("Build Docker Image"){
            agent {
                label "VM-Test"
            }
            steps {
                sh "docker compose build"
                sh "docker ps"
            }
        }

        stage("Run Docker Container"){
            agent {
                label "VM-Test"
            }
            steps {
                sh "docker compose up -d"
            }
        }

        stage("Clone exam-api-robot repository"){
            agent {
                label "VM-Test"
            }
            steps {
                sh "rm -rf exam-api-robot"
                sh "git clone https://github.com/KMITL-CE-2024-SDPX-Group3/exam-api-robot"
            }
        }

        stage("Run Robot Test"){
            agent {
                label "VM-Test"
            }
            steps {
                sh ". ${VENV_NAME}/bin/activate && robot exam-api-robot/exam-app.robot"
            }
        }

        stage("Push Docker Image") {
            agent {
                label "VM-Test"
            }
            steps {
                withCredentials(
                    [usernamePassword(
                        credentialsId: "Sun-GitHub-SDPX",
                        passwordVariable: "GITHUB_PASSWORD",
                        usernameVariable: "GITHUB_USERNAME"
                    )]
                ){
                    sh "docker login ghcr.io -u ${GITHUB_USERNAME} -p ${GITHUB_PASSWORD}"
                    sh "docker compose push"
                }
            }
        }

        stage("Stop Docker Container and Remove Image"){
            agent {
                label "VM-Test"
            }
            steps {
                sh "docker compose down --rmi local"
            }
        }
        
        stage("PreProd - Clean Up Docker Resource"){
            agent {
                label "VM-PreProd"
            }
            steps {
                // Stop and remove all running and exited containers
                sh "docker stop \$(docker ps -q) || true"
                sh "docker rm \$(docker ps -a -q) || true"

                // Remove unused images and volumes
                sh "docker rmi \$(docker images -q) || true"
                sh "docker system prune --volumes -f || true"
            }
        }

        stage("PreProd - Pull Image"){
            agent {
                label "VM-PreProd"
            }
            steps {
                withCredentials(
                    [usernamePassword(
                        credentialsId: "Sun-GitHub-SDPX",
                        passwordVariable: "GITHUB_PASSWORD",
                        usernameVariable: "GITHUB_USERNAME"
                    )]
                ){
                    sh "docker login ghcr.io -u ${GITHUB_USERNAME} -p ${GITHUB_PASSWORD}"
                    sh "docker compose pull"
                }
            }
        }

        stage("PreProd - Run Container from Image"){
            agent {
                label "VM-PreProd"
            }
            steps {
                sh "docker compose up -d"
            }
        }
    }

    post {
        always {
            // Clean up the virtual environment
            sh "rm -rf ${VENV_NAME}"
        }
    }
}